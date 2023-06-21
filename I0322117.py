import json
import sys

def tambah_anggota(nama, alamat, telepon):
    # Membaca data anggota dari file JSON
    try:
        with open("anggotas.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Mencari ID anggota baru
    if data:
        last_id = max(map(int, data.keys()))
        new_id = str(last_id + 1)
    else:
        new_id = "1"

    # Membentuk data anggota baru
    anggota = {
        "idanggota": new_id,
        "nama": nama,
        "alamat": alamat,
        "tanggal": "2023-04-03",
        "telepon": telepon
    }

    # Menambahkan data anggota baru ke dalam dictionary
    data[new_id] = anggota

    # Menyimpan data anggota ke dalam file JSON
    with open("anggotas.json", "w") as file:
        json.dump(data, file)

    print("Berhasil menambahkan data anggota.")

# Contoh penggunaan fungsi tambah_anggota
print("Penambahan Data Anggota")
nama = input("Nama: ")
alamat = input("Alamat: ")
telepon = input("Nomor Telepon: ")
tambah_anggota(nama, alamat, telepon)


import json

def cari_anggota_by_id(id_anggota):
    with open('anggotas.json', 'r') as file:
        data = json.load(file)

    for idanggota, anggota in data.items():
        if anggota['idanggota'] == id_anggota:
            return anggota

    return {}

def tampilkan_anggota(anggota):
    print("ID Anggota:", anggota['idanggota'])
    print("Nama:", anggota['nama'])
    print("Alamat:", anggota['alamat'])
    print("Telepon:", anggota['telepon'])
    print("Tanggal Daftar:", anggota['tanggal'])

# Contoh penggunaan fungsi
def main():
    print("Pencarian data anggota")
    id_anggota = input("Masukkan ID Anggota: ")
    hasil = cari_anggota_by_id(id_anggota)

    if hasil:
        print("Data anggota ditemukan:")
        print(hasil)
        print("---------------------------------------")
        tampilkan_anggota(hasil)
    else:
        print("Data anggota tidak ditemukan.")

if __name__ == '__main__':
    main()

import json
import os

def cari_anggota_by_id(id_anggota):
    with open('anggotas.json', 'r') as file:
        data = json.load(file)

    for idanggota, anggota in data.items():
        if anggota['idanggota'] == id_anggota:
            return anggota

def edit_anggota():
    while True:
        print("Pengubahan Data Anggota")
        id_anggota = input("Ketik ID anggota yang akan diedit: ")
        anggota = cari_anggota_by_id(id_anggota)
        
        if not anggota:
            print("Data anggota tidak ditemukan!")
            jawaban = input("Cari lagi (Y/y = Ya, T/t = Tidak)? ")
            if jawaban.lower() != "y":
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear') 
            continue

def main():
    print("\nMenu:")
        print("=================================================")
        print("===== Program Pengelolaan Tabungan Sampah ======")
        print("=================================================")
        print("1. Pengelolaan keanggotaan")
        print("1a.Penambahan Data Anggota")
        print("1a.Pencarian Data Anggota")
        print("1a.Pengubahan Data Anggota")
        print("9. Exit")
        choice = input("Pilih menu (1a/1b/1c/9): ")

        if choice == "1a":
            # Tambahkan menu saat ini ke stack
            tambah_anggota(nama, alamat, telepon)
        elif choice == "1b":
            cari_anggota_by_id(id_anggota)
        elif choice == "1c":
            edit_anggota()
        elif choice == "9":
            print("Terima Kasih! Program selesai.")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
