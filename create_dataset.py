import pandas as pd

# Buat DataFrame dengan kolom "wav" dan "text_norm"
data = {
    "wav": ["audio1", "audio2", "audio3"],
    "text_norm": ["hello world", "how are you", "goodbye"]
}

df = pd.DataFrame(data)

# Simpan DataFrame ke dalam file CSV
csv_path = "./content/metadata.csv"
df.to_csv(csv_path, index=False)

print("Dataset CSV created successfully!")
