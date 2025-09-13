========================================== TUGAS 2 ==============================================
1. Langkah mengimplementasi Checklist tugas : 
1) Untuk membuat sebuah proyek Django baru, pertama saya membuat new repository di github sesuai dengan nama aplikasi yang saya gunakan yaitu 'Final Whistle', kemudian saya membuat direktori lokal baru dan membuat virtual environtment di dalamnya yang berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain kemudian aktifkan.

2) Langkah kedua adalah menyiapkan dependencies (library, framework, package) dan lakukan instalasi terhadap dependencies yang ada kemudian buat proyek Django. Hal ini berguna untuk memanfaatkan kode yang ada, dan melakukan manajemen agar kompatibilitas versinya tepat. Dalam direktori finalwhistle saya membuat file requirements.txt dan mendambahan dependencies yang akan diinstal untuk proyek django.

3) Buat environtment variables yang disimpan di luar kode program dan digunakan untuk menyimpan informasi kredensial database tanpa perlu mengubah kode. Kemudian saya masukkan DB_NAME, HOST dan lainnya sesuai dengan variabel yang telah diberikan. Kemudian, tambahkan ALLOWED_HOST dengan DB_NAME atau host yang diperbolehkan untuk mengubah kode.

4) Migrasi databse untuk menyinkronkan kode model di Django dengan struktur database tanpa harus ubah secara manual. Kemudian jalankan server Django dan ketika peramban web sudah berfungsi (http://localhost:8000), nonaktifkan server kemudian push ke github.

5) Setelah itu saya membuat akun dan delpoyment melalui PWS (Pacil Web Service), login dengan akun SSO UI, create new project dan isi Project Name kemudian simpan credentials dan edit Raw Editor  dan tambahkan URL deployment PWS pada ALLOWED_HOST. Masukkan Username & Password kemudian running project.

6) Untuk membuat aplikasi main dalam proyek 'Final Whistle' saya akan menjalankan 'python manage.py startapp main' dan mendaftarkan aplikasi main ke proyek (settings.py). main tersebut saya ubah variabel nya dengan ketentuan yang sudah diberikan (name, price, description, dll).

7) Setelah template (html file) dimodifikasi berupa nama aplikai, npm, dan kelas, saya memetakan suatu URL ke sebuah fungsi view yang sudah didefinisikan (routing) dengan menambahkan view di views.py Semua rute dari aplikasi main juga harus dapat diakses langsung lewat http://localhost:8000/.

8) Tidak lupa juga melakukan deployment ke PWS dengan membuat project baru bernama 'finalwhistle' kemudian ubah beberapa hal seperti SCHEMA dan production. Kemudian push ke github dan periksa secara berkala mengenai proses deployment ini apakah sudah sukses pada server Django.


2. BAGAN REQUEST CLIENT KE WEB : 
https://drive.google.com/file/d/1-2-GJIkhWIBaRN_kEZFXjAURWHp1IzPW/view?usp=sharing

Hal pertama adalah client request ke internet dan request tersebut akan diterima oleh Django kemudian argumen atau request tersebut diterima oleh views.py. Views akan melihat argumen tersebut meminta apa atau tipe data apa. Jika argumen meminta informasi yang ada di database (seperti informasi pembuatan dan berakhir project) maka ia harus meneruskan ke bagian models.py

Models.py akan meneruskan permintaan client ke database dan mencari data yang diminta karena hanya models.py yang memiliki hak untuk mengatur pengambilan data bukan menyimpan. Setelah data diambil, models.py akan meneruskan ke views.py kemudian meneruskan ke index.html untuk membuat template kodenya dan diteruskan ke Django. Setelah itu informasi akan diteruskan ke client melalui internet.

3. Peran settings.py dalam proyek Django adalah sebagai pusat konfigurasi utama proyek agar bisa berjalan sesuai dengan keinginan, baik saat developemnt maupun production. Settings.py yang berisi pengaturan untuk proyek Django seperti menentukan konfigusari proyek, mengatur aplikasi yang aktif dijalankan, mengatur keamanan dan respons proyek, mengatur URL dan template, dan masih banyak lagi.

