import csv

# Membuka file input (line_index.tsv)
input_file_path = './content/jvFemale/line_index.tsv'
output_file_path = './content/metadata.csv'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
    # Membuat objek pembaca dan penulis CSV
    reader = csv.reader(input_file, delimiter='\t')
    writer = csv.writer(output_file)

    # Menulis header ke file output
    writer.writerow(['wav', 'text', 'text_norm'])

    # Membaca baris per baris dari file input dan menulis ke file output
    for row in reader:
        wav_id = row[0]
        text = ' '.join(row[1:])
        # Menyamakan text dan text_norm karena tidak ada perbedaan dalam spesifikasi
        text_norm = text

        # Menulis baris ke file output
        writer.writerow([wav_id, text, text_norm])

print(f'File {output_file_path} berhasil dibuat.')
