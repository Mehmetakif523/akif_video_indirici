import streamlit as st
import yt_dlp
import os

# Sayfa Başlığı
st.set_page_config(page_title="Akif Pro Video Downloader", page_icon="🎬")

st.title("🎬 Akif Video İndirme Merkezi")
st.markdown("---")

# Kalite Seçimi (Senin istediğin o özellik)
kalite = st.selectbox(
    "Görüntü Kalitesi Seçin:",
    ("4K (2160p)", "2K (1440p)", "1080p", "720p", "En İyi")
)

link = st.text_input("YouTube veya Instagram Linkini Yapıştırın:", placeholder="https://...")

if st.button("VİDEOYU HAZIRLA"):
    if not link:
        st.warning("Kanka önce bir link yapıştırman lazım!")
    else:
        with st.spinner('Kanka video işleniyor, YouTube ile pazarlık yapıyorum...'):
            try:
                # Kalite kodlarını ayarlayalım
                format_map = {
                    "4K (2160p)": "bestvideo[height<=2160]+bestaudio/best",
                    "2K (1440p)": "bestvideo[height<=1440]+bestaudio/best",
                    "1080p": "bestvideo[height<=1080]+bestaudio/best",
                    "720p": "bestvideo[height<=720]+bestaudio/best",
                    "En İyi": "best"
                }

                ydl_opts = {
                    'format': format_map[kalite],
                    'outtmpl': 'kanka_video.%(ext)s',
                    'noplaylist': True,
                    'no_check_certificate': True,
                    # Bot engelini aşmak için kritik ayarlar:
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'referer': 'https://www.google.com/',
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=True)
                    video_filename = ydl.prepare_filename(info)

                # Videoyu kullanıcıya sun
                with open(video_filename, "rb") as file:
                    st.success(f"Başardık! Video {kalite} kalitesinde hazır.")
                    st.video(file)
                    st.download_button(
                        label="📥 TELEFONA KAYDET",
                        data=file,
                        file_name=f"akif_video.mp4",
                        mime="video/mp4"
                    )
                
                # Temizlik
                os.remove(video_filename)

            except Exception as e:
                st.error(f"Eyvah! Bir hata oldu kanka: {str(e)}")
                st.info("İpucu: Eğer 403 hatası alırsan, birkaç dakika sonra tekrar dene. YouTube bazen IP engeller.")

st.markdown("---")
st.caption("Merkez Fırın Gururla Sunar 🥖")
