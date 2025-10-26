# PA-06-SISTEM-MANAJEMEN-LAUNDRY
Project Akhir Kelompok 06 - Sistem Informasi B'2025
- Noor Hamsyah Pratama (2509116046)
- Atha Rina Sarwahita (2509116047)
- Vidya Khansa Mizan (2509116052)

# FLOWCHART
<img width="7610" height="2472" alt="PA (6) DDP  drawio" src="https://github.com/user-attachments/assets/1a4bc29f-e96d-43a0-81ea-023878d47ec5" />

🔐 _**Login dan Sign Up Flowchart**\

Flowchart ini menggambarkan alur proses pengguna dalam melakukan Login atau Sign Up pada sistem.

🏠 1. Menampilkan Halaman Utama


❓ 2. Apakah Pengguna Sudah Memiliki Akun?
Jika Sudah → Pengguna diarahkan ke proses Login.
Jika Belum → Pengguna diarahkan ke proses Sign Up.

📝 3. Proses Sign Up
        1. Menampilkan halaman Sign Up.
        2. Pengguna memasukkan username.
        3. Pengguna memasukkan password.
        4. Data pengguna kemudian disimpan ke database.
        5. Setelah pendaftaran berhasil, pengguna akan diarahkan ke halaman Login.

🔑 4. Proses Login
        1. Menampilkan halaman Login.
        2. Pengguna memiliki 3 kali kesempatan untuk login.
        3. Pengguna memasukkan username.
        4. Pengguna memasukkan password.
        5. Sistem akan memverifikasi kecocokan username dan password dengan data di database.

⚙️ 5. Verifikasi Login
        1. Jika tidak sesuai:
        Pengguna diminta untuk mencoba kembali.
        Kesempatan login akan berkurang satu setiap kali gagal.
        Jika kesempatan sudah habis, sistem akan mengeluarkan pengguna secara otomatis.
        2. Jika sesuai:
        Pengguna akan diarahkan ke menu berdasarkan role masing-masing:
                👨‍💼 Admin → Menu Admin
                👤 Customer → Menu Customer



        
-**Menu Admin**\
Flowchart ini menggambarkan alur kerja sistem Menu Admin dalam sebuah aplikasi layanan (kemungkinan sistem pemesanan atau manajemen layanan).



-**Menu Customer**\
Flowchart customer ini menjelaskan alur dari menu customer yang ada di dalam program ini. Yaitu sebagai berikut:
1. Menampilkan halaman menu utama customer, dan menampilkan pilihan menu mana yang akan diakses oleh customer.
2. Lihat daftar produk/layanan
3. Pesan layanan
4. Lihat Saldo
5. Top Up Saldo
6. Keluar


