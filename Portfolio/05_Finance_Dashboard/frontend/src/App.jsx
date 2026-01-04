import { useState, useEffect } from 'react'
import './App.css'
import TransactionList from './components/TransactionList'
import TransactionForm from './components/TransactionForm'
import DashboardStats from './components/DashboardStats'
import SpendingChart from './components/SpendingChart'

function App() {
  // Liste güncellemelerini tetiklemek için kullanılan sayaç state'i
  const [refreshKey, setRefreshKey] = useState(0)

  // Listeyi yenileme fonksiyonu (Child bileşenlerden çağrılır)
  const handleRefresh = () => {
    setRefreshKey(oldKey => oldKey + 1)
  }

  // Kartlar için ortak stil (Eşit yükseklik ve modern görünüm için)
  const cardStyle = {
    backgroundColor: '#1e1e1e', // Arkaya hafif koyu bir fon (Kart hissi)
    borderRadius: '12px',
    padding: '20px',
    height: '100%', // Kapsayıcının tüm yüksekliğini kapla
    boxSizing: 'border-box',
    border: '1px solid #333'
  }

  return (
    <div className="container">
      <h1>💰 Finans Takip Sistemi</h1>

      {/* İstatistik Kartları */}
      <DashboardStats refreshTrigger={refreshKey} />

      {/* Ana İçerik: Form ve Grafik */}
      <div style={{ display: 'flex', gap: '20px', alignItems: 'stretch', justifyContent: 'space-between', marginBottom: '40px' }}>

        {/* SOL: İşlem Ekleme Formu */}
        <div style={{ flex: 2 }}>
          <div style={cardStyle}>
            <h3 style={{ marginTop: 0, marginBottom: '20px' }}>➕ Yeni İşlem Ekle</h3>
            <TransactionForm onAdd={handleRefresh} />
          </div>
        </div>

        {/* SAĞ: Harcama Grafiği */}
        <div style={{ flex: 1 }}>
          <div style={{ ...cardStyle, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
            <h3 style={{ marginTop: 0, marginBottom: '20px' }}>📊 Harcama Dağılımı</h3>
            <SpendingChart refreshTrigger={refreshKey} />
          </div>
        </div>

      </div>

      <hr style={{ margin: '20px 0', borderColor: '#444' }} />

      {/* İşlem Listesi */}
      <TransactionList refreshTrigger={refreshKey} onDelete={handleRefresh} />
    </div>
  )
}

export default App
