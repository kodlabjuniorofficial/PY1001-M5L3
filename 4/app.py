import streamlit as st
import sqlite3
import pandas as pd

@st.cache_resource
def init_connection():
    return sqlite3.connect('top250.db', check_same_thread=False)

conn = init_connection()

@st.cache_data(ttl=600)
def fetch_data(query, params=None):
    return pd.read_sql(query, conn, params=params)

st.title("🎬 Film Arşiv Paneli")
st.header("Aşama 4: Tür Filtresi")

st.info("Yan menüden film türü seçerek filmleri filtreleyin.", icon="➡️")

# --- YAN MENÜ ---
# GÖREV 1: st.sidebar kullanarak yan menüye "Filtreler" başlığını ekleyin.
# st.sidebar.header("KODU BURAYA YAZIN")

# GÖREV 2: Film türleri için sabit bir liste oluşturun. (Örnek: ["Tüm Türler", "Action", "Drama", "Crime", "Comedy"])
# genres = ["KODU BURAYA YAZIN"]

# GÖREV 3: st.sidebar.selectbox kullanarak yan menüde film türü seçimi için bir kutu oluşturun.
# Seçilen türü bir değişkene atayın (örneğin: selected_genre).
# selected_genre = st.sidebar.selectbox("KODU BURAYA YAZIN")

# --- ANA SAYFA ---
# GÖREV 4: Seçilen türe göre (veya 'Tüm Türler' seçilmişse tüm filmleri) filtreleyen bir SQL sorgusu oluşturun.
# Sorguyu yazarken 'top250' tablosunu ve film adları için 'name' sütununu kullandığınızdan emin olun.
# Eğer 'Tüm Türler' seçiliyse WHERE koşulu olmamalı. Diğer durumlarda WHERE genre = ? kullanın.
# query = "KODU BURAYA YAZIN"
# filtered_df = fetch_data(query, params=...)

# GÖREV 5: Filtrelenmiş DataFrame'i st.dataframe() ile ekrana basın.
# st.write(f"### Seçilen Tür: {selected_genre} ({len(filtered_df)} Film)")