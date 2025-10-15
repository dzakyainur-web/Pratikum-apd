
import os

users = {
    "ketua": {"password": "ketua2025"},
    "anggota": {"password": "anggotaasrama"}
}
data_anak_asrama = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("--- PENDATAAN ANAK ASRAMA BERAU ---")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    P = input("Pilih (1-3): ")

    if P == '1':
        os.system("cls" if os.name == "nt" else "clear")
        username = input("Buat nama kamu: ")
        password = input("Buat password kamu: ")
        if username in users:
            print("Username sudah digunakan orang lain, coba lagi.")
        else:
            users[username] = {"password": password}
            print(f"Anggota '{username}' berhasil terdaftar.")
        input("\nTekan Enter untuk lanjut...")

    elif P == '2':
        os.system("cls" if os.name == "nt" else "clear")
        username = input("Masukkan nama kamu: ")
        password = input("Masukkan password kamu: ")

        if username in users and users[username]["password"] == password:
            print(f"\nLogin berhasil! Selamat datang, {username}!\n")
            input("\nTekan Enter untuk lanjut...")

            #admin 
            if username == "ketua":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("""
                    ===============================
                    |   MENU ADMIN - DATA ASRAMA  |
                    ===============================
                    | 1. Tambah Data Anak Asrama  |
                    | 2. Tampilkan Data Asrama    |
                    | 3. Ubah Data Anak Asrama    |
                    | 4. Hapus Data Anak Asrama   |
                    | 5. Logout                   |
                    ===============================
                    """)
                    pilihm = input("Pilih menu (1-5): ")

                    if pilihm == '1':
                        nama = input("Nama: ")
                        asal = input("Asal Daerah Berau: ")
                        kamar = input("Nomor Kamar: ")
                        nomor_ortu = input("Nomor Orang Tua: ")
                        kampus = input("Kampus: ")
                        fakultas_prodi = input("Fakultas dan Prodi: ")
                        data_anak_asrama.append([nama, asal, kamar, nomor_ortu, kampus, fakultas_prodi])
                        print(f"Data {nama} berhasil ditambahkan.\n")
                        input("\nTekan Enter untuk lanjut...")

                    elif pilihm == '2':
                        if len(data_anak_asrama) == 0:
                            print("Belum ada data anak asrama.")
                        else:
                            print("\n--- DATA ANAK ASRAMA ---")
                            for i in range(len(data_anak_asrama)):
                                print(f"\nData ke-{i+1}")
                                print(f"Nama               : {data_anak_asrama[i][0]}")
                                print(f"Asal Daerah Berau  : {data_anak_asrama[i][1]}")
                                print(f"Nomor Kamar        : {data_anak_asrama[i][2]}")
                                print(f"Nomor Orang Tua    : {data_anak_asrama[i][3]}")
                                print(f"Kampus             : {data_anak_asrama[i][4]}")
                                print(f"Fakultas dan Prodi : {data_anak_asrama[i][5]}")
                                print("-----------------------------------------------")
                        input("\nTekan Enter untuk lanjut...")

                    elif pilihm == '3':
                        ubah = input("Masukkan nama yang akan diubah: ")
                        ditemukan = False
                        for i in range(len(data_anak_asrama)):
                            if data_anak_asrama[i][0] == ubah:
                                ditemukan = True
                                print(f"Mengubah data untuk {ubah}")
                                nama = input("Nama baru: ")
                                asal = input("Asal daerah baru: ")
                                kamar = input("Kamar baru: ")
                                nomor_ortu = input("Nomor baru: ")
                                kampus = input("Kampus baru: ")
                                fakultas_prodi = input("Fakultas dan prodi baru: ")
                                data_anak_asrama[i] = [nama, asal, kamar, nomor_ortu, kampus, fakultas_prodi]
                                print(f"Data {ubah} berhasil diubah.\n")
                                break
                        if not ditemukan:
                            print("Data tidak ditemukan.")
                        input("\nTekan Enter untuk lanjut...")

                    elif pilihm == '4':
                        hapus = input("Masukkan nama yang akan dihapus: ")
                        ditemukan = False
                        for i in range(len(data_anak_asrama)):
                            if data_anak_asrama[i][0] == hapus:
                                del data_anak_asrama[i]
                                ditemukan = True
                                print(f"Data {hapus} berhasil dihapus.")
                                break
                        if not ditemukan:
                            print("Data tidak ada.")
                        input("\nTekan Enter untuk lanjut...")

                    elif pilihm == '5':
                        print("Logout berhasil.")
                        input("\nTekan Enter untuk lanjut...")
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("\nTekan Enter untuk lanjut...")
            #anggota
            else:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("""
                    =================================
                    |   MENU ANGGOTA ASRAMA BERAU   |
                    =================================
                    | 1. Lihat Data Anak Asrama     |
                    | 2. Tambah Data Asrama         |
                    | 3. Logout                     |
                    =================================
                    """)
                    pilihn = input("Pilih menu (1-3): ")

                    if pilihn == '1':
                        if len(data_anak_asrama) == 0:
                            print("Belum ada data anak asrama.")
                        else:
                            print("\n--- DATA ANAK ASRAMA ---")
                            for i in range(len(data_anak_asrama)):
                                print(f"\nData ke-{i+1}")
                                print(f"Nama               : {data_anak_asrama[i][0]}")
                                print(f"Asal Daerah Berau  : {data_anak_asrama[i][1]}")
                                print(f"Nomor Kamar        : {data_anak_asrama[i][2]}")
                                print(f"Nomor Orang Tua    : {data_anak_asrama[i][3]}")
                                print(f"Kampus             : {data_anak_asrama[i][4]}")
                                print(f"Fakultas dan Prodi : {data_anak_asrama[i][5]}")
                                print("===============================================")
                        input("\nTekan Enter untuk lanjut...")

                    elif pilihn == '2':
                        nama = input("Nama: ")
                        asal = input("Asal Daerah: ")
                        kamar = input("Nomor Kamar: ")
                        nomor_ortu = input("Nomor Orang Tua: ")
                        kampus = input("Kampus: ")
                        fakultas_prodi = input("Fakultas dan Prodi: ")
                        data_anak_asrama.append([nama, asal, kamar, nomor_ortu, kampus, fakultas_prodi])
                        print(f"Data {nama} berhasil ditambahkan.")
                        input("\nTekan Enter untuk lanjut...")

                    elif pilihn == '3':
                        print("Logout berhasil.")
                        input("\nTekan Enter untuk lanjut...")
                        break
                    else:
                        print("Pilihan tidak ada.")
                        input("\nTekan Enter untuk lanjut...")

        else:
            print("Login gagal, Username atau password salah.")
            input("\nTekan Enter untuk lanjut...")

    elif P == '3':
        print("Terima kasih telah mendata")
        break

    else:
        print("Pilihan tidak ada")
        input("\nTekan Enter untuk lanjut...")

