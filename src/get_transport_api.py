import pandas as pd
import requests
import os

# Klasör oluştur
os.makedirs("data/transport", exist_ok=True)

RESOURCE_ID = "79cf14b5-65ed-47f7-98ca-1a76ee70b4cc"
API_URL = f"https://ulasav.csb.gov.tr/api/3/action/datastore_search?resource_id={RESOURCE_ID}&limit=10000000"

print("📥 API üzerinden veri indiriliyor...")

response = requests.get(API_URL)
data = response.json()

if not data.get("success", False):
    print("❌ API isteği başarısız oldu!")
    print(data)
    exit()

records = data["result"]["records"]
df = pd.DataFrame(records)

output_path = "data/transport/transport_2024_api.csv"
df.to_csv(output_path, index=False)

print(f"✅ Veri başarıyla indirildi!")
print(f"📄 Kayıt sayısı: {len(df)}")
print(f"💾 Dosya: {output_path}")