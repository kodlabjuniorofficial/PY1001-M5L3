import streamlit as st
import sqlite3
import pandas as pd

@st.cache_resource
def init_connection():
    return sqlite3.connect('top250.db', check_same_thread=False)

conn = init_connection()

@st.cache_data(ttl=600)
def fetch_data(query, params=None):
    """Veritabanından veri çeker ve DataFrame olarak döndürür."""
    return pd.read_sql(query, conn, params=params)

st.title("🎬 Film Arşiv Paneli")
st.header("Aşama 3: Büyük Arşiv - Tüm Filmler")

st.info("""
Bu aşamada, veritabanımızdaki tüm filmleri çekip `st.dataframe` ile göstereceğiz.
`@st.cache_data` dekoratörü sayesinde verileri bir kez çekip tekrar tekrar veritabanına gitmiyoruz.
""", icon="📜")

# GÖREV 1: "top250" tablosundan tüm filmleri çeken bir SQL sorgusu tanımlayın.
# QUERY_ALL_MOVIES = "KODU BURAYA YAZIN"

# GÖREV 2: Tanımladığınız sorguyu kullanarak `fetch_data` fonksiyonu ile veriyi çekin
# ve bir DataFrame'e atayın (örneğin `df`).

# GÖREV 3: Elde ettiğiniz DataFrame'i `st.dataframe()` ile ekrana basın.
# st.success(f"Veritabanından toplam {len(df)} film başarıyla çekildi!")