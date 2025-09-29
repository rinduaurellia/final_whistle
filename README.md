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

5. STEP BY STEP CHECKLIST : 
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
Jadi menurut saya tidak ada yang lebih baik diantara json dan xml, namun json memberikan repsresentasi data yang lebih mudah dibaca oleh manusia, ukuran file nya lebih kecil dibandingkan xml mengakibatkan lebih mudah atau cepat dalam proses pengiriman data. (source : Bu Ara)

JSON lebih populer dibanding XML karena lebih ringan, cepat, dan kemudahannya dalam bekerja. JSON tidak menggunakan struktur tag sehingga membuatnya lebih padat dan mudah dipahami oleh manusia. JSON mempresentasikan data yang sama dalam ukuran file yang lebih kecil untuk transfer data yang lebih cept. Selain itu, XML lebih kompleks dan membutuhkan struktur tag serta rentan terhadap modifikasi dan deklarasi tipe dokumen eksternal yang tidak terstruktu sehingga banyak orang yang meemilih JSON dibanding XML.

3. Fungsi dan Kegunaan is_valid() pada form Django
Method ini akan memeriksa semua data yang dimasukkan oleh pengguna berdasarkan aturan yang ada di dalam form. Meliputi 'apakah field sudah diisi?' 'apakah tipe data sudah sesuai?' 'apakah ada batasan nilai yang dilanggar?'. Selain validasi, fungsi ini juga akan mengonfersi data yang sudah divalidasi dan siap digunakan untuk membuat objek model baru. 

Kita memutuhkan is_valid() untuk mencegah data yang tidak valid, berbahaya, atau tidak lengkap masuk ke database karena jika menyimpan tanpa validasi, data yang salah dapat merusuak database dan logika aplikasi bisa saja menjadi kacau.

4. csrf_token saat membuat Django
csrf_token (Cross-Site Request Forgery token) yang berada di file create_product.html adalah sebuah token unik yang dibuat oleh Django dan ditempatkan dalam form HTML.SRF adalah jenis serangan di mana penyerang memaksa browser pengguna yang sudah terautentikasi untuk mengirimkan permintaan berbahaya ke website yang dipercayai oleh pengguna tersebut. Contohnya, penyerang membuat halaman HTML yang berisi form tersembunyi untuk mentransfer uang, dan halaman tersebut secara otomatis disubmit ketika pengguna mengunjunginya. Jika pengguna tersebut sedang login ke banknya, permintaan tersebut akan dianggap valid oleh server bank.

Django akan menyertakan csrf_token dalam form sebagai input tersembunyi. Ketika form di-submit, Django akan memeriksa form ini dan token hanya diketahui server dan sesi pengguna saat itu. Jika permintaan datang dari web lain, penyerang tidak akan tahu token yang benar karena token tersebut terkat pada sesi pengguna yang sah. Ketika server menerima permintaan POST, ia memvalidasi token yang dikirim. Jika token tidak cocok, permintaan akan ditolak.

Hal tersebut dimanfaatkan oleh penyerang dengan membuat halaman web palsu yang berisi form HTML yang dirancang untuk melakukan operasi sensitif dan berbahaya di platform kita. Form ini dibuat untuk mengirimkan data ke URL halaman palsu ke korban. Ketika korban login ke platform dengan klik URL maka browser secara otomatis mengisi dan mengirimkan form tersebut ke server kita. Server pun akan menganggap permintaan itu valid karena tidak ada csrf_token dan melakukan operasi berbahaya tanpa sepengetahuan developer.

---------No 5 di paling atas------

POSTMAN SCREENSHOOT : https://drive.google.com/drive/folders/11PlRvzNF_tk09rdzFOOIikPw98DJOYeK?usp=sharing


Tidak ada feedback untuk asdos selama tutorial 2, saya sangat merasa terbantu oleh Ka Edzhar yang mau mendemokan langkah - langkah memperbaiki eror pada hari Sabtu pagi (diluar jam kuliah) di discord.

================================================ TUGAS 4 =======================================================

1.  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan Django yang dipakai untuk proses login user dan diimport pada modul : from django.contrib.auth.forms import AuthenticationForm

Secara default, AuthenticationForm memiliki dua field, yaitu : 
a. username --> memastikan username user 
b. password --> memasukkan password user 

Secara otomatis, django akan memvalidasi apakah username terdaftar, mengecek apakah password cocok dan akan memberikan eror jika login gagal. 

Pada kode yang saya buat, method yang menangani login ada di views.py
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

