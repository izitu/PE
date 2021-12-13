import wget

url = "https://audioknigi-online.site/audio/1/Umor-phantastika/Terry-Pratchet/Ploskiy-mir/Tvorcy-zaklinaniy/"
# 66.mp3
for it in range(1,67):
    print(f"{url}{it}.mp3")
    wget.download(f"{url}{it}.mp3", f"dwn/{it}.mp3")