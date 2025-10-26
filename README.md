# PA-06-SISTEM-MANAJEMEN-LAUNDRY
Project Akhir Kelompok 06 - Sistem Informasi B'2025
- Noor Hamsyah Pratama (2509116046)
- Atha Rina Sarwahita (2509116047)
- Vidya Khansa Mizan (2509116052)

# FLOWCHART
<img width="7610" height="2472" alt="PA (6) DDP  drawio" src="https://github.com/user-attachments/assets/1a4bc29f-e96d-43a0-81ea-023878d47ec5" />

- **LOG IN DAN SIGN UP**\
Flowchart ini menjelaskan alur proses pengguna dalam melakukan login atau sign up:
1. Menampilkan halaman utama
2. Apakah pengguna sudah memiliki akun?
   - Jika Sudah, pengguna diarahkan ke proses log in
   - Jika Belum, pengguna diarahkan ke proses sign up
3. > Proses Sign Up
     1. Menampilkan halaman Sign Up
     2. Pengguna memasukkan username
     3. pengguna memasukkan password
     4. kemudian data pengguna di simpan di database
     5. setelah sign up berhasil, kemudian di arahkan ke halaman log in

   > Proses Log in
     1. Menampilkan halaman log in
     (PENGGUNA MEMILIKI 3 KALI KESEMPATAN UNTUK LOG IN)
     2. Pengguna Memasukkan Username
     3. Pengguna Memasukkan Password
     4. Sistem Memverifikasi apakah username dan password sesuai dengan di database

 4. Apakah username dan password sesuai?
    - Jika tidak sesuai, pengguna diarahkan untuk mencoba log in kembali dan kesempatan mencoba berkurang satu  (ketika kesempatan mencoba sudah habis, maka akan langsung keluar)
    - Jika sesuai, pengguna di arahakan ke menu sesuai role masing masing. jika role admin maka akan diarahkan ke menu admin, lalu jika rolenya customer akan di arakan ke menu customer
        
