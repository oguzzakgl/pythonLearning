import { useState, useEffect } from 'react'

function TransactionList({ refreshTrigger, onDelete }) {
    // İşlem verilerini ve aktif sekme bilgisini tutan state'ler
    const [transactions, setTransactions] = useState([])
    const [activeTab, setActiveTab] = useState('Hepsi') // Seçenekler: 'Hepsi', 'Gelir', 'Gider'
    const [searchTerm, setSearchTerm] = useState('') // Arama Kutusu State'i

    // Veri Çekme İşlemi (Fetching)
    // Sayfa yüklendiğinde veya refreshTrigger tetiklendiğinde çalışır.
    useEffect(() => {
        fetch('http://localhost:8000/transactions/1')
            .then(response => response.json())
            .then(data => {
                // Eğer data.transactions tanımlı değilse boş dizi ata
                setTransactions(data.transactions || [])
            })
            .catch(error => console.error("Veri çekme hatası:", error))
    }, [refreshTrigger])

    // İşlem Silme Fonksiyonu
    const handleDelete = (id) => {
        if (!confirm('Bu işlemi silmek istediğinize emin misiniz?')) return;

        fetch(`http://localhost:8000/transactions/${id}`, { method: 'DELETE' })
            .then(res => res.json())
            .then(data => {
                alert('İşlem silindi.')
                if (onDelete) onDelete() // Listeyi yenile
            })
            .catch(err => console.error('Silme hatası:', err))
    }

    // Filtreleme Mantığı: Hem SEKME hem de ARAMA filtresi
    const filteredTransactions = transactions.filter(t => {
        // 1. Sekme Filtresi
        const tabMatch = (activeTab === 'Hepsi') || (t[3] === activeTab)

        // 2. Arama Filtresi (Başlık içinde ara - Harf büyüklüğüne duyarsız)
        const searchMatch = t[1].toLowerCase().includes(searchTerm.toLowerCase())

        return tabMatch && searchMatch
    })

    // Sekme butonu için dinamik stil fonksiyonu
    const tabStyle = (tabName) => ({
        padding: '10px 20px',
        cursor: 'pointer',
        borderBottom: activeTab === tabName ? '3px solid #007bff' : '3px solid transparent',
        color: activeTab === tabName ? '#007bff' : '#555',
        fontWeight: 'bold',
        transition: 'all 0.3s ease'
    })

    return (
        <div>
            <h2>📋 İşlem Geçmişi</h2>

            {/* Arama ve Filtreleme Alanı */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                {/* Sekmeler */}
                <div style={{ display: 'flex', borderBottom: '1px solid #ddd' }}>
                    <div onClick={() => setActiveTab('Hepsi')} style={tabStyle('Hepsi')}>Hepsi</div>
                    <div onClick={() => setActiveTab('Gelir')} style={tabStyle('Gelir')}>Gelirler 💰</div>
                    <div onClick={() => setActiveTab('Gider')} style={tabStyle('Gider')}>Giderler 💸</div>
                </div>

                {/* Arama Kutusu */}
                <input
                    type="text"
                    placeholder="🔍 İşlem ara..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    style={{
                        padding: '8px',
                        borderRadius: '6px',
                        border: '1px solid #ccc',
                        width: '200px'
                    }}
                />
            </div>

            {/* Liste Görünümü */}
            {filteredTransactions.length === 0 ? (
                <p>Bu kriterlere uygun işlem bulunamadı.</p>
            ) : (
                <table border="1" cellPadding="10" style={{ width: '100%', borderCollapse: 'collapse' }}>
                    <thead>
                        <tr style={{ backgroundColor: '#f2f2f2' }}>
                            <th>Tarih</th>
                            <th>Başlık</th>
                            <th>Miktar</th>
                            <th>Tip</th>
                            <th>İşlem</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredTransactions.map((t, index) => (
                            <tr key={index} className="fade-in">
                                <td>{t[4]}</td>
                                <td>{t[1]}</td>
                                <td>{t[2]} TL</td>
                                <td style={{ color: t[3] === 'Gelir' ? 'green' : 'red', fontWeight: 'bold' }}>
                                    {t[3]}
                                </td>
                                <td>
                                    <button
                                        onClick={() => handleDelete(t[0])}
                                        style={{ backgroundColor: '#dc3545', color: 'white', border: 'none', padding: '5px 10px', borderRadius: '4px', cursor: 'pointer' }}
                                    >
                                        Sil 🗑️
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    )
}

export default TransactionList
