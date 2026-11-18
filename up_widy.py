# Studi Kasus: Sistem Pengelolaan Stok Barang Toko

# 1. Input data awal
nama_barang = input("Masukkan nama barang: ")
while True:
    try:
        stok = int(input("Masukkan jumlah stok awal: "))
        if stok < 0:
            print("Stok tidak boleh negatif!")
            continue
        break
    except ValueError:
        print("Masukkan angka yang valid!")

# 5. Perulangan agar transaksi bisa dilakukan berkali-kali
while True:
    # 2. Pilih transaksi
    print("\n=== MENU TRANSAKSI ===")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")
    pilihan = input("Pilih transaksi (1/2/3): ")

    if pilihan == "3":
        break

    if pilihan not in ("1", "2"):
        print("Pilihan tidak valid!")
        continue

    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue
    except ValueError:
        print("Masukkan angka yang valid!")
        continue

    # 3. Proses transaksi (percabangan)
    if pilihan == "1":
        stok += jumlah
        print(f"Berhasil! {jumlah} {nama_barang} masuk.")
    else:
        # 4. Cek stok
        if jumlah > stok:
            print("Stok Tidak Mencukupi")
        else:
            stok -= jumlah
            print(f"Berhasil! {jumlah} {nama_barang} keluar.")

    print(f"Stok {nama_barang} saat ini: {stok}")

# 6. Tampilkan hasil
print("\n=== HASIL AKHIR ===")
print(f"Nama barang : {nama_barang}")
print(f"Stok akhir  : {stok}")