Disini code akan cek apakah username ada di database? dan apakah password cocok dengan username tersebut? Jika iya maka ambil objek user yang berhasil lolos validasi dan menyimpan datanya ke dalam session yang menandakan bahwa user sudah dianggap login.
Setelah berhasil login, user akan diarahkan ke halaman utama (home). 

Dilansir dari https://docs.djangoproject.com/id/5.2/topics/auth/default/ pembuktian keaslian pengguna ada pada 'authenticate()' dimana di belakang layar, Django melihat daftar 'backend pembuktian keaslian' yang dia periksa ketika seseorang login dan mengembalikan objek User jika user memang sah dan terdapat di database.

Kelebihan AuthenticationForm : 
- Sudah build in dari Django, sehingga developer dapat menggunakannya tanpa perlu membuat form login manual, sehingga developer dapat menghemat lebih banyak waktu.
- Keamanan terjamin karena password akan dicek dengan username apakah keduanya cocok atau keduanya ada di dalam database dan validasi otomatis terjadi jika username atay password salah maka akan memberikan error ke form tanpa harus menulis kode untuk validasi.
- Dapat langsung terintegrasi dengan sistem auth Django dan dapat dipakai bersama login(), logout(), loginRequiredMixin dll
- Mudah dikostumisasi yaitu dengan mengoverride AuthenticationForm jika ingin menambah field baru (login dengan email)


Kekurangan AuthenticationForm :
- Hanya memiliki username dan password sebagai default dari Django, sehingga jika ingin login menggunakan email, no telpon, atau metode lain membutuhkan custom code atau ovveride 
- Tampilan sederhana yaitu berupa HTML tanpa styling (label, input, error sederhana) yang mungkin cukup untuk prototipe atau aplikasi internal. Namun kurang fleksibel jika digunakan untuk aplikasi yang sering digunakan publik (seperti sosial media, fintech application)
- Ketika login gagal (password atau username salah) maka error message akan muncul secara default. Namun, user tidak tahu apakah username atau password yang salah karena tidak diberi tahu oleh Django. “Please enter a correct username and password. Note that both fields may be case-sensitive.”
- AuthenticationForm hanya fokus pada username + password login. Banyak fitur login modern yang tidak otomatis tersedia di proyek ini, misalnya : 'Remember me' yaitu ketika pengguna ingin tetap login meskipun browser tertutup, kita harus menambahkan sendiri di kode nya. 

Menurut saya AuthenticationForm ringkas, aman, dan siap pakai. Namun, kelemahannya ada pada tampilan yang sangat sederhana, kurang menarik, dan pesan error sangat kaku. Jika digunakan untuk project kecil mungkin cukup akan tetapi jika digunakan untuk project besar harus kostumisasi atau integrasi dengan library tambahan.


2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi (authentication) adalah proses yang digunakan untuk memastikan identitas seorang pengguna dalam sistem atau proses memastikan identitas pengguna. Dengan kata lain, autentikasi menjawab pertanyaan “siapa kamu?”. Proses ini biasanya dilakukan dengan cara pengguna memasukkan kredensial tertentu, misalnya username dan password, token, kode OTP, atau bahkan login lewat akun pihak ketiga seperti Google atau Facebook. 

Jika kredensial yang dimasukkan cocok dengan yang tersimpan di basis data, maka sistem akan mengenali bahwa pengguna tersebut memang benar-benar pemilik identitas tersebut. Dalam konteks Django, autentikasi diatur melalui framework bawaan django.contrib.auth. Django menyediakan fungsi authenticate() untuk memverifikasi kombinasi username dan password, serta login() untuk menyimpan status autentikasi pengguna di dalam session. Middleware AuthenticationMiddleware secara otomatis menambahkan informasi tentang pengguna ke dalam setiap request melalui request.user. 

Dengan demikian, begitu seorang pengguna berhasil login, Django akan tahu siapa pengguna tersebut dalam setiap interaksi berikutnya.

Sedangkan Otorisasi (authorization) adalah proses yang terjadi setelah autentikasi berhasil. Jika autentikasi memastikan siapa seorang pengguna, maka otorisasi menjawab pertanyaan “apa yang boleh dilakukan oleh pengguna ini?”. 

