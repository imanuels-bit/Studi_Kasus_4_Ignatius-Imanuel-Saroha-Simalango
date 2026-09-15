dBuku = {
    "judul": "Blue Box",
    "penulis": "Kouji Miura",
    "Tahunterbit": 2021
}

milihnomor = ""

while milihnomor != "5":
    print("\n=== MENU PENGELOLAAN DATA BUKU ===")
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")
    milihnomor = input("Pilih menu (1-5): ")
    if milihnomor == "1":
        print("\nData buku sekarang:")
        print("Judul        :", dBuku["judul"])
        print("Penulis      :", dBuku["penulis"])
        print("Tahun terbit :", dBuku["Tahunterbit"])
        if "penerbit" in dBuku:
            print("Penerbit     :", dBuku["penerbit"])
    elif milihnomor == "2":
        penerbitb = input("Masukkan penerbit baru: ")
        dBuku["penerbit"] = penerbitb
        print("Penerbit baru telah ditambahkan")
        print("\nData buku sekarang:")
        print("Judul        :", dBuku["judul"])
        print("Penulis      :", dBuku["penulis"])
        print("Tahun terbit :", dBuku["Tahunterbit"])
        print("Penerbit     :", dBuku["penerbit"])
    elif milihnomor == "3":
        penulisb = input("Masukkan penulis baru: ")
        dBuku["penulis"] = penulisb
        print("Data penulis berhasil diubah")
        print("\nData buku sekarang:")
        print("Judul        :", dBuku["judul"])
        print("Penulis      :", dBuku["penulis"])
        print("Tahun terbit :", dBuku["Tahunterbit"])
        if "penerbit" in dBuku:
            print("Penerbit     :", dBuku["penerbit"])
    elif milihnomor == "4":
        if "penerbit" in dBuku:
            del dBuku["penerbit"]
        else:
            print("Data penerbit belum ada di dalam buku")
        print("\nData buku sekarang:")
        print("Judul        :", dBuku["judul"])
        print("Penulis      :", dBuku["penulis"])
        print("Tahun terbit :", dBuku["Tahunterbit"])
    elif milihnomor == "5":
        print("program selesai")
    else:
        print("pilihan cuman nomor...")