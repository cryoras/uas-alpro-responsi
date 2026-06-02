import random
import os
from datetime import datetime

bank_soal = {
    "mudah": [
        {"teks": "katak",   "palindrom": True},
        {"teks": "malam",   "palindrom": True},
        {"teks": "level",   "palindrom": True},
        {"teks": "kodok",   "palindrom": True},
        {"teks": "radar",   "palindrom": True},
        {"teks": "kamu",    "palindrom": False},
        {"teks": "python",  "palindrom": False},
        {"teks": "ibu",     "palindrom": False},
        {"teks": "ini",     "palindrom": True},
        {"teks": "buku",    "palindrom": False},
    ],
    "sedang": [
        {"teks": "kasur rusak",  "palindrom": True},
        {"teks": "civic",        "palindrom": True},
        {"teks": "komputer",     "palindrom": False},
        {"teks": "aba",          "palindrom": True},
        {"teks": "palindrom",    "palindrom": False},
        {"teks": "rotator",      "palindrom": True},
        {"teks": "kertas",       "palindrom": False},
    ],
    "sulit": [
        {"teks": "step on no pets",  "palindrom": True},
        {"teks": "ibu pergi pasar",  "palindrom": False},
        {"teks": "kasur ini rusak",  "palindrom": True},
        {"teks": "aku suka baca",    "palindrom": False},
    ],
}

sesi = {
    "riwayat": [],          # list semua jawaban (kuis + manual)
    "skor_total": 0,        # akumulasi skor semua ronde
    "streak_terbaik": 0,    # streak terpanjang sepanjang sesi
    "last_statistik": None, # statistik ronde terakhir (untuk export)
}

def garis(char="─", panjang=52):
    """Cetak garis pemisah horizontal."""
    print("  " + char * panjang)


def judul(teks):
    """Cetak judul section dengan border atas-bawah."""
    garis("═")
    print(f"   {teks}")
    garis("═")