4. Cara kerja migrasi database di Django : 
Migrasi database bekerja dengan cara menyingkronkan model Python dengan struktur database yang sudah ada. Ketika mengubah model di models.py, Django akan mendeteksi perubahan dan melakukan file migration dengan prompt 'python manage.py migrate' yang berisi instruksi perubahan database. File yang di migrate akan dieksekusi perubahannya di field pada database.

5. Menurut saya framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah karena mudah dipahami, lengkap, dan langsung bisa menghasilkan aplikasi nyata. Selain itu, saya juga mengerjakannya dengan Pythin dimana bahasa nya lebih mudah dipelajari dibandingkan Java. Saya juga merasa bahwa tidak perlu mengatur banyak hal dari nol dan Django menerapkan struktur proyek terorganisir dengan pola arsitektur Model-View-Template (MVT).

================================================ TUGAS 3 =======================================================

STEP BY STEP CHECKLIST : 
Sebelum membuat form, kita harus membuat skeleton yang berfungsi sebagai kerangka views situs web. Pada tugas kali ini, ada 4 fungsi yang ditambahkan pada file views.py untuk menampilkan objek yang sudah ada dalam format XML dan JSON, baik untuk esmua objek maupun berdasarkan ID. Fungsi - fungsi ini mengambil objek dari model seperti produk sepatu pada web saya dan mengonfersinya menjadi formal XML atau JSON.

Selanjutnya jangan lupa untuk membuat rooting URL untuk masing - masing views (XML, JSON, XML by ID, JSON by ID) pada variabel urlpattern untuk menentukan bagaimana permintaan URL dari pengguna dipresentasikan ke file views di dalam aplikasi. Ketika pengguna mengakses https produk, Django akan melihat file urls.py untuk menentukan pola yang cocok dengan produk tersebut. Kemudian django akan memanggil fungsi view yang telah ditautkan ke rute tersebut. Tanpa urls.py, Django tidak bisa mengetahui fungsi mana yang harus dijalankan untu URL tertentu. Oleh karena itu, hal ini sangat diperlukan

Setelah membuat rooting URL unruk masing - masing views, di main.html saya menambahkan 'add product' yang kemudian akan redirect ke halaman form untuk menambah produk dengan variabel - variabel yang sudah ditentukan seperti nama produk, deksripsi, kategori. Setelah di build, produk dapat dilihat pada main web (halaman utama) serta ada tombol 'detail' yang ditulis pada file product_detail.html untuk melihat deksripsi produk lebih lanjut. 

Selanjutnya adalah membuat halaman form untuk menambahkan objek model sebagai jembatan antara pengguna dan database aplikasi. Seperti fungsi 'show_main' untuk mengambil objek product yang tersimpan pada database, 'create_product' untuk menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data di-submit dari form. Tanpa form, tidak ada cara bagi pengguna untuk berinteraksi dan mengirimkan data baru ke aplikasi. Form juga memiliki peran dalam memastikan integritas dan kevalidan data sebelum disimpan ke database, seperti field wajib diisi, tipe data benar, serta panjang karakter juga memiliki batasan dan diatur oleh kode di form. Form juga memberikan feedback fisual bagi pengguna.

Halaman detail dibuat pada file product_detail dengan menyambungkan apa saja yang sudah ditulis di models.py dan menambahkannya di detail produk. Agar ketika user klik 'detail' maka akan langsung ditujukan ke halaman yang menampilkan detail dari produk.

1. DATA DELIVERY
Data delivery adalah proses mentransfer data dari satu sistem ke sistem lain untuk berinteraksi dengan pengguna atau sistem lain yang ada di project tersebut. Interaksi tersebut meliputi : 

1) Interaksi Client : Data delivery sebagai mekanisme utama yang memungkinkan klien (web) untuk mengirim permintaam ke sever (mengambil data atau menyimpan informasi) dan menerima respons (data yang dimita seperti produk). Tanpa data delivery, komunikasi antar web dan client tidak dapat terjadi. 

