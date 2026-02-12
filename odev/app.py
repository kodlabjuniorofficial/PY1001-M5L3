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

st.title("⭐ ÖDEV: Film Arama Çubuğu")
st.info("GÖREV: Yan menüye bir arama çubuğu ekleyerek filmleri başlığına göre arayın.")

# --- YAN MENÜ ---
st.sidebar.title("Arama Seçenekleri")

# GÖREV 1: st.sidebar.text_input kullanarak bir arama çubuğu oluşturun.
# Arama çubuğunun varsayılan değeri boş olsun.

# --- ANA SAYFA ---

# GÖREV 2: Eğer arama_metni boş değilse, bu metni içeren filmleri filtreleyen bir SQL sorgusu oluşturun.
# Arama yaparken 'name' sütununu kullandığınızdan emin olun ve büyük/küçük harf duyarlı olmamalıdır. (LOWER() fonksiyonunu kullanın.)
# Eğer arama metni boşsa tüm filmleri getirin.

# GÖREV 3: fetch_data fonksiyonu ile sonuçları alın ve bir DataFrame'e atayın.

# GÖREV 4: Sonuçları st.dataframe ile gösterin.
# Eğer sonuç yoksa uygun bir mesaj gösterin (Örn: "Film bulunamadı!").