Otorisasi digunakan untuk mengatur hak akses dan peran di dalam aplikasi. Misalnya, seorang admin boleh menambah atau menghapus produk, tetapi pengguna biasa hanya boleh melihat dan membeli produk. Dalam Django, otorisasi juga diatur oleh django.contrib.auth melalui sistem permission dan group. Django memberikan atribut khusus pada user, seperti is_staff dan is_superuser, serta memungkinkan developer membuat permission kustom untuk model tertentu. 

Untuk penerapannya, Django menyediakan dekorator seperti @login_required untuk memastikan pengguna sudah login, atau @permission_required untuk memastikan pengguna memiliki izin tertentu sebelum bisa mengakses suatu view. Contohnya adalah untuk delete product yang sudah ditambahkan oleh author maka user harus login dengan username yang sama ketika menambahkan produk tersebut, sehingga tidak sembarang orang dapat menghapus produk. Pada level class-based view, Django juga menyediakan LoginRequiredMixin dan PermissionRequiredMixin untuk fungsi serupa.

Autentikasi dan otorisasi adalah dua konsep yang saling melengkapi. Autentifikasi memastikan bahwa identitas pengguna yang dimasukkan sesuai dengan database, sementara otorisasi memastikan hanya pengguna yang sudah dikenali yang dapat mengakses sumber daya sesuai dengan hak yang diberikan. Dalam django, kedua konsep ini telah diimplementasikan secara terintegrasi melalui sisten autentikasi dan otorisasi bawaan yang kuat, sehingga developer tidak perlu membangun sistem keamanan dari nol. 

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Dikutip dari skemadigital.id, session adalah cara bagi situs web untuk menyimpan data pengguna sementara selama pengguna masih aktif di situr tersebut. Data ini disimpan di server dan biasanya akan hilang setelahpengguna menutup browser atau setelah periode tertentu ketika tidak ada lagi aktivitas dalam browser. 

Contohnya seperti ketika login ke localhost maka server akan membuat session yang menyimpan informasi bahwa kita sudah login dan sepanjang melihat detail product atau menambahkan product, maka akan tetap dikenali sebagai pengguna yang sudah login di sesi tersebut.

Kelebihan session : 
- Lebih aman karena langsung disimpan di server dan data penting tidak tersimpan di client, hanya session ID saja
- Fleksibel karena dapat disimpan di database, chace, atau file tergantung kebutuhan.
- Cocok untuk bekerja dengan data sensitif seperti status login atau data sementara.

Kekurangan Session : 
- Membebani server karena semua data session harus disimpan dan dikelola di server, jika terdapat banyak user, maka akan boros memori.
- Membutuhkan manajemen tambahan karena session harus memiliki mekanisme expired atau cleanup agar tidak menupuk di server.
- Ketergantungan cookie atau URL karena session ID biasanya disimpan di cookie, jadi jika cookie dimatikan maka session jadi sulit dipakai 

Sedangkan cookie adalah file kecil yang disimpan di perangat oleh browser untuk menyimpan informasi secara lokal, seperti preferensi bahasa, produk yang pernah dilihat, atau data login yang disimpan. Berbeda dengan session yang menyimpan data di server, cookie menyimpan data di sisi klien (browser), sehingga bisa bertahan meskipun browser ditutup.

Kelebihan cookie : 
- Sederhana kerena langsung disimpan di browser client sehingga tidak membebani server dengan menyimpan banyak data.
- Dpat diset untuk bertahan meskipun browser ditutup (selama belum expired).
- Cocok untuk menyimpan preferensi pengguna (bahasa, tema, keranjang belanja sederhana)
- Mudah digunakan lintas request karena browser otomatis mengirim cookie setiap kali request ke server.

Kekurangan cookie : 
- Rentan keamaan karena tersimpan di client, data dapat dimodifikasi atau dicuri (misalnya serangan XSS).
- Ukuran terbatas biasanya maksimal 4KB cookie
- Terlalu sering dikirim (setiap request ke server akan membawa cookie meski server tidak membutuhkannya).
- Tidak cocok untuk data senditif misalnya password atau informasi pribadi tidak aman jika langsung disimpan di cookie.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default, cookies tidak 100% aman karena mereka disimpan di sisi client browser yang artinya dapat dibaca atau dimodifikasi oleh siapa saja yang memiliki akses ke perangkat atau browser. Cookies juga ikut terkirim di setiap request browser ke server sehingga dapat dicegat di jaringan (man-in-the-middle attact) jika tidak dienkripsi (HTTPS). Cookies juga rentan serangan siber. 

Cookies aman jika dipakai untuk hal - hal yang tidak terlalu sensitif dan sederhana, namun jika hal besar seperti login session atau token autentikasi harus benar - benar dijaga.

