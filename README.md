# Face Recognition (Deteksi Wajah)

Proyek sederhana untuk mendeteksi wajah, mata, dan senyuman menggunakan OpenCV dan Haar Cascades.

## Struktur proyek

- `FaceDetection.py` - deteksi wajah dasar.
- `FaceEyeDetection.py` - deteksi wajah dan mata.
- `FaceEyeSmileDetection.py` - deteksi wajah, mata, dan senyuman.
- `Cascades/` - berisi file Haar Cascade yang diperlukan:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`
  - `haarcascade_smile.xml`

## Prasyarat

- Python 3.5 atau lebih baru direkomendasikan.
- pip
- (Rekomendasi) virtual environment seperti `venv`.

## Instalasi

1. Buka terminal (Command Prompt atau PowerShell) dan masuk ke folder proyek.

2. (Opsional tetapi direkomendasikan) Buat dan aktifkan virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# atau untuk Command Prompt
.\.venv\Scripts\activate.bat
```

3. Pasang dependensi yang diperlukan:

```powershell
pip install --upgrade pip
pip install opencv-python
```


## Menjalankan program

Semua skrip menggunakan kamera bawaan (webcam) secara default. Jalankan masing-masing file dari terminal:

- Deteksi wajah saja:

```powershell
python FaceDetection.py
```

- Deteksi wajah dan mata:

```powershell
python FaceEyeDetection.py
```

- Deteksi wajah, mata, dan senyuman:

```powershell
python FaceEyeSmileDetection.py
```

Tekan tombol `esc` atau tutup jendela video untuk menghentikan program.

## Lokasi file cascade

Pastikan folder `Cascades/` tetap berada di dalam direktori proyek dan file XML cascade ada di sana. Skrip mencari berkas-berkas cascade relatif terhadap lokasi proyek — jika Anda memindahkan file .py ke folder lain, perbarui path di dalam skrip.

## Troubleshooting

- Tidak ada kamera terdeteksi: pastikan webcam terpasang dan tidak digunakan aplikasi lain.
- Error import OpenCV: periksa instalasi `opencv-python` dan versi Python yang digunakan.
- Program tidak menemukan file cascade: pastikan folder `Cascades/` dan nama file XML benar.