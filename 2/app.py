import streamlit as st
import sqlite3
import pandas as pd

# --- VERİTABANI BAĞLANTISI ---

# Streamlit uygulamanızın performansını artırmak için @st.cache_resource kullanılır.
# Bu, veritabanı bağlantısının Streamlit yeniden çalıştığında tekrar tekrar kurulmasını önler.
@st.cache_resource
def init_connection():
    """
    Veritabanına bir kez bağlanır ve bu bağlantıyı uygulama boyunca tekrar kullanır.
    check_same_thread=False, Streamlit'in birden fazla iş parçacığı kullanırken SQLite'a güvenli erişimini sağlar.
    """
    return sqlite3.connect('top250.db', check_same_thread=False)

# Veritabanı bağlantısını başlatıyoruz.
conn = init_connection()

# --- UYGULAMA BAŞLIĞI ---
st.title("🎬 Film Arşiv Paneli")
st.success("Veritabanı bağlantısı başarıyla kuruldu! Film bilgilerini çekmeye hazırız.")

# Buradan itibaren öğrenciler yeni kodlar yazacaklar.