Resiko Potensial penggunaan cookies : 
- Session hijacking -> penyerang mencuri session ID di cookie, lalu menyamar jadi user.
- Cookie theft lewat XSS -> script berbahaya di browser bisa membaca isi cookie.
- Manipulasi cookie -> user bisa edit isi cookie karena mereka yang menyimpannya.
- Insecure transmission -> kalau aplikasi masih pakai HTTP, cookie bisa disadap di jaringan publik.

Lalu bagaimana django menangani hal ini? 
Django memiliki beberapa keamanan bawaan untuk mengurangi resiko, seperti : 
- HttpOnly -> dimana django menandai cookies session dengan HttpOnly=True, artinya JavaScript di browser tidak bisa membaca cookie yang berarti lebih aman dari XSS

- Secure -> jika memakai akai HTTPS, kamu bisa aktifkan SESSION_COOKIE_SECURE=True atau CSRF_COOKIE_SECURE=True. Dengan ini, cookies hanya dikirim lewat HTTPS, bukan HTTP.

- CSRF protection -> Django punya middleware CSRF yang pakai cookie khusus (csrftoken). Ini mencegah serangan Cross-Site Request Forgery.

- Session di server, bukan di cookie 
Django tidak menyimpan data user langsung di cookie, hanya session ID. Data asli (misalnya status login, keranjang belanja) disimpan di server/database. Jadi walaupun cookie dicuri, penyerang hanya dapat ID acak, bukan data langsung.

Kesimpulannya adalah cookies tidak sepenuhnya aman karena beragam resiko dapat dihadapi seperti pencurian, manipulasi, atau penyadapan. Namun, django sudah memiliki langkah mitigasi default seperti HttpOnly dan session-based cookies. Jika ingin lebih secure, developer perlu menambahkan setting keamanan ekstra seperti HTTPS + SESSION_COOKIE_SECURE=True, Atur SESSION_COOKIE_SAMESITE='Strict' bila memungkinkan dan gunakan CSRF protection bawaan Django

5. Step by Step implementasi checklist : 

1) Untuk mengimplementasi sesi login - logout, kita harus membuat fungsi registrasi dan form terlebih dahulu dengan mengimport usercreationform dan message pada bagain atas views,py agar memudahkan formulir pendaftaran pengguna dalam aplikasi web, dengan formulir ini pengguna dapat mendaftar dengan mudah di situs web tanpa menulis kode dari awal. 

2) Tambahkan juga fungsi register ke dalam views.py yang bertujuan untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di sumbit di form. formulir register sudah jadi yang terdiri dari username, password, dan password confirmation dengan beberapa ketentuan seperti minimal panjang dan perbedaan password dengan username.

3) Import authenticate dan login pada views.py agar dapat melakukan autentikasi dan login, tambahkan fungsi login_user untuk mengautentikasi pengguna yang login dengan cek apakah pengguna mengirim permintaan login kemudaian validasi. Import fungsi login dan tambahkan di urls.py kemudian tambahkan path url ke dalam urlpatterns.

4) Setelah login berhasil, kita akan membuat fungsi logout dengan menambahkan import logout pada bagian paling atas bersamaan dengan authenticate dan login. Tambahkan fungsi logout_user ke dalam views.py untuk mekanisme logout. Tambahkan button Logout pada main.html, jangan lupa import fungsi logout_user pada urls.py dan tambahkan urlpatterns.

5) Setelah itu, saya mencoba buat dua akun dan password lalu sesuai dengan ketentuan checklist tugas, saya menambahkan 3 buah product pada masing - masing user dan fungsi delete untuk menghapus produk dengan ketentuan yang dapat menghapus produknya adalah user yang menambahkan produk tersebut. 

6) Kita harus menghubungkan setiap object Product dengan pengguna pembuatnya agar hanya pengguna yang sedang login yang dapat melihat product yang ia buat sendiri. Hal pertama adalah import user dan tambahkan 

class Product(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

pada model Product yang berfungsi mengubungkan satu product dengan satu user melalui sebuah relationship dan setiap news dapat terasosiasi dengan user (many-to-one relationship) dengan menambahkan fungsi create_product pada views.py. Hal ini kita manfaatkan untuk mengisi field User dengan nilai request.user, yaitu pengguna yang sedang login sehingga setiap objek yang dibuat akan secara otomatis terhubung dengan pengguna yang membuatnya.

7) Untuk menggunakan data dari cookies kita harus logout terlebih dahulu dari aplikasi Django dan membuka view.py di subdirektori main. Tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas. Ubah bagian login_user untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login. Ubah fungsi logout_user untuk menghapus cookie last_login setelah melakukan logout untuk mengapus last_login dari daftar cookies di reponse. 


