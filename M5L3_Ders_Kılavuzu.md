# 🎬 Modül 5, Ders 3: Sinema Analiz Paneli (Sadeleştirilmiş)

**Hoş Geldiniz!** Bu derste, Streamlit'in gücünü temel SQL veritabanı etkileşimleriyle birleştirerek interaktif bir film analiz paneli oluşturacağız. Modül 4'te öğrendiğimiz `top250.db` veritabanını bir web arayüzü üzerinden "kumanda etmeyi" öğreneceğiz!

---

### 🎯 Dersin Hedefleri

1.  **Veritabanı Entegrasyonu:** `sqlite3` kütüphanesini Streamlit ile konuşturmak ve bağlantıyı verimli bir şekilde yönetmek.
2.  **Veri Görselleştirme (Tablo):** Veritabanındaki verileri `st.dataframe` ile interaktif, sıralanabilir ve aranabilir bir tabloda göstermek.
3.  **Dinamik Filtreleme:** Kullanıcı seçimlerine göre (Sidebar) basit SQL sorgularını dinamik olarak çalıştırmak.
4.  **Kullanıcı Etkileşimi:** Temel `st.text_input` ve `st.selectbox` gibi Streamlit bileşenlerini kullanarak kullanıcıdan girdi almak.

---

### 🧩 ADIM ADIM İŞLEYİŞ VE NOTLAR

#### 1. Aşama: Veri Dedektifliğine Giriş (15 Dakika) - SADECE ANLATIM

Bu aşama, öğrencilerin veritabanı ve web arayüzü arasındaki temel farkı kavraması için ayrılmıştır. Kodlama yapılmayacak, yalnızca kavramsal bir giriş sağlanacaktır.

*   **Konsept:** "Kasadaki Dosyaları Vitrine Çıkarma"
*   **Recap (Öğretmen Notu):** Öğrencilere Modül 4'teki SQL bilgilerini hatırlatın: "Modül 4 boyunca SQLite ile verilerimizi bir dosyaya (.db) kaydetmeyi öğrendik. Ama bu verilere bakmak için hep kod yazmamız gerekiyordu."
*   **Vizyon (Öğretmen Notu):** "Bugün bu verileri, bir web sitesi üzerinden, sanki bir kumanda kullanıyormuş gibi filtreleyip inceleyeceğiz. Artık veritabanı uzmanı olmayan biri bile sizin yaptığınız bu paneli kullanarak en iyi filmleri bulabilecek."
*   **Kazanım:** Veritabanı (veri deposu) ve Web Arayüzü (vitrin) arasındaki farkı kavrar.
*   **Aksiyon:** Bu aşama kod içermemektedir. Öğrenciler sadece konsepti dinleyecek ve tartışmaya katılacaklardır.

---

#### 2. Aşama: Tesisatın Kurulması (Bağlantı) (15 Dakika)

Bu aşamada, Python kodumuz ile `top250.db` veritabanı arasına köprü kuracağız. Bu köprü, Streamlit uygulamamızın verilere erişmesini sağlayacak ilk adımdır.

*   **Konsept:** Python ile Veritabanı arasına köprü kurma.
*   **Öğretmen Notu:** `@st.cache_resource` komutuna özellikle değinin: "Sitemiz her saniye veritabanına gidip yorulmasın, bağlantıyı bir kez kursun ve aklında tutsun." Bu, uygulamanın performansını artırır ve gereksiz kaynak kullanımını önler.
*   **Aksiyon:** `M5L3/2/app.py` dosyasını açın ve aşağıdaki taslak kod ile veritabanı bağlantısını kurun. Bu aşamada kod hazır olarak verilmiştir.

-   **Kod (`M5L3/2/app.py`):**
    ```python
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
    ```

---

#### 3. Aşama: Büyük Arşiv (Tüm Filmleri Listeleme) (20 Dakika)

Artık veritabanı bağlantımız hazır olduğuna göre, tüm film arşivini Streamlit uygulamamızda interaktif bir tablo olarak görüntüleyeceğiz.

