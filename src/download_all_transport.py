import os
import requests

SAVE_DIR = "data/transport"
os.makedirs(SAVE_DIR, exist_ok=True)

links = [
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/36f60fe4-6054-4660-88a6-bf09db0c1581/download/hourly_transportation_202401.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/b6e05542-ff81-4878-a4bc-a3bd3485947e/download/hourly_transportation_202402.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/56c66478-6b86-406d-a751-0ef2beb02124/download/hourly_transportation_202403.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/7116a2ed-ec97-47c9-9901-7d012db982e8/download/hourly_transportation_202404.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/857998e9-c051-4172-a988-757f03b1ac6c/download/hourly_transportation_202405.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/e653ab7b-22d3-419a-b55d-70ec99c6c312/download/hourly_transportation_202406.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/741d920a-97b3-4a30-a855-76107217583c/download/hourly_transportation_202407.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/2705d01c-4f2c-4ed3-8e6a-0a25696a5678/download/hourly_transportation_202408.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/4546fb79-e598-4dc7-888b-626361110e37/download/hourly_transportation_202409.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/ea8daee8-62e4-4c42-903f-15b5e372d902/download/hourly_transportation_202410.csv",
    "https://data.ibb.gov.tr/dataset/a6855ce7-4092-40a5-82b5-34cf3c7e36e3/resource/7368f923-dc2b-401a-9778-c33eb7083b27/download/hourly_transportation_202411.csv"
]

for url in links:
    filename = url.split("/")[-1]
    print(f"⬇️ {filename} indiriliyor...")
    resp = requests.get(url)
    with open(os.path.join(SAVE_DIR, filename), "wb") as f:
        f.write(resp.content)

print("✅ Tüm dosyalar indirildi!")