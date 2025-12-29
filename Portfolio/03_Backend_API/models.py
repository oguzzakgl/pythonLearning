from sqlalchemy import Column, Integer, String, Float
from database import Base

# VERİTABANI TABLO MODELİ (SQLAlchemy)
# Burada veritabanında oluşacak tabloları Python sınıfı olarak tanımlıyoruz.

class Product(Base):
    # __tablename__ = "products"
    
    # Sütunlar:
    # id (Integer, Primary Key)
    # name (String)
    # price (Float)
    # stock (Integer)
    pass
