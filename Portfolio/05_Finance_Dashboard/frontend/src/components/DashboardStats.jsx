import { useState, useEffect } from 'react'

function DashboardStats({ refreshTrigger }) {
    const [stats, setStats] = useState({
        toplam_gelir: 0,
        toplam_gider: 0,
        bakiye: 0,
        en_cok_harcanan: '-'
    })

    useEffect(() => {
        fetch('http://localhost:8000/analysis/summary')
            .then(res => res.json())
            .then(data => {
                if (data) {
                    setStats(data)
                }
            })
            .catch(err => console.error(err))
    }, [refreshTrigger])

    const cardStyle = (color) => ({
        backgroundColor: 'white',
        padding: '20px',
        borderRadius: '10px',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
        textAlign: 'center',
        flex: 1,
        margin: '0 10px',
        borderTop: `4px solid ${color}`
    })

    return (
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '30px' }}>

            {/* Gelir Kartı */}
            <div style={cardStyle('#28a745')}>
                <h3 style={{ margin: 0, color: '#555' }}>Toplam Gelir</h3>
                <p style={{ fontSize: '24px', fontWeight: 'bold', color: '#28a745', margin: '10px 0' }}>
                    {stats.toplam_gelir} TL
                </p>
            </div>

            {/* Gider Kartı */}
            <div style={cardStyle('#dc3545')}>
                <h3 style={{ margin: 0, color: '#555' }}>Toplam Gider</h3>
                <p style={{ fontSize: '24px', fontWeight: 'bold', color: '#dc3545', margin: '10px 0' }}>
                    {stats.toplam_gider} TL
                </p>
            </div>

            {/* Bakiye Kartı */}
            <div style={cardStyle('#007bff')}>
                <h3 style={{ margin: 0, color: '#555' }}>Kalan Bakiye</h3>
                <p style={{ fontSize: '24px', fontWeight: 'bold', color: '#007bff', margin: '10px 0' }}>
                    {stats.bakiye} TL
                </p>
            </div>

            {/* En Çok Harcanan Kartı */}
            <div style={cardStyle('#ffc107')}>
                <h3 style={{ margin: 0, color: '#555' }}>En Çok Harcanan</h3>
                <p style={{ fontSize: '18px', fontWeight: 'bold', color: '#d39e00', margin: '14px 0' }}>
                    {stats.en_cok_harcanan}
                </p>
            </div>

        </div>
    )
}

export default DashboardStats
