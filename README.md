1. Langkah mengimplementasi Checklist tugas : 
1) Untuk membuat sebuah proyek Django baru, pertama saya membuat new repository di github sesuai dengan nama aplikasi yang saya gunakan yaitu 'Final Whistle', kemudian saya membuat direktori lokal baru dan membuat virtual environtment di dalamnya yang berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain kemudian aktifkan.

2) Langkah kedua adalah menyiapkan dependencies (library, framework, package) dan lakukan instalasi terhadap dependencies yang ada kemudian buat proyek Django.

3) Buat environtment variables yang disimpan di luar kode program dan digunakan untuk menyimpan informasi kredensial database tanpa perlu mengubah kode. Kemudian saya masukkan DB_NAME, HOST dan lainnya sesuai dengan variabel yang telah diberikan. Kemudian, tambahkan ALLOWED_HOST dengan DB_NAME atau host yang diperbolehkan untuk mengubah kode

4) Migrasi databse untuk menyinkronkan kode dmodel di Django dengan struktur database tanpa harus ubah secara manual. Kemudian jalankan server Django dan ketika peramban web sudah berfungsi (http://localhost:8000), nonaktifkan server kemudian push ke github.

5) Untuk membuat aplikasi main dalam proyek 'Final Whistle' saya akan menjalankan 'python manage.py startapp main' dan mendaftarkan aplikasi main ke proyek (settings.py). main tersebut saya ubah variabel nya dengan ketentuan yang sudah diberikan (name, price, description, dll).

6) Setelah template (html file) dimodifikasi berupa nama aplikai, npm, dan kelas, saya memetakan suatu URL ke sebuah fungsi view yang sudah didefinisikan (routing) dengan menambahkan view di views.py Semua rute dari aplikasi main juga harus dapat diakses langsung lewat http://localhost:8000/.

7) Tidak lupa juga melakukan deployment ke PWS dengan membuat project baru bernama 'finalwhistle' kemudian ubah beberapa hal seperti SCHEMA dan production. Kemudian push ke github dan periksa secara berkala mengenai proses deployment ini apakah sudah sukses pada server Django.


2. BAGAN REQUEST CLIENT KE WEB : 
https://drive.google.com/file/d/1-2-GJIkhWIBaRN_kEZFXjAURWHp1IzPW/view?usp=sharing

Hal pertama adalah client request ke internet dan request tersebut akan diterima oleh Django kemudian argumen atau request tersebut diterima oleh views.py. Views akan melihat argumen tersebut meminta apa atau tipe data apa. Jika argumen meminta informasi yang ada di database (seperti informasi pembuatan dan berakhir project) maka ia harus meneruskan ke bagian models.py

Models.py akan meneruskan permintaan client ke database dan mencari data yang diminta karena hanya models.py yang memiliki hak untuk mengatur pengambilan data bukan menyimpan. Setelah data diambil, models.py akan meneruskan ke views.py kemudian meneruskan ke index.html untuk membuat template kodenya dan diteruskan ke Django. Setelah itu informasi akan diteruskan ke client melalui internet.

3. Peran settings.py dalam proyek Django adalah sebagai pusat konfigurasi utama proyek agar bisa berjalan sesuai dengan keinginan, baik saat developemnt maupun production. Settings.py yang berisi pengaturan untuk proyek Django seperti menentukan konfigusari proyek, mengatur aplikasi yang aktif dijalankan, mengatur keamanan dan respons proyek, mengatur URL dan template, dan masih banyak lagi.

4. Cara kerja migrasi database di Django : 
Migrasi database bekerja dengan cara menyingkronkan model Python dengan struktur database yang sudah ada. Ketika mengubah model di models.py, Django akan mendeteksi perubahan dan melakukan file migration dengan prompt 'python manage.py migrate' yang berisi instruksi perubahan database. File yang di migrate akan dieksekusi perubahannya di field pada database.

5. Menurut saya framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah karena mudah dipahami, lengkap, dan langsung bisa menghasilkan aplikasi nyata. Selain itu, saya juga mengerjakannya dengan Pythin dimana bahasa nya lebih mudah dipelajari dibandingkan Java. Saya juga merasa bahwa tidak perlu mengatur banyak hal dari nol dan Django menerapkan struktur proyek terorganisir dengan pola arsitektur Model-View-Template (MVT).
