from pydub import AudioSegment
import os


def downgrade_sample_rate(input_folder, output_folder, target_sample_rate=22050):
    # Membuat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop melalui semua file audio di folder input
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Membaca file audio
            audio = AudioSegment.from_file(input_path)

            # Menurunkan sample rate
            audio = audio.set_frame_rate(target_sample_rate)

            # Menyimpan file audio yang telah dimodifikasi
            # Anda bisa mengganti format sesuai kebutuhan
            audio.export(output_path, format="wav")

            print(
                f"File {filename} berhasil dimodifikasi dan disimpan di {output_folder}")


# Contoh penggunaan
input_folder = "./content/jvFemale/wavs"
output_folder = "./content/jvFemale/wavs2"
downgrade_sample_rate(input_folder, output_folder)
