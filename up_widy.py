print("================================")
print("  SISTEM PENGELOLAAN STOK TOKO")
print("================================")

# 1. Input data barang
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

# 2. Perulangan transaksi
while True:
    print("\n===== MENU TRANSAKSI =====")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Cek Stok")
    print("4. Keluar")

    pilihan = input("Pilih transaksi (1-4): ")

    # 3. Proses transaksi
    if pilihan == "1":
        jumlah = int(input("Jumlah barang masuk: "))
        stok = stok + jumlah
        print("Barang berhasil ditambahkan!")

    elif pilihan == "2":
        jumlah = int(input("Jumlah barang keluar: "))

        # 4. Cek ketersediaan stok
        if jumlah <= stok:
            stok = stok - jumlah
            print("Barang berhasil dikeluarkan!")
        else:
            print("Stok Tidak Mencukupi!")

    elif pilihan == "3":
        print("Nama Barang :", nama_barang)
        print("Stok Tersedia:", stok)

    elif pilihan == "4":
        print("\n===== HASIL AKHIR =====")
        print("Nama Barang :", nama_barang)
        print("Sisa Stok    :", stok)
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")