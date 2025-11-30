import pandas as pd
import glob

files = sorted(glob.glob("data/transport/hourly_transportation_*.csv"))

print("Birleşecek dosyalar:")
for f in files:
    print(" -", f)

output = "data/transport/transport_merged.csv"

chunk_size = 200_000  # 200k satır kısıtı, RAM dostu

with open(output, "w", encoding="utf-8") as outfile:
    first = True    

    for f in files:
        print(f"\n👉 İşleniyor: {f}")
        for chunk in pd.read_csv(f, chunksize=chunk_size, low_memory=False):
            if first:
                chunk.to_csv(outfile, index=False)
                first = False
            else:
                chunk.to_csv(outfile, index=False, header=False)

print("\n✔ BİRLEŞTİRME TAMAMLANDI!")
print("✔ Çıktı:", output)