import { useState } from 'react'

function TransactionForm({ onAdd }) {
  // Form inputları için state tanımları
  const [baslik, setBaslik] = useState('')
  const [miktar, setMiktar] = useState('')
  const [tip, setTip] = useState('Gider') // Varsayılan: Gider
  const [tarih, setTarih] = useState('')

  // Form gönderildiğinde çalışacak fonksiyon
  const handleSubmit = (e) => {
    e.preventDefault()

    const yeniIslem = {
      kullanici_id: 1,
      baslik: baslik,
      miktar: parseFloat(miktar),
      tip: tip,
      tarih: tarih
    }

    // Backend API'ye POST isteği gönder
    fetch('http://localhost:8000/transactions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(yeniIslem),
    })
      .then(response => response.json())
      .then(data => {
        // Başarılı olursa listeyi hemen güncelle (Parent bileşeni tetikle)
        if (onAdd) {
          onAdd()
        }

        alert('İşlem başarıyla eklendi! 🎉')

        // Formu temizle
        setBaslik('')
        setMiktar('')
        setTarih('')
      })
      .catch(error => console.error('API Hatası:', error))
  }

  // Input stilleri
  const inputStyle = {
    width: '100%',
    padding: '12px',
    borderRadius: '8px',
    border: '1px solid #444',
    backgroundColor: '#2a2a2a',
    color: 'white',
    fontSize: '1em',
    outline: 'none',
    boxSizing: 'border-box' // Padding dahil genişlik hesapla
  }

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>

      {/* Başlık Input */}
      <div>
        <label style={{ display: 'block', marginBottom: '8px', color: '#aaa', fontSize: '0.9em' }}>Harcama/Gelir Başlığı</label>
        <input
          type="text"
          placeholder="Örn: Market Alışverişi"
          value={baslik}
          onChange={(e) => setBaslik(e.target.value)}
          required
          style={inputStyle}
        />
      </div>

      {/* Miktar ve Tip (Yan Yana) */}
      <div style={{ display: 'flex', gap: '15px' }}>
        <div style={{ flex: 1 }}>
          <label style={{ display: 'block', marginBottom: '8px', color: '#aaa', fontSize: '0.9em' }}>Miktar (TL)</label>
          <input
            type="number"
            placeholder="0.00"
            value={miktar}
            onChange={(e) => setMiktar(e.target.value)}
            required
            style={inputStyle}
          />
        </div>
        <div style={{ flex: 1 }}>
          <label style={{ display: 'block', marginBottom: '8px', color: '#aaa', fontSize: '0.9em' }}>İşlem Tipi</label>
          <select
            value={tip}
            onChange={(e) => setTip(e.target.value)}
            style={{ ...inputStyle, cursor: 'pointer' }}
          >
            <option value="Gider">Gider 💸</option>
            <option value="Gelir">Gelir 💰</option>
          </select>
        </div>
      </div>

      {/* Tarih */}
      <div>
        <label style={{ display: 'block', marginBottom: '8px', color: '#aaa', fontSize: '0.9em' }}>Tarih</label>
        <input
          type="date"
          value={tarih}
          onChange={(e) => setTarih(e.target.value)}
          required
          style={{ ...inputStyle, fontFamily: 'inherit' }}
        />
      </div>

      {/* Gönder Butonu */}
      <button
        type="submit"
        style={{
          marginTop: '10px',
          padding: '15px',
          backgroundColor: '#007bff',
          color: 'white',
          border: 'none',
          borderRadius: '8px',
          fontSize: '1.1em',
          fontWeight: 'bold',
          cursor: 'pointer',
          transition: 'background 0.3s'
        }}
        onMouseOver={(e) => e.target.style.backgroundColor = '#0056b3'}
        onMouseOut={(e) => e.target.style.backgroundColor = '#007bff'}
      >
        Ekle +
      </button>
    </form>
  )
}

export default TransactionForm