================================================ TUGAS 5 =======================================================

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Mengutip dari web Easycoding, urutan prioritas selector CSS (specificity) adalah sebuah nilai atau bobot yang diberikan kepada selektor CSS yang menentukan aturan mana yang lebih kuat atau diprioritaskan dan diterapkan pada elemen HTML. Setiap kali browser menganalisis CSS, ia menghitung nilai specificity dari selector untuk menentukan aturan mana yang berlaku. 

Berikut merupakan urutan prioritas dari yang paling rendah ke yang paling tinggi : 
1) Selector Universal (*) : 
   Adalah selektor yang paling rendah dalam urutan prioritas dan memiliki nilai specificity 0

2) Selektor Elemen dan Pseudo-Elemen : 
   Memiliki bobot rendah seperti div,p, atau h1, dan nilai specifity nya adalah 0,0,1
   Contoh : 
   p {
    color: red;
   }

3) Class, Pseudo-class, dan Attribute Selector: 
   Selector ini seperti .container, :hover, atau [type="text"] memiliki nilai specificity 0, 1, 0.
   Contoh : 
   .menu {
    background-color: blue;
   }

4) ID Selector (#header atau #footer) : 
   ID memiliki bobot yang lebih tinggi dibandingkan class dan elemen. Selector seperti #header memiliki nilai specificity 1, 0, 0.
   Contoh : 
   #header {
    font-size: 20px;
   }

5) Inline Styles: 
   Jika Anda memberikan style langsung pada elemen melalui atribut style, seperti <h1 style="color: red;">, nilai specificity-nya adalah 1, 0, 0, 0.
   Contoh : <div style="color: green;">Text</div>

Namun dibalik itu semua, !important pada aturan CSS akan mengesampingkan semua aturan lain kecuali inline syyles.

Specificity dapat dihitung dengan empat angka yang dipisahkan oleh koma : (a, b, c, d) dari paling tinggi prioritas -> rendah
(Inline styles; ID Selectors ; Jumlah class selectors; attribute selectors, pseudo-classes; Element selectors dan pseudo-elements)

Contoh : 
#header .menu-item a:hover {
  color: blue;
}

Selector diatas memiliki nilai specificity (0, 1, 2, 1)
Ada 1 ID selector (#header)
Ada 2 class/pseudi-class selector (.menu-item dan :hover)
Ada 1 elemen selector (a)

Contoh HTML : 
<h1 id="header" class="title">Judul Utama</h1>

CSS : 
h1 {
  color: green;
}

#header {
  color: red;
}

.title {
  color: blue;
}

Lalu mana yang diterapkan duluan?
Specificity dari tiap selektor : 
- h1: Selector ini adalah element selector, sehingga specificity-nya adalah (0, 0, 0, 1).
- #header: Selector ini adalah ID selector, sehingga specificity-nya adalah (0, 1, 0, 0).
- .title: Selector ini adalah class selector, sehingga specificity-nya adalah (0, 0, 1, 0).

CSS akan membaca dari atas ke bawah maka kode akan menerapkan h1 terlebih dahulu yaitu warna hijau. Namun, keika eksekusi #header maka warna akan terganti menjadi warna merah karena prioritas ID selecor lebih tinggi dibanding element selector. Meskipun ditulis terakhir, .title specificity-nya lebih rendah dibandinh #header, sehingga tidak merubah warna ketika #header diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Dilansir dari laporan Marktingdive, sejumlah 53% pengguna intenet ternyata banyak yang memilih untuk meninggalkan website apabila loading-nya terlalu lama. Hal tersebut dikarenakan oleh design website yang dimiliki tidak responsif.

Dikutip dari codingstudio.id, Fungsi responsive design website adalah untuk membuat tampilan website bisa menyesuaikan diri pada masing - masing ukuran layar pada pengunjung web. Berbagai tampilan yang disesuaikan diantaranya dari segi tampilan UI, ukuran huruf, hingga tata letak disesuaikan dengan ukuran layar pengguna dan resolusi perangkat yang digunakan.

