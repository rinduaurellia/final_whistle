1. Langkah mengimplementasi Checklist tugas : 
1) Untuk membuat sebuah proyek Django baru, pertama saya membuat new repository di github sesuai dengan nama aplikasi yang saya gunakan yaitu 'Final Whistle', kemudian saya membuat direktori lokal baru dan membuat virtual environtment di dalamnya yang berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain kemudian aktifkan.

2) Langkah kedua adalah menyiapkan dependencies (library, framework, package) dan lakukan instalasi terhadap dependencies yang ada kemudian buat proyek Django.

3) Buat environtment variables yang disimpan di luar kode program dan digunakan untuk menyimpan informasi kredensial database tanpa perlu mengubah kode. Kemudian saya masukkan DB_NAME, HOST dan lainnya sesuai dengan variabel yang telah diberikan. Kemudian, tambahkan ALLOWED_HOST dengan DB_NAME atau host yang diperbolehkan untuk mengubah kode

4) Migrasi databse untuk menyinkronkan kode dmodel di Django dengan struktur database tanpa harus ubah secara manual. Kemudian jalankan server Django dan ketika peramban web sudah berfungsi (http://localhost:8000), nonaktifkan server kemudian push ke github.

5) Untuk membuat aplikasi main dalam proyek 'Final Whistle' saya akan menjalankan 'python manage.py startapp main' dan mendaftarkan aplikasi main ke proyek (settings.py). main tersebut saya ubah variabel nya dengan ketentuan yang sudah diberikan (name, price, description, dll).

6) Setelah template (html file) dimodifikasi berupa nama aplikai, npm, dan kelas, saya memetakan suatu URL ke sebuah fungsi view yang sudah didefinisikan (routing) dengan menambahkan view di views.py Semua rute dari aplikasi main juga harus dapat diakses langsung lewat http://localhost:8000/.

7) Tidak lupa juga melakukan deployment ke PWS dengan membuat project baru bernama 'finalwhistle' kemudian ubah beberapa hal seperti SCHEMA dan production. Kemudian push ke github dan periksa secara berkala mengenai proses deployment ini apakah sudah sukses pada server Django.


2. 
