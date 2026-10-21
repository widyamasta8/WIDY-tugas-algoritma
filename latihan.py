# Program Penilaian dan Status Kelulusan Mahasiswa (Tanpa Input Manual)

# 1. Nilai yang sudah ditentukan langsung di dalam variabel
nilai_tugas = 80  #[span_0](start_span)[span_0](end_span)
nilai_uts = 80  #[span_1](start_span)[span_1](end_span)
nilai_uas = 90  #[span_2](start_span)[span_2](end_span)
kehadiran = 95  #[span_3](start_span)[span_3](end_span)

# 2. Hitung nilai akhir dengan rumus
nilai_akhir = (0.20 * nilai_tugas) + (0.30 * nilai_uts) + (0.50 * nilai_uas)

# 3 & 4. Menentukan Syarat Kelulusan dan Predikat
syarat_lulus = (nilai_akhir >= 75) and (kehadiran >= 80)
syarat_predikat = (
    (nilai_akhir >= 85)
    and (kehadiran >= 90)
    and (int(nilai_akhir) % 2 == 0)
)

# 5 & 6. Logika Penentuan Status
if not syarat_lulus:
  status = "BELUM LULUS"
elif syarat_predikat:
  status = "LULUS DENGAN PREDIKAT"
else:
  status = "LULUS"

# Menampilkan Output persis seperti contoh di soal
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Status      : {status}")