Mengapa Responsive Design penting? 
a. Pengalaman Pengguna (UX) yang ditingkatkan 
Website yang menyediakan pengalaman konsisten dan nyaman bagi pengguna akan meningkatkan waktu pemakaian user terlepas dari perangkat yang mereka gunakan. 

b. Penggunaan beragam perangkat 
Pengguna saat ini mengakses aplikasi web menggunakan berbagai jenis perangkat, mulai dari desktop, laptop, tablet, hingga smartphone. Dengan semakin banyaknya pengguna mobile, situs yang tidak dioptimalkan untuk tampilan layar kecil atau besar akan memberikan pengalaman pengguna yang buruk.

c. Mengurangi Biaya Pemeliharaan 
Dengan membuat satu desain yang responsif, developer tidak perlu lagi unruk membuat dan memelihara versi terpisah dari situs untuk deskop dan versi mobile atau seluler. Hal ini dapat mengurangi biaya dan waktu pemeliharaan.

d. Search Engine Optimization (SEO) meningkat 
Perlu diketahui bahwa tampilan website yang responsif ternyata dapat mempengaruhi peringkat di mesin pencarian. Maka dari itu dengan menggunakan desain web responsif , visibilitas website akan meningkat pada hasil pencarian karena hanya perlu mengelola satu URL dan satu konten.

Contoh aplikasi yang sudah menerapkan responsive design : 
1) AMAZON 
Seperti yang kita ketahui, amazon memiliki basis pengguna global yang sangat besar, menjadi kewajiban bagi mereka memastikan bahwa pengalaman belanja tetap nyaman dan aman di berbagai perangkat (deskop amupun mobile) sangat penting untuk meningkatkan konversi dan penjualan.

Ketika pengguna mengakses Amazon menggunakan ponsel atau tablet, situs menyesuaikan tampilannya dengan ukuran layar perangkat tersebut, memungkinkan pengguna untuk belanja dengan mudah melalui perangkat mobile atau desktop.

2) Instagram
Instagram merupakan platform sosial yang digunakan oleh hampir seluruh masyarakat di dunia dan berbasis gambar, jadi desain responsif memungkinkan gambar dan konten ditampilkan secara optimal pada berbagai ukuran layar, memaksimalkan kualitas visual dan interaksi pengguna.

Instagram juga menerapkan desain responsif pada situs web mereka. Pengguna dapat mengakses Instagram baik melalui aplikasi seluler atau melalui browser web, dengan desain yang konsisten dan pengalaman pengguna yang tetap optimal.

3) BCC News 
BCC News menawarkan website berita internasional yang sudah pasti sering dikunjungi oleh berbagai pengguna. Karena pengguna sering mengakses berita di ponsel mereka, situs web yang responsif memastikan bahwa berita dan konten tetap dapat diakses dengan cepat dan nyaman di berbagai perangkat.

Situs web berita seperti BBC News memiliki desain responsif, memastikan bahwa artikel dapat dibaca dengan mudah pada perangkat kecil seperti ponsel atau tablet, tanpa memerlukan zoom atau pengguliran horizontal.

Contoh aplikasi yang belum menerapkan responsive design : 

1) https://www.papua.go.id/#
Ketika mengakses website dengan menggunakan latop, beberapa fungsi terload dengan baik. Namun ketika membuka web dengan handphone atau mobile, tidak ada satupun fungsi yang terdefinisi dengan baik mengakibatkan saya tidak dapat melihat berita yang memang harusnya tersedia.

2) https://www.bukalapak.com
Ketika mengakses aplikasi, fungsi e-commerce terdefinisi dengan baik dan tampilannya juga sesuai dengan bentuk mobile. Namun ketika mengakses web nya, web akan menampilkan aplikasi dengan mode mobile, padahal harusnya tidak (tampilkan dalam bentuk web). Inailah yang menjadi dasar mengapa bukalapak belum menerapkan responsive design antara web dan aplikasi.


3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

1) Margin adalah ruang luar (di luar border) yang memisahkan suatu elemen dengan elemen lainnya. Margin bertugas mengontrol jarak antara elemen dan elemen lainnya di dalam halaman web baik elemen dalam satu baris (horizontal) maupun dalam satu kolom (vertikal).

Contoh (CSS): 
margin: 10px;  -> Memberikan jarak 10px pada semua sisi 
margin-top: 20px;  -> Memberikan jarak 20px pada sisi atas 
margin-right: 15px;  -> Memberikan jarak 15px pada sisi kanan 
margin-bottom: 20px;  -> Memberikan jarak 20px pada sisi bawah 
margin-left: 10px;  -> Memberikan jarak 10px pada sisi kiri