*   **Konsept:** "SELECT * FROM top250" komutunu web sitesine dökme.
*   **Öğrenci Görevi:** `pd.read_sql` kullanarak "top250" tablosundaki tüm verileri çekin ve `st.dataframe` ile sayfaya basın.
*   **Eğlence (Öğretmen Notu):** Tablonun başlıklarına tıklayarak filmleri puana göre (rating) büyükten küçüğe sıralatın. "Bakın, SQL'deki ORDER BY'ı Streamlit bizim yerimize otomatik yapıyor!" diyerek öğrencilerin heyecanını artırın. Bu, `st.dataframe`'in etkileşimli özelliklerini vurgular.
*   **Aksiyon:** `M5L3/3/app.py` dosyasını açın ve aşağıdaki taslak kod ile tüm filmleri listeleyin.

-   **Taslak Kod (`M5L3/3/app.py`):**
    ```python
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
    # Film adları için 'name' sütununu kullanın.
    # QUERY_ALL_MOVIES = "KODU BURAYA YAZIN"
    # GÖREV 2: Tanımladığınız sorguyu kullanarak `fetch_data` fonksiyonu ile veriyi çekin
    # ve bir DataFrame'e atayın (örneğin `df`).

    # GÖREV 3: Elde ettiğiniz DataFrame'i `st.dataframe()` ile ekrana basın.
    # st.success(f"Veritabanından toplam {len(df)} film başarıyla çekildi!")
    ```

-   **Çözüm Kodu (`M5L3/3/app.py` - Öğretmen Referansı İçin):**
    ```python
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

    QUERY_ALL_MOVIES = "SELECT name, genre, year, rating FROM top250"

    df = fetch_data(QUERY_ALL_MOVIES)

    st.dataframe(df, use_container_width=True)
    st.success(f"Veritabanından toplam {len(df)} film başarıyla çekildi!")
    ```

---

#### 4. Aşama: Tür Filtresi (Sidebar Sorgusu) (25 Dakika)

Şimdi film arşivimizi daha kullanışlı hale getireceğiz! Yan menüye bir açılır kutu (`st.selectbox`) ekleyerek, kullanıcıların filmleri türüne göre filtrelemesini sağlayacağız.

