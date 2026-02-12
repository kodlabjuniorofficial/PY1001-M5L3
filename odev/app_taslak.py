import streamlit as st
import sqlite3
import pandas as pd

# --- VERİTABANI İŞLEMLERİ ---

# NOT: Bu bir taslak dosyasıdır. Öğrencilerin görevi tamamlaması beklenir.

@st.cache_resource
def init_connection():
    """Veritabanına bağlanır."""
    return sqlite3.connect('top250.db', check_same_thread=False)

conn = init_connection()

@st.cache_data(ttl=600)
def fetch_data(query, params=None):
    """Veritabanından parametreli sorgu ile veri çeker."""
    return pd.read_sql(query, conn, params=params)

# --- ÖDEV ---
st.title("⭐ ÖDEV: Yıla Göre Film Filtreleme")

st.info("""
**GÖREVİNİZ:**

1.  Veritabanındaki en eski ve en yeni film yıllarını bulun.
2.  Bu iki yıl arasında seçim yapmayı sağlayan bir `st.slider` oluşturun.
3.  Kullanıcı slider'ı hareket ettirdiğinde, seçilen yılda çekilmiş filmleri
    SQL sorgusu ile veritabanından alın.
4.  Sonuçları `st.dataframe` ile ekranda gösterin.
5.  Eğer o yıl hiç film yoksa, "Bu yılda film bulunamadı." gibi bir mesaj gösterin.
""")

# GÖREV 1: En eski ve en yeni yılı bulun.
# İPUCU: `SELECT MIN(year), MAX(year) FROM movies`
# year_range = fetch_data(...)
# min_year = ...
# max_year = ...


# GÖREV 2: Yıl seçimi için bir slider oluşturun.
# selected_year = st.slider(...)


# GÖREV 3 & 4: Seçilen yıla göre filmleri sorgulayın ve gösterin.
# query = "..."
# params = (...)
# result_df = fetch_data(query, params=params)
# st.dataframe(result_df)

# GÖREV 5: Film yoksa mesaj gösterin.
# if result_df.empty:
#    st.warning(...)

# --- KODU AŞAĞIYA YAZIN ---