2) Border 
Definisi: Border adalah garis yang mengelilingi elemen di sekitar padding dan di dalam margin. Border memisahkan elemen dengan ruang sekitarnya, dan digunakan untuk memberikan garis pembatas atau batas visual pada elemen misalnya untuk tombol, kotak input, gambar, dan lainnya.

Contoh (CSS): 
border: 2px solid black;  -> Garis border 2px, tipe solid, warna hitam 
border-top: 3px dotted red;  -> Border atas dengan tipe dotted dan warna merah 
border-right: 1px solid green;  -> Border kanan dengan tipe solid dan warna hijau 
border-bottom: 4px dashed blue;  -> Border bawah dengan tipe dashed dan warna biru 
border-left: 2px solid yellow;  -> Border kiri dengan tipe solid dan warna kuning 

3) Padding 
Padding adalah ruang dalam (di dalam border) yang memisahkan konten (misalnya teks, gambar) dari border elemen. Padding memberikan ruang antara konten dengan batas elemen. Biasanya digunakan untuk mnambah ruang di dalam elemen agar konten tidak terlalu rapat dengan border.

Contoh (CSS) : 
padding: 10px;  -> Memberikan ruang 10px pada semua sisi 
padding-top: 20px;  -> Memberikan ruang 20px pada sisi atas 
padding-right: 15px;  -> Memberikan ruang 15px pada sisi kanan 
padding-bottom: 20px;  -> Memberikan ruang 20px pada sisi bawah 
padding-left: 10px;  -> Memberikan ruang 10px pada sisi kiri 

Contoh : 

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Margin, Border, dan Padding</title>
    <style>
        /* CSS untuk elemen div */
        .box {
            margin: 30px;         /* Jarak luar (antar elemen) */
            padding: 20px;        /* Jarak dalam (antara border dan konten) */
            border: 5px solid blue;  /* Border dengan ketebalan 5px dan warna biru */
            background-color: #f0f0f0; /* Memberikan latar belakang abu-abu terang */
        }
    </style>
</head>
<body>

    <div class="box">
        elemen margin, padding, dan border.
    </div>

</body>
</html>

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Dilansir dari rumahweb, Flex box adalah sebuah sistem CSS yang berfungsi untuk menyederhanakan tata letak tampilan website, dimana dapat mengatur element secara responsif baik dalam arah horizonal maupun vertikal tanpa perlu menggunakan tata letak tradisional yang lebih kompleks. Flexbox sangat berguna untuk membuat tata letak tampilan website yang dinamis, seperti menyamakan elemen di tengah, membagi ruang secara proporsional, atau mengatur elemen dengan ukuran berbeda agar tetap seimbang di berbagai perangkat.

Fungsi CSS Flex Box : 
- Mengatur elemen secara horizontal atau vertikal
- Membuat elemen responsif
- Membagi elemen dengan mudah
- Mengatur urutan elemen

Dasar Penggunaan CSS Flexbox : 
1) Layout
Untuk menggunakan Flexbox layout, kita harus membuat sebuah container dengan property : display dan menggunakan nilai / value flex.

Contoh : 
.container {
  display: flex;
}

2) Container 
Setelah membuat sebuah elemen kontainer menggunakan properti display:flex, maka secara otomatis layout pada kontainer tersebut akan menggunakan layout flexbox container, sehingga kita dapat menggunakan beberapa properti lain yang digunakan oleh layout flexbox.

3) Flex Items 
Properti Flex Item : 
- display : menggunakan nilai dan value
.container {
  display: flex;
}

- flex-direction : dapat menentukan arah yang akan menampilkan elemen yang ada di dalam container flexbox. Arah tersebut dapat mengarah berbaris atau horizontal (dari kiri ke kanan atau sebaliknya), atau seperti kolom/vertikal (dari atas kebawah atau sebaliknya)
.container {
  display: flex;
  flex-direction: column;
}

- justify-content :  digunakan untuk menentukan elemen agar sejajar di antara elemen secara horizontal
.container {
  display: flex;
  justify-content:center ;
}

- align-content : digunakan untuk menentukan elemen di dalam kontainer agar sejajar di antara elemen secara vertikal.
.container {
  display: flex;
  align-content: center;
}

- align-items : menentukan elemen di dalam kontainer agar sejajar di antara elemen secara horizontal
.container {
  display: flex;
  align-items: center;
}