def bersihkan_layar():
    """Bersihkan terminal (Windows & Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def preprocessing(teks: str) -> str:
    """Ubah teks ke bentuk siap cek palindrom.

    Langkah:
    1. Ubah semua huruf menjadi huruf kecil (lowercase).
    2. Hapus semua karakter spasi.

    Args:
        teks: Teks asli yang akan dibersihkan.

    Returns:
        String baru hasil preprocessing (lowercase, tanpa spasi).

    Contoh:
        >>> preprocessing("Kasur Rusak")
        'kasurrusak'
    """
    pass


def is_palindrom(teks: str) -> bool:
    """Tentukan apakah teks adalah palindrom.

    Algoritma:
    - Teks diproses terlebih dahulu (lowercase, tanpa spasi).
    - Bandingkan karakter dari ujung depan dan ujung belakang secara
      bersamaan menggunakan satu loop (two-pointer manual).
    - Jika ada satu pasang yang tidak cocok → bukan palindrom.

    Args:
        teks: Teks asli yang akan dicek palindromnya.

    Returns:
        True jika palindrom setelah preprocessing, False jika tidak.

    Contoh:
        >>> is_palindrom("Kasur Rusak")
        True
        >>> is_palindrom("python")
        False
    """
    pass


def hitung_karakter(teks: str) -> int:
    """Hitung jumlah karakter pada teks asli.

    Menghitung SEMUA karakter termasuk spasi, tanda baca, dsb.
    Tidak menggunakan len() built-in — dihitung secara manual via loop.

    Args:
        teks: Teks asli yang dihitung jumlah karakternya.

    Returns:
        Total karakter pada teks asli (termasuk spasi).

    Contoh:
        >>> hitung_karakter("kasur rusak")
        11
    """
    pass


def hitung_kata(teks: str) -> int:
    """Hitung jumlah kata berdasarkan pemisah spasi.

    Menggunakan split() untuk memecah teks berdasarkan spasi.
    Spasi ganda otomatis diabaikan oleh split().

    Args:
        teks: Teks asli yang dihitung jumlah katanya.

    Returns:
        Total kata setelah mengabaikan spasi ganda.

    Contoh:
        >>> hitung_kata("kasur rusak")
        2
        >>> hitung_kata("step on no pets")
        4
    """
def mulai_kuis(level, soal_list):
    skor = 0
    benar = 0
    salah = 0

    print(f"\n=== Level {level} Dimulai! ===")

    for i, soal in enumerate(soal_list, 1):
        print(f"\nSoal {i}: Apakah '{soal}' adalah palindrom? (y/n)")
        jawaban = input("Jawaban: ").lower()

        # cek palindrom
        if soal == soal[::-1]:
            kunci = 'y'
        else:
            kunci = 'n'

        if jawaban == kunci:
            print(" Benar!")
            skor += 10
            benar += 1
        else:
            print(f"Salah! Jawaban yang benar: {kunci}")
            salah += 1

    statistik = {
        "total": len(soal_list),
        "benar": benar,
        "salah": salah,
        "skor": skor
    }

    return statistik

def tampilkan_statistik(statistik):
    total = statistik["total"]
    benar = statistik["benar"]
    salah = statistik["salah"]
    skor = statistik["skor"]

    akurasi = (benar / total) * 100 if total > 0 else 0

    print("\n=== HASIL KUIS ===")
    print(f"Total Soal   : {total}")
    print(f"Benar        : {benar}")
    print(f"Salah        : {salah}")
    print(f"Akurasi      : {akurasi:.2f}%")
    print(f"Skor Akhir   : {skor}")

def main():
    while True:
        print("\n=== PALINQUIZ CLI ===")
        print("1. Mulai Kuis")
        print("2. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            soal_level1 = ["katak", "apel", "radar", "pisang"]

            statistik = mulai_kuis("1", soal_level1)
            tampilkan_statistik(statistik)

        elif pilihan == "2":
            print("Terima kasih sudah bermain!")
            break

        else:
            print("Pilihan tidak valid!")


def hitung_vokal(teks: str) -> int:
    """Hitung jumlah huruf vokal pada teks.

    Menghitung kemunculan huruf a, i, u, e, o tanpa memperhatikan kapital.
    Huruf kapital ditangani dengan mengubah teks ke lowercase sebelum cek.

    Args:
        teks: Teks asli yang dihitung jumlah vokalnya.

    Returns:
        Total huruf vokal (a, i, u, e, o) tanpa memperhatikan kapital.

    Contoh:
        >>> hitung_vokal("katak")
        2
        >>> hitung_vokal("kasur rusak")
        4
    """
    jumlah_vokal = 0

    for huruf in hasil:

        if huruf in "aiueo":
            jumlah_vokal += 1

    print("Jumlah vokal :", jumlah_vokal)

    
    data = {
        "teks": teks,
        "status": status,
        "mode": "manual"
    }

    riwayat.append(data)

    print("\nData masuk ke riwayat\n")



def tampilkan_analisis(teks: str, status: bool) -> None:
    """Tampilkan analisis lengkap untuk satu soal.

    Args:
        teks: Teks soal yang dianalisis.
        status: Status palindrom yang sudah dihitung (True/False).

    Returns:
        None. Fungsi ini menghasilkan output ke layar.
    """



def mulai_kuis() -> None:
    """Jalankan kuis interaktif.

    Alur:
    1. User memilih level (mudah / sedang / sulit).
    2. Bank soal untuk level tersebut di-shuffle secara acak.
    3. Setiap soal ditampilkan satu per satu:
       - Tampilkan teks soal.
       - Minta input jawaban user (1=Ya / 2=Tidak).
       - Verifikasi jawaban, update skor & streak.
       - Tampilkan analisis teks.
       - Simpan ke riwayat sesi.
    4. Setelah semua soal selesai, tampilkan statistik ronde.

    Returns:
        None. Fungsi ini mengelola input/output kuis dan pembaruan data sesi.
    """



def tampilkan_riwayat(riwayat: list) -> None:
    """Tampilkan daftar riwayat jawaban selama sesi berjalan.

    Menampilkan tabel semua entri riwayat dari sesi ini,
    lalu menawarkan opsi sorting (panjang teks / hasil).

    Args:
        riwayat: List berisi entri riwayat (teks, jawaban user, jawaban benar).

    Returns:
        None. Fungsi ini menghasilkan output ke layar.
    """
    if len(riwayat) == 0:
        print("\nBelum ada riwayat\n")
        return

    print("\n=== RIWAYAT ===")
    print("1. Sort panjang teks")
    print("2. Sort benar dulu")
    print("3. Tanpa sort")

    pilih = input("Pilih: ")

    data = riwayat.copy()

    if pilih == "1":
        data.sort(key=lambda x: len(x["teks"]))

    elif pilih == "2":
        data.sort(key=lambda x: x["status"] != "Benar")

    print("\n--------------------------------------------------")
    print("No\tStatus\t\tMode\t\tTeks")
    print("--------------------------------------------------")

    no = 1

    for item in data:
        print(
            str(no) + "\t" +
            item["status"] + "\t\t" +
            item["mode"] + "\t\t" +
            item["teks"]
        )

        no += 1

    print("--------------------------------------------------")




def cek_manual() -> None:
    """Mode cek palindrom dari input manual pengguna.

    User bebas memasukkan kata atau kalimat apapun.
    Program menampilkan analisis lengkap dan menyimpan hasilnya
    ke riwayat sesi dengan label level = 'manual'.
    Ketik 'selesai' untuk kembali ke menu utama.

    Returns:
        None. Fungsi ini meminta input dan menampilkan hasil analisis.
    """
     print("\n=== MODE CEK MANUAL ===")

    teks = input("Masukkan teks: ")

    hasil = teks.lower().replace(" ", "")

    kiri = 0
    kanan = len(hasil) - 1

    palindrom = True

    while kiri < kanan:

        if hasil[kiri] != hasil[kanan]:
            palindrom = False
            break

        kiri += 1
        kanan -= 1

    if palindrom:
        status = "Palindrom"
    else:
        status = "Bukan"

    print("\nHasil:")
    print("Teks asli :", teks)
    print("Setelah preprocess :", hasil)
    print("Status :", status)
    print("Jumlah karakter :", len(teks))
    print("Jumlah kata :", len(teks.split()))






def tampilkan_statistik(statistik: dict) -> None:
    """Tampilkan statistik akhir permainan satu ronde.

    Menampilkan ringkasan performa beserta komentar motivasi
    berdasarkan nilai akurasi yang dicapai.

    Args:
        statistik: Dict statistik akhir dengan key:
                   level, total, benar, salah, akurasi, skor.

    Returns:
        None. Fungsi ini menghasilkan output ke layar.
    """



def export_hasil(
    riwayat: list, statistik: dict, nama_file: str = "hasil_quiz.txt") -> None
    """Simpan riwayat dan statistik ke file teks.
    
    Menulis header, statistik ronde terakhir, dan seluruh entri riwayat
    ke file .txt. File disimpan di direktori yang sama dengan script.
    
    Args:
        riwayat   : List berisi entri riwayat sesi.
        statistik : Dict statistik akhir permainan.
        nama_file : Nama file tujuan (default: 'hasil_quiz.txt').
    
    Returns:
        None. Fungsi ini menulis output ke file.
    """
        
    if len(riwayat) == 0:
        print("\nBelum ada data\n")
        return

    file = open("hasil_quiz.txt", "w")

    file.write("===== HASIL PALINQUIZ =====\n\n")

    file.write("STATISTIK\n")
    file.write("Total : " + str(statistik_sesi["total"]) + "\n")
    file.write("Benar : " + str(statistik_sesi["benar"]) + "\n")
    file.write("Salah : " + str(statistik_sesi["salah"]) + "\n")
    file.write("Skor  : " + str(statistik_sesi["skor"]) + "\n")

    if statistik_sesi["total"] > 0:
        akurasi = (
            statistik_sesi["benar"] /
            statistik_sesi["total"]
        ) * 100
    else:
        akurasi = 0

    file.write("Akurasi : " + str(round(akurasi, 2)) + "%\n")

    file.write("\n===== RIWAYAT =====\n\n")

    no = 1

    for item in riwayat:

        file.write(str(no) + ". " + item["teks"] + "\n")
        file.write("Status : " + item["status"] + "\n")
        file.write("Mode   : " + item["mode"] + "\n\n")

        no += 1

    file.close()

    print("\nBerhasil export ke hasil_quiz.txt\n")




def main() -> None:
    """Tampilkan menu utama dan routing ke semua fitur.

    Loop utama program. Menampilkan banner dan menu,
    lalu memanggil fungsi yang sesuai berdasarkan pilihan user.
    Program berhenti ketika user memilih [0] Keluar.

    Returns:
        None.
    """
    bersihkan_layar()

    # banner pembuka
    print("""
  ╔════════════════════════════════════════════════╗
  ║                                                ║
  ║          🎮  P A L I N Q U I Z                ║
  ║         Game Tebak Palindrom CLI               ║
  ║                                                ║
  ║    UAP Algoritma Pemrograman — Unila 2026      ║
  ╚════════════════════════════════════════════════╝
    """)
    pass

if __name__ == "__main__":
    main()
