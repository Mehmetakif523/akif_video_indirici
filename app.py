import streamlit as st
import yt_dlp
import os

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Kanka İndirici v5", page_icon="🎬")

st.title("🎬 Akif Video İndirme Merkezi")
st.info("YouTube ve Instagram bazen engelleme yapabilir. Hata alırsanız linki tekrar deneyin.")

link = st.text_input("Video Linkini Yapıştır:")

if st.button("VİDEOYU HAZIRLA"):
    if link:
        with st.spinner('Video dosyaları yakalanıyor...'):
            try:
                # Bot engelini aşmak için profesyonel ayarlar
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'indirilen_video.mp4',
                    'noplaylist': True,
                    'quiet': True,
                    'no_check_certificate': True,
                    # YouTube ve Instagram'ı kandırmak için tarayıcı taklidi:
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'referer': 'https://www.google.com/',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                
                with open("indirilen_video.mp4", "rb") as file:
                    st.success("Video başarıyla hazırlandı!")
                    st.video(file)
                    st.download_button(
                        label="📥 TELEFONA KAYDET",
                        data=file,
                        file_name="kanka_video.mp4",
                        mime="video/mp4"
                    )
                
                # Geçici dosyayı temizle
                os.remove("indirilen_video.mp4")
                
            except Exception as e:
                # Hata türüne göre kullanıcıya mesaj ver
                if "403" in str(e):
                    st.error("Hata: YouTube sunucuyu engelledi. 5 dakika sonra tekrar dene kanka.")
                elif "login required" in str(e).lower():
                    st.error("Hata: Instagram bu video için giriş istiyor. Gizli hesapları indiremem kanka.")
                else:
                    st.error(f"Bir sorun çıktı: {e}")
    else:
        st.warning("Önce link yapıştır kanka!")