- order : mengubah urutan elemen di dalam kontainer flex. Anda dapat mengurutkan dari awal hingga akhir atau dari atas ke bawah (flex-direction:column) atau dari kiri ke kanan (flex-direction:row).
.container {
  display: flex;
  flex-direction: row;
}

Dikutip dari https://www.barajacoding.or.id/apa-itu-grid-layout-untuk-programing/, Grid Layout CSS adalah modul CSS yang memungkinkan pengembangan web untuk membuat atat letak halaman secara lebih fleksibel dan kuat dibandingkan dengan metode tata letak tradisional seperti float atau positioning. Grid laytout memungkinkan pembuatan grid fua dimensi yang terdiri dari baris (rows) dan kolom (coloumns), dimana elemen - elemen HTML dapat ditempatkan dengan tepat di dalamnya.

Fitur Utama Grid Layout CSS : 
1) Grid Container 
Elemen yang menggunakan properti display: grid; atau inline-grid; menjadi grid container, yang memulai konteks grid untuk inheritence nya.

2) Grid Items 
Inheritence atau anak - anak dari grid container yang ditempatkan di dalam sel grid.

3) Grid Lines 
Garis-garis vertikal dan horizontal yang membagi grid menjadi baris dan kolom.

4) Grid Tracks
Area antara dua garis grid bersebelahan, bisa berupa baris atau kolom.

5) Grid Cells
Area persegi atau persegi panjang yang dibentuk oleh dua garis grid yang berpotongan.

6) Grid Areas
Area yang diberi nama di dalam grid, memungkinkan gruping dari beberapa sel menjadi satu area yang lebih besar.

Keunggulan Grid Layout CSS : 
- Responsif :
Memungkinkan pengembang untuk membuat tata letak responsif dengan mudah, mengatur ulang ukuran dan posisi elemen-elemen sesuai dengan perubahan ukuran layar atau perangkat.

- Fleksibilitas tinggi : 
Menyediakan kontrol yang lebih besar terhadap tata letak halaman, dengan kemampuan untuk menentukan dimensi relatif, posisi, dan tata letak elemen secara tepat.

- Peningkatan Kinerja :
Dibandingkan dengan teknik tata letak tradisional seperti float atau positioning, Grid Layout cenderung lebih efisien dalam hal kinerja karena memungkinkan browser untuk mengoptimalkan render secara lebih baik.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1) Hal pertama yang dilakukan adalah menambah tailwind ke Aplikasi untuk mempermudah pengembangan UI dengan menggunakan kelas utility yang akan diterapkan langsung ke HTML.

2) Tambahkan fitur edit news ke aplikasi final whistle pada views.py yaitu edit product yang dimana hanya user yang add product tersebut yang dapat mengedit detail product. Jangan lupa untuk membuat tampilan utama atau berkas html nya dan rooting ke urls.py serta urls patterns. Tambahkan looping untuk pengeditan produk pada main.html nya.

3) Tambahkan juga function untuk menghapus produk namun hanya user yang terautorisasi yang bisa menghapus data produk serta lakukan rooting ke urls dan path ke dalam url patterns. Jangan lupa untuk menambahkan button dan tampilan delete product ke dalma main html.

4) Tambahkan navigation bar pada aplikasi yang akan ditempatkan di bagian atas halaman berisi tombol atau tautan ke halaman - halaman dalam aplikasi. Pada kali ini, saya membuat navigation bar hot product dan create product. Hot product akan memfilter product yang telah dilihat lebih dari 50 kali. Jangan lupa untuk membuat html nya agar navbar dapat terlihat di dalam web final whistle.

5) Tambahkan middleware whiteNoise pada settings.py agar secara otomatis Django dapat mengelola file statis secara otomatis dalam mode produksi (DEBUG=False) tanpa perlu konfigurasi yang kompleks. Hal ini berguna agar file statis tersebut dapat diakses di deployment.

6) Hubungkan global.css dan script Tailwind ke base.html agar dapat mengatur tampilan form yang memiliki class form-style. Kode CSS akan membuat semua input memiliki lebar penuh, padding, border, dan sudut yang melengkung. Namun, saya menambahkan beberapa perubahan seperti warna pada halaman registrasi, utama, dan detail produk.

7) Styling halaman navigation bar, login, register, home, edit produk, create new product dengan kode html yang telah dibuat. Tambahkan direktori static dan buat file image, masukkan image png dan drag. Kemudian modifikasi main.html sehingga dapat menampilkan thumbnail dengan foto yang sudah diinput.