2) Integrasi Sistem : Data delivery memungkinkan pertukaran informasi antara platdorm dengan layanan lain (penunjang) seperti API pihak ketiga (pembayaran, map, atau media sosial)

3) Skalabilitas dan Keterbukaan : Dengan menggunakan format data standar (seperti JSON atau XML) yang dapat dipahami oleh berbagai bahasa dan platform, data delivery memungkinkan platform diakses oleh berbagai jenis perangkat.

2. JSON VS XML
Dikutip dari aws.amazon.com , JSON dan XML adalah representasi data yang digunakan dalam pertukaran data antaraplikasi. JSON adalah format pertukaran data yang terbuka dan dpaat dibaca oleh manusia dan mesin. JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. Sedangkan XML adalah bahasa markup yang menyediakan aturan untuk menentukan data apapun. XML menggunakan tanda untuk membedakan antara arribut data dan data aktual.

JSON lebih populer dibanding XML karena lebih ringan, cepat, dan kemudahannya dalam bekerja. JSON tidak menggunakan struktur tag sehingga membuatnya lebih padat dan mudah dipahami oleh manusia. JSON mempresentasikan data yang sama dalam ukuran file yang lebih kecil untuk transfer data yang lebih cept. Selain itu, XML lebih kompleks dan membutuhkan struktur tag serta rentan terhadap modifikasi dan deklarasi tipe dokumen eksternal yang tidak terstruktu sehingga banyak orang yang meemilih JSON dibanding XML.

3. Fungsi dan Kegunaan is_valid() pada form Django
Method ini akan memeriksa semua data yang dimasukkan oleh pengguna berdasarkan aturan yang ada di dalam form. Meliputi 'apakah field sudah diisi?' 'apakah tipe data sudah sesuai?' 'apakah ada batasan nilai yang dilanggar?'. Selain validasi, fungsi ini juga akan mengonfersi data yang sudah divalidasi dan siap digunakan untuk membuat objek model baru. 

Kita memutuhkan is_valid() untuk mencegah data yang tidak valid, berbahaya, atau tidak lengkap masuk ke database karena jika menyimpan tanpa validasi, data yang salah dapat merusuak database dan logika aplikasi bisa saja menjadi kacau.

4. csrf_token saat membuat Django
csrf_token (Cross-Site Request Forgery token) yang berada di file create_product.html adalah sebuah token unik yang dibuat oleh Django dan ditempatkan dalam form HTML.SRF adalah jenis serangan di mana penyerang memaksa browser pengguna yang sudah terautentikasi untuk mengirimkan permintaan berbahaya ke website yang dipercayai oleh pengguna tersebut. Contohnya, penyerang membuat halaman HTML yang berisi form tersembunyi untuk mentransfer uang, dan halaman tersebut secara otomatis disubmit ketika pengguna mengunjunginya. Jika pengguna tersebut sedang login ke banknya, permintaan tersebut akan dianggap valid oleh server bank.

Django akan menyertakan csrf_token dalam form sebagai input tersembunyi. Ketika form di-submit, Django akan memeriksa form ini dan token hanya diketahui server dan sesi pengguna saat itu. Jika permintaan datang dari web lain, penyerang tidak akan tahu token yang benar karena token tersebut terkat pada sesi pengguna yang sah. Ketika server menerima permintaan POST, ia memvalidasi token yang dikirim. Jika token tidak cocok, permintaan akan ditolak.

Hal tersebut dimanfaatkan oleh penyerang dengan membuat halaman web palsu yang berisi form HTML yang dirancang untuk melakukan operasi sensitif dan berbahaya di platform kita. Form ini dibuat untuk mengirimkan data ke URL halaman palsu ke korban. Ketika korban login ke platform dengan klik URL maka browser secara otomatis mengisi dan mengirimkan form tersebut ke server kita. Server pun akan menganggap permintaan itu valid karena tidak ada csrf_token dan melakukan operasi berbahaya tanpa sepengetahuan developer.

