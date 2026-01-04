import { useState, useEffect } from 'react'

function SpendingChart({ refreshTrigger }) {
    const [imageUrl, setImageUrl] = useState(null)

    // Resim URL'ini state'te tutuyoruz
    // refreshTrigger değiştiğinde URL'in sonuna zaman damgası ekleyerek tarayıcıyı resmi yenilemeye zorluyoruz.
    useEffect(() => {
        setImageUrl(`http://localhost:8000/analysis/spending-pie?t=${Date.now()}`)
    }, [refreshTrigger])

    return (
        <div style={{ textAlign: 'center', margin: '30px 0' }}>
            <h3 style={{ color: '#555', marginBottom: '15px' }}>📊 Harcama Dağılımı</h3>

            {imageUrl && (
                <img
                    src={imageUrl}
                    alt="Harcama Grafiği"
                    style={{
                        maxWidth: '250px',
                        width: '100%',
                        height: 'auto',
                        borderRadius: '12px',
                        boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
                        border: '1px solid #eee'
                    }}
                />
            )}
        </div>
    )
}

export default SpendingChart
