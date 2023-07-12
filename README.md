# UAS-PENGOLAHAN-CITRA-Erik-maulana-312110188
---
# UAS - Pengolahan Citra
```
Dosen Pengampu   : Muhammad Najamuddin Dwi Miharja, S.Kom, M.Kom
Mata Kuliah      : Pengolahan Citra
Nama             : Erik Maulana
Nim              : 312110188
Kelas            : TI.21.C.1
```
* **Berikut penjelasan singkat komponen utama dalam kode program tersebut :**  
```
1.) Import library:
    - `tkinter`: untuk membuat antarmuka grafis.
    - `math`: Digunakan untuk operasi matematika.
    - `filedialog` dari `tkinter`: Digunakan untuk mengatur dialog pengunggahan berkas.
    - `numpy`: untuk melakukan operasi numerik pada array.
    - `Image` dan `ImageTk` dari library PIL : untuk memanipulasi dan menampilkan gambar.



2.) Fungsi `calculate_mse(original, processed)`: Menghitung nilai Mean Squared Error (MSE) antara citra asli dan citra yang telah diproses dengan metode median filter.

3.) Fungsi `calculate_psnr(mse, max_pixel=255.0)`: Menghitung nilai Peak Signal-to-Noise Ratio (PSNR) berdasarkan nilai MSE dan nilai piksel maksimum.

4.) Fungsi `median_filter(image_array, filter_size)`: Menerapkan metode median filter pada array citra dengan ukuran filter tertentu. Fungsi ini mengembalikan citra yang telah diproses.

5.) Kelas `Application` yang mewarisi `tk.Tk`: Merupakan kelas utama yang mengatur antarmuka aplikasi dan interaksi pengguna. Pada konstruktor, elemen-elemen antarmuka seperti judul, frame gambar, label, tombol, dan sebagainya diinisialisasi dan ditampilkan. Ada juga metode `upload_image()` untuk mengunggah gambar, `process_image()` untuk memproses gambar dengan metode median filter, dan `display_image()` untuk menampilkan gambar pada canvas.

6.) Pada bagian terakhir, kode program memeriksa apakah file ini dijalankan langsung (`__name__ == "__main__"`) dan kemudian membuat objek `Application` dan memulai aplikasi dengan metode `mainloop()`.
```

* **Berikut ini  hasil dari program yang sudah di buat** *

  ![gambar](ss1/ss1.JGP)


