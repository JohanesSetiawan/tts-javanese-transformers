import csv


def convert_format(input_file, output_file):
    # Buka file input dan output
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        # Buat objek writer CSV
        csv_writer = csv.writer(outfile)

        # Tulis header untuk metadata.csv
        csv_writer.writerow(['wav', 'text_norm'])

        # Baca baris-baris dari file input
        for line in infile:
            # Pisahkan kolom menggunakan tab ("\t") sebagai pemisah
            columns = line.strip().split('\t')

            # Ambil ID audio dan teks dari kolom pertama dan kedua
            audio_id, text = columns[0], columns[1]

            # Tulis ke file output dalam format CSV
            csv_writer.writerow([audio_id, text])


if __name__ == "__main__":
    # Ganti nama file input dan output sesuai kebutuhan
    input_file = './content/ljspeech/metadata.csv'
    output_file = './content/metadata.csv'

    # Panggil fungsi convert_format
    convert_format(input_file, output_file)

    print(f"Format berhasil diubah. Hasil disimpan dalam file: {output_file}")
