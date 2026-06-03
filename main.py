import os
import random
from datetime import datetime


bank_soal = {
    "mudah": [
        {"teks": "katak", "palindrom": True},
        {"teks": "malam", "palindrom": True},
        {"teks": "level", "palindrom": True},
        {"teks": "kodok", "palindrom": True},
        {"teks": "radar", "palindrom": True},
        {"teks": "kamu", "palindrom": False},
        {"teks": "python", "palindrom": False},
        {"teks": "ibu", "palindrom": False},
        {"teks": "ini", "palindrom": True},
        {"teks": "buku", "palindrom": False},
    ],
    "sedang": [
        {"teks": "kasur rusak", "palindrom": True},
        {"teks": "civic", "palindrom": True},
        {"teks": "komputer", "palindrom": False},
        {"teks": "aba", "palindrom": True},
        {"teks": "palindrom", "palindrom": False},
        {"teks": "rotator", "palindrom": True},
        {"teks": "kertas", "palindrom": False},
    ],
    "sulit": [
        {"teks": "step on no pets", "palindrom": True},
        {"teks": "ibu pergi pasar", "palindrom": False},
        {"teks": "kasur ini rusak", "palindrom": True},
        {"teks": "aku suka baca", "palindrom": False},
    ],
}


sesi = {
    "riwayat": [],  # list semua jawaban (kuis + manual)
    "skor_total": 0,  # akumulasi skor semua ronde
    "last_statistik": None,  # statistik ronde terakhir (untuk export)
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



# zahlian
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
    hasil = ""
    for huruf in teks.lower():  # iterasi tiap huruf setelah lowercase
        if huruf != " ":  # abaikan spasi
            hasil += huruf
    return hasil


# rima
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
    bersih = preprocessing(teks)
    n = len(bersih)
    for i in range(n // 2):  # hanya perlu cek setengah panjang
        if bersih[i] != bersih[n - 1 - i]:  # bandingkan depan vs belakang
            return False
    return True


# rima
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
    jumlah = 0
    for _ in teks:  # iterasi tiap karakter, tambah counter
        jumlah += 1
    return jumlah


# rima
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
    kata = teks.strip().split()  # split() tanpa argumen: pisah di semua whitespace
    return len(kata)



 # zahlian
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
    vokal = "aiueo"
    jumlah = 0
    for huruf in teks.lower():  # lowercase dulu agar A == a
        if huruf in vokal:
            jumlah += 1
    return jumlah


# zahlian
def tampilkan_analisis(teks: str, status: bool) -> None:
    """Tampilkan analisis lengkap untuk satu soal.

    Args:
        teks: Teks soal yang dianalisis.
        status: Status palindrom yang sudah dihitung (True/False).

    Returns:
        None. Fungsi ini menghasilkan output ke layar.
    """
    bersih = preprocessing(teks)
    garis()
    print("   ANALISIS TEKS")
    garis()
    print(f"   Teks asli          : {teks}")
    print(f"   Setelah preprocess : {bersih}")
    print(f"   Status palindrom   : {'✓ Palindrom' if status else '✗ Bukan Palindrom'}")
    print(f"   Jumlah karakter    : {hitung_karakter(teks)}")
    print(f"   Jumlah kata        : {hitung_kata(teks)}")
    print(f"   Jumlah huruf vokal : {hitung_vokal(teks)}")
    garis()


# billy
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
    judul("MULAI KUIS")
    print("  Pilih level kesulitan:\n")
    print("   [1] Mudah  — kata pendek (10 soal)")
    print("   [2] Sedang — kata panjang & frasa (7 soal)")
    print("   [3] Sulit  — kalimat (4 soal)")
    print("   [0] Kembali ke menu")
    garis()

    pilihan = input("  Pilihan: ").strip()
    level_map = {"1": "mudah", "2": "sedang", "3": "sulit"}

    if pilihan == "0":
        return
    if pilihan not in level_map:
        print("\n  ⚠  Pilihan tidak valid.")
        input("  Tekan Enter untuk kembali...")
        return

    level = level_map[pilihan]
    soal_list = bank_soal[level].copy()
    random.shuffle(soal_list)  # acak urutan soal tiap ronde

    # variabel ronde
    skor = 0
    streak = 0
    total_benar = 0
    total_salah = 0

    bersihkan_layar()
    judul(f"LEVEL: {level.upper()} | {len(soal_list)} SOAL")

    for nomor, soal in enumerate(soal_list, 1):
        teks = soal["teks"]
        jawaban_benar = soal["palindrom"]

        # header soal
        print(
            f"\n  Soal {nomor}/{len(soal_list)}  |  Skor: {skor}  |  Streak: {streak} {'🔥' if streak >= 3 else ''}"
        )
        garis()
        print(f'   Teks: "{teks}"')
        print(f"\n   Apakah teks ini PALINDROM?")
        print("   [1] Ya     [2] Tidak")
        garis()

        # validasi input user
        while True:
            jawaban_input = input("  Jawaban: ").strip()
            if jawaban_input in ["1", "2"]:
                break
            print("  ⚠  Masukkan 1 atau 2.")

        jawaban_user = jawaban_input == "1"
        benar = jawaban_user == jawaban_benar

        # update skor & streak
        if benar:
            skor += 10
            streak += 1
            total_benar += 1
            print("\n  ✓  BENAR! +10 poin")
            if streak >= 3:
                print(f"  🔥  Streak {streak}! Luar biasa!")
        else:
            streak = 0
            total_salah += 1
            print("\n  ✗  SALAH!")

        # analisis teks
        tampilkan_analisis(teks, jawaban_benar)

        # simpan riwayat
        sesi["riwayat"].append(
            {
                "teks": teks,
                "jawaban_user": "Ya" if jawaban_user else "Tidak",
                "jawaban_benar": "Ya" if jawaban_benar else "Tidak",
                "hasil": "Benar" if benar else "Salah",
                "level": level,
            }
        )

        input("  Tekan Enter untuk lanjut...")
        bersihkan_layar()

    # update sesi global
    sesi["skor_total"] += skor

    # buat dict statistik ronde ini
    statistik = {
        "level": level,
        "total": len(soal_list),
        "benar": total_benar,
        "salah": total_salah,
        "akurasi": round((total_benar / len(soal_list)) * 100, 1),
        "skor": skor,
    }
    sesi["last_statistik"] = statistik  # simpan untuk export

    tampilkan_statistik(statistik)


# nody
def tampilkan_riwayat(riwayat: list) -> None:
    """Tampilkan daftar riwayat jawaban selama sesi berjalan.

    Menampilkan tabel semua entri riwayat dari sesi ini,
    lalu menawarkan opsi sorting (panjang teks / hasil).

    Args:
        riwayat: List berisi entri riwayat (teks, jawaban user, jawaban benar).

    Returns:
        None. Fungsi ini menghasilkan output ke layar.
    """
    judul("RIWAYAT PENGECEKAN")

    if not riwayat:
        print("  Belum ada riwayat dalam sesi ini.")
        input("\n  Tekan Enter untuk kembali...")
        return

    # header tabel
    print(f"   {'No':<4} {'Teks':<22} {'Jawaban':<9} {'Benar':<9} {'Hasil':<8} Level")
    garis()
    for i, e in enumerate(riwayat, 1):
        print(
            f"   {i:<4} {e['teks']:<22} {e['jawaban_user']:<9} {e['jawaban_benar']:<9} {e['hasil']:<8} {e['level']}"
        )
    garis()
    print(f"   Total data: {len(riwayat)} entri")

    # opsi sorting
    print("\n  Urutkan riwayat berdasarkan:")
    print("   [1] Panjang teks (pendek → panjang)")
    print("   [2] Hasil (Benar dulu)")
    print("   [0] Kembali")
    pilihan = input("  Pilihan: ").strip()

    if pilihan == "1":
        terurut = sorted(riwayat, key=lambda x: len(x["teks"]))
        print("\n  Riwayat diurutkan (pendek → panjang):\n")
        for i, e in enumerate(terurut, 1):
            print(f'   {i}. [{e["hasil"]}] "{e["teks"]}"  ({len(e["teks"])} karakter)')

    elif pilihan == "2":
        # "Benar" < "Salah" secara alfabet, jadi Benar muncul duluan
        terurut = sorted(riwayat, key=lambda x: x["hasil"])
        print("\n  Riwayat diurutkan (Benar dulu):\n")
        for i, e in enumerate(terurut, 1):
            print(f'   {i}. [{e["hasil"]}] "{e["teks"]}"')

    input("\n  Tekan Enter untuk kembali...")


# nody
def cek_manual() -> None:
    """Mode cek palindrom dari input manual pengguna.

    User bebas memasukkan kata atau kalimat apapun.
    Program menampilkan analisis lengkap dan menyimpan hasilnya
    ke riwayat sesi dengan label level = 'manual'.
    Ketik 'selesai' untuk kembali ke menu utama.

    Returns:
        None. Fungsi ini meminta input dan menampilkan hasil analisis.
    """
    judul("MODE CEK MANUAL")
    print("  Masukkan kata atau kalimat untuk dicek palindromnya.")
    print("  Ketik 'selesai' untuk kembali ke menu.\n")

    while True:
        teks = input("  Teks: ").strip()

        if teks.lower() == "selesai":
            print("\n  Kembali ke menu utama...")
            break

        if not teks:
            print("  ⚠  Teks tidak boleh kosong.\n")
            continue

        status = is_palindrom(teks)
        tampilkan_analisis(teks, status)

        # simpan ke riwayat sesi
        sesi["riwayat"].append(
            {
                "teks": teks,
                "jawaban_user": "-",
                "jawaban_benar": "Ya" if status else "Tidak",
                "hasil": "Manual",
                "level": "manual",
            }
        )
        print()  # jarak antar cek


# billy
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
    judul("STATISTIK PERMAINAN")
    print(f"   Level            : {statistik['level'].upper()}")
    print(f"   Total soal       : {statistik['total']}")
    print(f"   Jawaban benar    : {statistik['benar']}  ✓")
    print(f"   Jawaban salah    : {statistik['salah']}  ✗")
    print(f"   Akurasi          : {statistik['akurasi']}%")
    print(f"   Skor ronde ini   : {statistik['skor']}")
    print(f"   Skor total sesi  : {sesi['skor_total']}")
    garis()

    # komentar berdasarkan akurasi
    akurasi = statistik["akurasi"]
    if akurasi == 100:
        print("   🏆  SEMPURNA! Kamu menguasai palindrom!")
    elif akurasi >= 80:
        print("   🎉  Hebat! Sedikit lagi sempurna!")
    elif akurasi >= 60:
        print("   👍  Lumayan! Terus berlatih ya!")
    else:
        print("   💪  Jangan menyerah, coba lagi!")
    garis()

    input("\n  Tekan Enter untuk kembali ke menu...")


# nody
def export_hasil(
    riwayat: list, statistik: dict, nama_file: str = "hasil_quiz.txt"
) -> None:
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
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(nama_file, "w", encoding="utf-8") as f:
        f.write("=" * 52 + "\n")
        f.write("   HASIL PALINQUIZ\n")
        f.write(f"   Waktu   : {waktu}\n")
        f.write(f"   Level   : {statistik['level'].upper()}\n")
        f.write("=" * 52 + "\n\n")

        f.write("STATISTIK:\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total soal       : {statistik['total']}\n")
        f.write(f"Jawaban benar    : {statistik['benar']}\n")
        f.write(f"Jawaban salah    : {statistik['salah']}\n")
        f.write(f"Akurasi          : {statistik['akurasi']}%\n")
        f.write(f"Skor             : {statistik['skor']}\n")
        f.write("RIWAYAT JAWABAN:\n")
        f.write("-" * 52 + "\n")
        for i, e in enumerate(riwayat, 1):
            status_ikon = "✓" if e["hasil"] in ("Benar", "Manual") else "✗"
            f.write(f'{i:>3}. {status_ikon} [{e["hasil"]:<6}] "{e["teks"]}"\n')
            if e["jawaban_user"] != "-":
                f.write(
                    f"       Jawaban: {e['jawaban_user']}  |  Kunci: {e['jawaban_benar']}\n"
                )
        f.write("\n" + "=" * 52 + "\n")

    print(f"\n  ✓  Hasil tersimpan di '{nama_file}'")
    input("  Tekan Enter untuk kembali...")


# billy
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

    while True:
        print("  MENU UTAMA")
        garis()
        print("   [1]  Mulai Kuis")
        print("   [2]  Lihat Riwayat")
        print("   [3]  Mode Cek Manual")
        # menu [4] hanya muncul kalau sudah ada statistik yang bisa di-export
        if sesi["last_statistik"]:
            print("   [4]  Export Hasil ke .txt")
        print("   [0]  Keluar")
        garis()

        pilihan = input("  Pilihan: ").strip()

        if pilihan == "1":
            bersihkan_layar()
            mulai_kuis()
            bersihkan_layar()

        elif pilihan == "2":
            bersihkan_layar()
            tampilkan_riwayat(sesi["riwayat"])
            bersihkan_layar()

        elif pilihan == "3":
            bersihkan_layar()
            cek_manual()
            bersihkan_layar()

        elif pilihan == "4" and sesi["last_statistik"]:
            nama = input("\n  Nama file (Enter = 'hasil_quiz.txt'): ").strip()
            if not nama:
                nama = "hasil_quiz.txt"
            export_hasil(sesi["riwayat"], sesi["last_statistik"], nama)
            bersihkan_layar()

        elif pilihan == "0":
            bersihkan_layar()
            print("\n  Terima kasih sudah bermain PalinQuiz!")
            print(f"  Skor total sesi ini : {sesi['skor_total']}")
            print("\n  Sampai jumpa! 👋\n")
            break

        else:
            print("\n  ⚠  Pilihan tidak valid, coba lagi.\n")


if __name__ == "__main__":
    main()
