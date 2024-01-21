import csv


def remove_third_column(input_file, output_file):
    # Buka file input dan output
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        # Buat objek writer CSV
        csv_writer = csv.writer(outfile, delimiter='|')

        # Baca baris-baris dari file input
        for line in infile:
            # Pisahkan kolom menggunakan '|' sebagai pemisah
            columns = line.strip().split('|')
            # Ambil hanya dua kolom pertama
            columns = columns[:2]
            # Tulis ke file output dalam format CSV
            csv_writer.writerow(columns)


if __name__ == "__main__":
    # Ganti nama file input dan output sesuai kebutuhan
    input_file = './content/metadata1.csv'
    output_file = './content/metadata.csv'

    # Panggil fungsi remove_third_column
    remove_third_column(input_file, output_file)

    print(
        f"Kolom ketiga berhasil dihapus. Hasil disimpan dalam file: {output_file}")
