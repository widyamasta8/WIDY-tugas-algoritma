#Program Penjualan Toko WIDY
nama = input("Masukkan Nama Anda: ")
total =int(input("total belanja (Rp):"))

diskon = 0
bonus = "tidak ada"

# Percabangan diskon
if total >= 500000:
    diskon = total * 10 / 100
elif total >= 200000:
    diskon = total * 5 / 100
else:
    diskon = 0

# bonus(terpisah dari diskon)
if total >= 1000000:
    bonus = "vocer belanja Rp50.000 "

total_bayar = total - diskon

# Output
print("==== STRUK TOKO WIDY ====")
print(f"Nama Pelanggan: {nama}")
print(f"Total Belanja : Rp{total:,.0f}".replace(",", "."))
print(f"Diskon        : Rp{diskon:,.0f}".replace(",", "."))
print(f"Total Bayar   : Rp{total_bayar:,.0f}".replace(",", "."))
print(f"Bonus         : {bonus}")
print(f"Total Bayar   : Rp{total_bayar:,.0f}".replace(",", "."))
print("Terima kasih telah berbelanja di Toko WIDY")