import streamlit as st
import yt_dlp
import os

# 1. Sayfanın en üstünde görünecek başlıklar
st.set_page_config(page_title="Kanka İndirici", page_icon="🚀")
st.title("🚀 Kanka Video İndirme")
st.write("Linkini yapıştır ve videonu hemen al!")

# 2. Kalite seçme kutusu (4K'ya kadar)
kalite_secimi = st.selectbox("Maksimum Kalite Ne Olsun?", ["4K (2160p)", "1080p", "720p", "En İyi"])

# 3. Linki yapıştıracağın kutu
link = st.text_input("YouTube, Instagram veya TikTok linki:")

# 4. "İndir" butonuna basınca ne olacak?
if st.button("VİDEOYU HAZIRLA"):
    if link:
        with st.spinner('Kanka senin için videoyu yakalıyorum, bekle...'):
            try:
                # Kalite ayarını belirleyelim
                k_map = {
                    "4K (2160p)": "bestvideo[height<=2160]+bestaudio/best",
                    "1080p": "bestvideo[height<=1080]+bestaudio/best",
                    "720p": "bestvideo[height<=720]+bestaudio/best",
                    "En İyi": "best"
                }
                
                ydl_opts = {
                    'format': k_map.get(kalite_secimi),
                    'outtmpl': 'kanka_video.mp4', # Geçici dosya adı
                    'merge_output_format': 'mp4',
                    'noplaylist': True,
                }
                
                # Videoyu önce sunucuya indiriyoruz
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                
                # 5. İndirme bittiğinde ekranda videoyu ve "Kaydet" butonunu göster
                with open("kanka_video.mp4", "rb") as file:
                    st.success("Video hazır! Aşağıdan izleyebilir veya indirebilirsin.")
                    st.video(file) # Telefonunda izleyebilmen için
                    st.download_button(
                        label="TELEFONA KAYDET",
                        data=file,
                        file_name="indirilen_video.mp4",
                        mime="video/mp4"
                    )
                
                # Temizlik (Sunucuda yer kaplamasın)
                os.remove("kanka_video.mp4")
                
            except Exception as e:
                st.error(f"Eyvah! Bir hata oldu kanka: {e}")
    else:
        st.warning("Kanka linki yapıştırmadan işlem yapamam.")