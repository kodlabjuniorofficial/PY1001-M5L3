import streamlit as st
import sqlite3
import pandas as pd

# --- VERİTABANI İŞLEMLERİ ---

# NOT: Bu dosya, ödevin tamamlanmış halini içerir.

@st.cache_resource
def init_connection():
    """Veritabanına bağlanır."""
    return sqlite3.connect('top250.db', check_same_thread=False)

conn = init_connection()

@st.cache_data(ttl=600)
def fetch_data(query, params=None):
    """Veritabanından parametreli sorgu ile veri çeker."""
    return pd.read_sql(query, conn, params=params)

# --- ÖDEV ÇÖZÜMÜ ---
st.title("⭐ ÖDEV ÇÖZÜMÜ: Yıla Göre Film Filtreleme")

st.info("Bu sayfa, ödevin doğru yapılmış halini göstermektedir.")

# GÖREV 1: En eski ve en yeni yılı bulun.
try:
    year_range_df = fetch_data("SELECT MIN(year) AS min_year, MAX(year) AS max_year FROM movies")
    min_year = int(year_range_df['min_year'][0])
    max_year = int(year_range_df['max_year'][0])

    # GÖREV 2: Yıl seçimi için bir slider oluşturun.
    selected_year = st.slider(
        "Filmleri yıla göre filtrelemek için bir yıl seçin:",
        min_value=min_year,
        max_value=max_year,
        value=min_year  # Varsayılan olarak en eski yılı göster
    )

    st.subheader(f"📅 {selected_year} Yılında Çekilen Filmler")

    # GÖREV 3 & 4: Seçilen yıla göre filmleri sorgulayın ve gösterin.
    query = "SELECT title, genre, rating FROM movies WHERE year = ?"
    params = (selected_year,)
    result_df = fetch_data(query, params=params)

    # GÖREV 5: Film yoksa mesaj gösterin.
    if result_df.empty:
        st.warning(f"{selected_year} yılında listemizde kayıtlı bir film bulunamadı.")
    else:
        st.dataframe(result_df, use_container_width=True)
        st.success(f"{selected_year} yılına ait {len(result_df)} film bulundu.")

except Exception as e:
    st.error(f"Veriler yüklenirken bir hata oluştu: {e}")
