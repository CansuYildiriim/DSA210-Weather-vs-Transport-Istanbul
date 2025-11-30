import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://ulasav.csb.gov.tr/dataset/34-hourly-public-transport-data-set"

SAVE_DIR = "data/transport"
os.makedirs(SAVE_DIR, exist_ok=True)

# Headless Chrome ayarları
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("🚀 Chrome başlatılıyor...")

# Yeni Selenium yöntemi — HATA ÇÖZÜLDÜ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print("🌐 Sayfaya gidiliyor...")
driver.get(BASE_URL)
time.sleep(3)

print("🔍 CSV linkleri aranıyor...")
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

links = soup.find_all("a")
download_links = []

for a in links:
    href = a.get("href", "")
    if "download" in href and href.endswith(".csv"):
        if href.startswith("/"):
            href = "https://ulasav.csb.gov.tr" + href
        download_links.append(href)

# Sadece 2024 yılı
download_links = [l for l in download_links if "2024" in l]

print(f"📌 Bulunan CSV sayısı: {len(download_links)}")

# Dosyaları indir
for link in download_links:
    filename = link.split("/")[-1]
    print(f"⬇️ İndiriliyor: {filename}")

    file_path = os.path.join(SAVE_DIR, filename)
    r = requests.get(link)

    with open(file_path, "wb") as f:
        f.write(r.content)

print("✅ Bitti! Tüm dosyalar indirildi.")
driver.quit()