*   **Konsept:** Yan menüden film türü seçip listeyi güncelleme.
*   **Öğrenci Görevi:** `st.sidebar` kullanarak yan menüye bir `st.selectbox` ekleyin. İçine veritabanından çektiğiniz eşsiz türleri (`DISTINCT genre`) ve en başta "Tüm Türler" seçeneğini koyun.
*   **Dinamik Sorgu:** Seçilen türe göre SQL sorgusunu (`SELECT * FROM top250 WHERE genre = ?`) güncelleyip `st.dataframe`'i anında yenileyin. Bu, en güvenli yöntem olan **parametreli sorgu** ile yapılmalıdır.
*   **Vay Be Anı (Öğretmen Notu):** Kullanıcı türü seçtiği an tablonun anında değişmesini (Streamlit'in "Rerun" mantığı) öğrencilere gösterin. Bu, web uygulamalarının etkileşimli doğasını vurgular.
*   **Aksiyon:** `M5L3/4/app.py` dosyasını açın ve aşağıdaki taslak kod ile tür filtresini uygulayın.

-   **Taslak Kod (`M5L3/4/app.py`):**
    ```python
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

    # --- YAN MENÜ ---
    st.sidebar.header("Filtreler")

    # GÖREV 1: Veritabanından eşsiz (distinct) film türlerini çeken bir fonksiyon yazın.
    # @st.cache_data kullanmayı unutmayın!
    # def get_distinct_genres():
    #     query = "SELECT DISTINCT genre FROM top250 ORDER BY genre"
    #     genres_df = fetch_data(query)
    #     return ["Tüm Türler"] + genres_df['genre'].tolist()

    # genres = get_distinct_genres()
    # selected_genre = st.sidebar.selectbox("Film Türü Seçin", genres)


    # --- ANA SAYFA ---
    # GÖREV 2: Seçilen türe göre filmleri filtreleyin.
    # 'Tüm Türler' seçilirse, tüm filmleri gösteren sorguyu çalıştırın.
    # Diğer durumlarda, SADECE seçilen türü getiren GÜVENLİ (parametreli) bir sorgu kullanın.
    #
    # if selected_genre == "Tüm Türler":
    #     query = "SELECT name, genre, year, rating FROM top250"
    #     filtered_df = fetch_data(query)
    # else:
    #     # GÜVENLİ YÖNTEM: SQL Injection'a karşı korumalıdır.
    #     query = "SELECT name, genre, year, rating FROM top250 WHERE genre = ?"
    #     # `params` olarak tek elemanlı bir tuple göndermeyi unutmayın: (selected_genre,)
    #     filtered_df = fetch_data(query, params=(KODU_BURAYA_YAZIN))

    # st.write(f"### Seçilen Tür: {selected_genre} ({len(filtered_df)} Film)")
    # st.dataframe(filtered_df, use_container_width=True)
    ```

-   **Çözüm Kodu (`M5L3/4/app.py` - Öğretmen Referansı İçin):**
    ```python
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

    # Veritabanından eşsiz türleri çeken ve önbelleğe alan fonksiyon
    @st.cache_data
    def get_distinct_genres():
        query = "SELECT DISTINCT genre FROM top250 ORDER BY genre"
        genres_df = fetch_data(query)
        # Liste başına "Tüm Türler" seçeneğini ekliyoruz.
        return ["Tüm Türler"] + genres_df['genre'].tolist()

    st.title("🎬 Film Arşiv Paneli")
    st.header("Aşama 4: Tür Filtresi")
    st.info("Yan menüden film türü seçerek filmleri dinamik olarak filtreleyin.", icon="➡️")

    # --- YAN MENÜ ---
    st.sidebar.header("Filtreler")
    
    genres = get_distinct_genres()
    selected_genre = st.sidebar.selectbox("Film Türü Seçin", genres)

    # --- ANA SAYFA ---
    if selected_genre == "Tüm Türler":
        st.write(f"### Tüm Filmler ({len(fetch_data('SELECT * FROM top250'))} Film)")
        query = "SELECT name, genre, year, rating FROM top250"
        filtered_df = fetch_data(query)
    else:
        st.write(f"### Tür: {selected_genre}")
        # GÜVENLİ YÖNTEM: SQL Injection'ı önlemek için sorgu parametre ile çalıştırılır.
        query = "SELECT name, genre, year, rating FROM top250 WHERE genre = ?"
        filtered_df = fetch_data(query, params=(selected_genre,))

    st.dataframe(filtered_df, use_container_width=True)
    st.success(f"'{selected_genre}' kategorisinde {len(filtered_df)} film listelendi.")
    ```

---

#### 5. Aşama: Analiz ve Grafikler (`st.bar_chart`) (20 Dakika)

Tablolar harikadır, ancak bazen bir resim binlerce satırdan daha fazlasını anlatır. Şimdi verilerimizi görselleştirmek için basit bir çubuk grafik ekleyeceğiz.

*   **Konsept:** Veriyi Konuşan Grafiğe Dönüştürme.
*   **Öğrenci Görevi:** "Yıllara Göre Film Sayısı"nı gösteren bir `st.bar_chart` oluşturun.
*   **SQL Yeteneği:** Bu görev için `GROUP BY` kullanarak verileri gruplamamız gerekecek. Bu, SQL'in en güçlü özelliklerinden biridir ve burada çok basit bir kullanımını göreceğiz.
*   **Aksiyon:** Önceki aşamanın kodlarını `M5L3/5/app.py` adlı yeni bir dosyaya kopyalayın ve aşağıdaki taslak kod ile bir grafik ekleyin.

-   **Taslak Kod (`M5L3/5/app.py`):**
    ```python
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

    # Veritabanından eşsiz türleri çeken ve önbelleğe alan fonksiyon
    @st.cache_data
    def get_distinct_genres():
        query = "SELECT DISTINCT genre FROM top250 ORDER BY genre"
        genres_df = fetch_data(query)
        # Liste başına "Tüm Türler" seçeneğini ekliyoruz.
        return ["Tüm Türler"] + genres_df['genre'].tolist()

    st.title("🎬 Film Arşiv Paneli")

    # --- YAN MENÜ (SIDEBAR) ---
    st.sidebar.header("Filtreler")
    
    genres = get_distinct_genres()
    selected_genre = st.sidebar.selectbox("Film Türü Seçin", genres)

    # --- ANA SAYFA ---
    # Filtreleme mantığı
    if selected_genre == "Tüm Türler":
        st.header("Tüm Filmler")
        query = "SELECT name, genre, year, rating FROM top250"
        filtered_df = fetch_data(query)
    else:
        st.header(f"Tür: {selected_genre}")
        query = "SELECT name, genre, year, rating FROM top250 WHERE genre = ?"
        filtered_df = fetch_data(query, params=(selected_genre,))

    st.dataframe(filtered_df, use_container_width=True)
    st.success(f"'{selected_genre}' kategorisinde {len(filtered_df)} film listelendi.")

    # --- GRAFİK BÖLÜMÜ ---
    st.header("Aşama 5: Yıllara Göre Film Sayısı")
    st.info("Bu bölümde, `GROUP BY` kullanarak veritabanından toplu veri çekecek ve bir çubuk grafik ile göstereceğiz.", icon="📊")

    # GÖREV 1: Yıllara göre film sayılarını getiren bir SQL sorgusu yazın.
    # Sorgu: "SELECT year, COUNT(name) as film_sayisi FROM top250 GROUP BY year ORDER BY year"
    # GRAFIK_QUERY = "KODU BURAYA YAZIN"
    # chart_df = fetch_data(GRAFIK_QUERY)

    # GÖREV 2: Gelen DataFrame'i st.bar_chart'a uygun hale getirin.
    # st.bar_chart, x ekseni için DataFrame'in indeksini kullanır.
    # Bu yüzden 'year' sütununu indeks yapmalısınız: chart_df.set_index('year')
    # st.write("#### Yıllara Göre Film Sayısı Grafiği")
    # st.bar_chart(KODU BURAYA YAZIN)
    ```

-   **Çözüm Kodu (`M5L3/5/app.py` - Öğretmen Referansı İçin):**
    ```python
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

    # Veritabanından eşsiz türleri çeken ve önbelleğe alan fonksiyon
    @st.cache_data
    def get_distinct_genres():
        query = "SELECT DISTINCT genre FROM top250 ORDER BY genre"
        genres_df = fetch_data(query)
        # Liste başına "Tüm Türler" seçeneğini ekliyoruz.
        return ["Tüm Türler"] + genres_df['genre'].tolist()

    st.title("🎬 Film Arşiv Paneli")

    # --- YAN MENÜ (SIDEBAR) ---
    st.sidebar.header("Filtreler")
    
    genres = get_distinct_genres()
    selected_genre = st.sidebar.selectbox("Film Türü Seçin", genres)

    # --- ANA SAYFA ---
    # Filtreleme mantığı
    if selected_genre == "Tüm Türler":
        st.header("Tüm Filmler")
        query = "SELECT name, genre, year, rating FROM top250"
        filtered_df = fetch_data(query)
    else:
        st.header(f"Tür: {selected_genre}")
        query = "SELECT name, genre, year, rating FROM top250 WHERE genre = ?"
        filtered_df = fetch_data(query, params=(selected_genre,))

    st.dataframe(filtered_df, use_container_width=True)
    st.success(f"'{selected_genre}' kategorisinde {len(filtered_df)} film listelendi.")
    
    # --- GRAFİK BÖLÜMÜ ---
    st.header("Yıllara Göre Film Sayısı")
    st.info("Bu bölümde, `GROUP BY` kullanarak veritabanından toplu veri çekecek ve bir çubuk grafik ile göstereceğiz.", icon="📊")

    GRAFIK_QUERY = "SELECT year, COUNT(name) as film_sayisi FROM top250 GROUP BY year ORDER BY year"
    chart_df = fetch_data(GRAFIK_QUERY)

    st.write("#### Yıllara Göre Film Sayısı Grafiği")

    # AÇIKLAMA: st.bar_chart, x-ekseni olarak DataFrame'in indeksini kullanır.
    # Bu nedenle, 'year' sütununu grafiğin x-ekseni yapmak için onu indeks olarak ayarlıyoruz.
    st.bar_chart(chart_df.set_index('year'))

    st.success("Grafik başarıyla oluşturuldu!")
    ```

---

#### 6. Aşama: Kapanış ve "Bul Bakalım" Ödevi (15 Dakika)

Bu son aşamada, ders boyunca öğrendiklerimizi özetleyecek ve yeni bir meydan okuma ile öğrencileri baş başa bırakacağız: Bir arama çubuğu eklemek!

*   **Konsept:** Değerlendirme ve vizyon.
*   **Özet (Öğretmen Notu):** "Bugün veritabanımızı bir web sitesine bağladık. Artık filtreleme yapabilen interaktif bir panelimiz var! Sadece birkaç satır Python koduyla ne kadar güçlü web uygulamaları yapabileceğimizi gördük."
*   **Değerlendirme (Öğretmen Notu):** "Tür filtresi butonuna bastığımızda veya bir tür seçtiğimizde SQL sorgumuzda ne değişiyor?" (Cevap: `WHERE` şartı ekleniyor/değişiyor). Öğrencilerin bu dinamik yapıyı kavradığından emin olun.
*   **Ödev:** "Arama Kutusu Ekleyelim". Kullanıcı bir harf yazdığında o harfle başlayan veya içinde o harfi/kelimeyi içeren filmleri getiren bir `st.text_input` ekleme görevi.
*   **Öğretmen Notu (Ödev):** Bu ödevde `LIKE` sorgusunun nasıl kullanılacağını hatırlatın. "SQL'de `LIKE` operatörü ile metin araması yapıyorduk, hatırlıyor musunuz? Özellikle `LOWER()` fonksiyonu ile büyük/küçük harf duyarlılığını nasıl ortadan kaldırıyorduk?"
*   **Aksiyon:** `M5L3/odev/app.py` dosyasını açın ve ödev görevlerini tamamlayın.

-   **Ödev Taslak Kod (`M5L3/odev/app.py`):**
    ```python
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
    arama_metni = st.sidebar.text_input("Film Başlığı Ara:", "")

    # --- ANA SAYFA ---

    # GÖREV 2: Eğer arama_metni boş değilse, bu metni içeren filmleri filtreleyen bir SQL sorgusu oluşturun.
    # Arama büyük/küçük harf duyarlı olmamalıdır. (LOWER() fonksiyonunu kullanın.)
    # GÜVENLİ YÖNTEM: "SELECT name, genre, year, rating FROM top250 WHERE LOWER(name) LIKE ?"
    # Parametre: ('%' + arama_metni.lower() + '%',)
    # Eğer arama metni boşsa tüm filmleri getirin.
    #
    # if arama_metni:
    #     query = "KODU BURAYA YAZIN"
    #     params = (KODU BURAYA YAZIN,)
    #     result_df = fetch_data(query, params=params)
    # else:
    #     query = "KODU BURAYA YAZIN"
    #     result_df = fetch_data(query)


    # GÖREV 3: Sonuçları st.dataframe ile gösterin.
    # if not result_df.empty:
    #    st.dataframe(result_df, use_container_width=True)
    # else:
    #    st.warning("Film bulunamadı!")
    ```

-   **Ödev Çözüm Kod (`M5L3/odev/app.py` - Öğretmen Referansı İçin):**
    ```python
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

    st.title("⭐ ÖDEV ÇÖZÜMÜ: Film Arama Çubuğu")

    # --- YAN MENÜ ---
    st.sidebar.title("Arama Seçenekleri")

    arama_metni = st.sidebar.text_input("Film Başlığı Ara:", "")

    # --- ANA SAYFA ---

    if arama_metni:
        st.subheader(f"'{arama_metni}' için Arama Sonuçları")
        # GÜVENLİ YÖNTEM: LIKE sorgusu da parametre ile çalıştırılmalıdır.
        query = "SELECT name, genre, year, rating FROM top250 WHERE LOWER(name) LIKE ?"
        params = ('%' + arama_metni.lower() + '%',)
        result_df = fetch_data(query, params=params)
    else:
        st.subheader("Tüm Filmler")
        query = "SELECT name, genre, year, rating FROM top250"
        result_df = fetch_data(query)

    if not result_df.empty:
        st.dataframe(result_df, use_container_width=True)
        st.success(f"Toplam {len(result_df)} film bulundu.")
    else:
        st.warning(f"'{arama_metni}' başlığına sahip film bulunamadı!")
    ```

---

### Sonraki Ders Konusu

"Bugün veritabanımızı bir web sitesine bağladık ve basit filtrelemeler yapabildik! Gelecek dersimizde, kullanıcıdan daha karmaşık girdiler alacak, formları yönetecek ve belki de veritabanına veri ekleme gibi CRUD (Create, Read, Update, Delete) operasyonlarına giriş yapacağız."

---

### Ek Notlar:

*   **Kod Yükü Az:** Karmaşık Pandas gruplamaları veya `GROUP BY` gibi ileri SQL/Pandas işlemleri şimdilik yok. Sadece bildikleri `SELECT` ve `WHERE` var.
*   **Odak Noktası Net:** Öğrenci "nasıl arayüz yapılır" ve "veri oraya nasıl gelir" konusuna odaklanıyor.
*   **Başarı Hissi Yüksek:** Ders sonunda 250 filmlik dev bir arşivi kumanda edebilen çalışan bir web sitesi ellerinde kalıyor.