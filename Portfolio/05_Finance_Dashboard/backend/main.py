from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
import database
import analytics
import visuals

app = FastAPI()

# CORS Ayarları
# Frontend (React) ve Backend arasındaki port farkından doğan güvenlik engelini kaldırır.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.on_event("startup")
def startup_event():
    database.init_db()

class Transaction(BaseModel):
    kullanici_id: int
    baslik: str
    miktar: float
    tip: str 
    tarih: str

@app.post("/transactions")
def create_transaction(islem: Transaction):
    database.add_transaction(
        islem.kullanici_id,
        islem.baslik,
        islem.miktar,
        islem.tip,
        islem.tarih
    )
    return {"message": "İşlem başarıyla eklendi."}

@app.delete("/transactions/{id}")
def delete_transaction(id: int):
    database.delete_transaction(id)
    return {"message": "İşlem başarıyla silindi."}

@app.get("/")
def read_root():
    return {"mesaj": "Finans Takip Sistemi Çalışıyor!"}

@app.get("/transactions/{kullanici_id}")
def read_transactions(kullanici_id: int):
    transactions = database.get_transactions(kullanici_id)
    return {"transactions": transactions}

@app.get("/analysis/spending-pie")
def get_spending_pie_chart():
    """
    Harcamaların kategori bazlı dağılımını analiz eder ve
    sonucu bir pasta grafiği (PNG) olarak döndürür.
    """
    df = analytics.get_data_as_dataframe()
    summary_df = analytics.analyze_spending_by_category(df)
    visuals.create_spending_pie_chart(summary_df)
    return FileResponse("spending_pie.png")

@app.get("/analysis/summary")
def get_summary_stats():
    """
    Dashboard için genel özet istatistiklerini (Gelir, Gider, Bakiye, En Çok Harcanan) hesaplar.
    """
    df = analytics.get_data_as_dataframe()
    stats = analytics.calculate_summary_stats(df)
    return stats