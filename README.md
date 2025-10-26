# PA-06-SISTEM-MANAJEMEN-LAUNDRY
Project Akhir Kelompok 06 - Sistem Informasi B'2025
- Noor Hamsyah Pratama (2509116046)
- Atha Rina Sarwahita (2509116047)
- Vidya Khansa Mizan (2509116052)

# FLOWCHART
<img width="7610" height="2472" alt="PA (6) DDP  drawio" src="https://github.com/user-attachments/assets/1a4bc29f-e96d-43a0-81ea-023878d47ec5" />

# 🔐 Login dan Sign Up Flowchart

Flowchart ini menggambarkan alur proses pengguna dalam melakukan Login atau **Sign Up pada sistem ini.

---

## 🏠 1. Menampilkan Halaman Utama
Pengguna akan diarahkan ke halaman utama.

---

## ❓ 2. Apakah Pengguna Sudah Memiliki Akun?
- Jika Sudah, Pengguna diarahkan ke proses Login.  
- Jika Belum, Pengguna diarahkan ke proses Sign Up.

---

## 📝 3. Proses Sign Up
1. Menampilkan halaman Sign Up.  
2. Pengguna memasukkan username, minimal 3 karakter.  
3. Pengguna memasukkan password, minimal 3 karakter.
4. Jika pengguna menginput username dan password kurang dari 3 karakter, maka akan diarahkan untuk mengisi username dan password ulang  
5. Data pengguna kemudian disimpan ke "datauseradmin.json".  
6. Setelah pendaftaran berhasil, pengguna akan diarahkan ke halaman Login.

---

## 🔑 4. Proses Login
1. Menampilkan halaman Login.  
2. Pengguna memiliki 3 kali kesempatan untuk login.  
3. Pengguna memasukkan username.  
4. Pengguna memasukkan password.  
5. Sistem akan memverifikasi kecocokan username dan password dengan data di "datauseradmin.json".

---

## ⚙️ 5. Verifikasi Login
- Jika tidak sesuai:
  - Pengguna diminta untuk mencoba kembali.  
  - Kesempatan login akan berkurang satu setiap kali gagal.  
  - Jika kesempatan sudah habis, sistem akan mengeluarkan pengguna secara otomatis.  

- Jika sesuai:  
  Pengguna akan diarahkan ke menu berdasarkan role masing-masing:
  - 👨‍💼 Admin ke Menu Admin  
  - 👤 Customer ke Menu Customer  

---





        
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


# SIGN-UP DAN LOG-IN
ketika program mulai dijalankan, maka kita akan masuk ke halaman utama. Pada halaman utama ini kita Washy (sistem) akan menanyakana apakah kamu sudah memiliki akun atau belum, seperti pada gambar di bawah ini.
<img width="686" height="199" alt="Screenshot 2025-10-26 170026" src="https://github.com/user-attachments/assets/4c22f296-34b0-48b9-9b7b-c9e0e5916b98" />


- **SIGN UP**\
Jika kamu menjawab "no" maka Washy akan bertanya lagi apakah kamu ingin membuat akun atau tidak.
<img width="678" height="263" alt="Screenshot 2025-10-26 170206" src="https://github.com/user-attachments/assets/213dca4c-84ac-4d52-9716-0c176e4b2e13" />


-> jika kamu menjawab "yes" pada pertanyaan yang ke-dua, maka kamu akan dialihkan ke halaman Sign-Up, seperti pada gambar di bawah.
<img width="695" height="324" alt="Screenshot 2025-10-26 165657" src="https://github.com/user-attachments/assets/3dacbd39-533a-4eff-ad6a-e1343c7daa5e" />


pada halaman Sign-Up kita akan diminta untuk mengisi Username dan Password yang kita inginkan, dengan syarat Username dan Password ini harus memiliki minimal 3 karakter. Jika input username dan password memenuhi syarat tersebut, maka akun dinyatakan berhasil terdaftar ke database dan dialihkan ke halaman Log-in.\
<img width="687" height="156" alt="Screenshot 2025-10-26 171208" src="https://github.com/user-attachments/assets/905d39bf-1e8b-4ed3-b351-e44b94c345e0" />


Namun jika username dan password yang anda masukkan ternyata sudah terdaftar di database, maka akan muncul output yang berisikan bahwa akun sudah digunakan dan Washy akan kembali ke input Username.\
<img width="708" height="271" alt="Screenshot 2025-10-26 171910" src="https://github.com/user-attachments/assets/5ebcb2ad-4ed3-474b-929e-8fef02512786" />


-> jika kamu menjawab "no" pada pertanyaan yang ke-dua, maka kamu akan keluar dari program ini, seperti pada gambar di bawah.
<img width="674" height="286" alt="Screenshot 2025-10-26 165124" src="https://github.com/user-attachments/assets/1921fe54-bf08-46d7-8b94-1af941a8ba04" />


- **LOG-IN**\
Jika kamu menjawab "yes" maka Washy akan mengalihkanmu ke halaman Log-In
<img width="687" height="247" alt="Screenshot 2025-10-26 172615" src="https://github.com/user-attachments/assets/02a0214f-62d4-42ee-960e-c64405f992ee" />


Selanjutnya, kamu akan diminta untuk mengisi Username dan Password milikmu, apabila akunnya sudah terdaftar di database maka Washy akan mengalihkanmu ke menu layanan admin/cust.\
<img width="691" height="207" alt="Screenshot 2025-10-26 172733" src="https://github.com/user-attachments/assets/a674de26-1ac3-43db-b144-401af41613ad" />


Namun jika kamu melakukan kesalahan input data, baik di username ataupun password. Maka kesempatanmu untuk melakukan log-in berkuran (kesempatan log-in = 3) dan jika kesempatanmu sudah habis maka kamu akan keluar dari program.\
<img width="895" height="497" alt="Screenshot 2025-10-26 173250" src="https://github.com/user-attachments/assets/2155f124-3a34-43c6-b662-f23a501cecf9" />


# MENU ADMIN
ketika kamu sudah berhasil Log-in, maka Washy akan mengecek apakah akunmu ini Admin atau Customer sesuai dengan role yang ada di database.\
<img width="672" height="187" alt="Screenshot 2025-10-26 174425" src="https://github.com/user-attachments/assets/28049f10-f4fe-49f0-a409-cc785acbea1f" />


Jika kamu terdaftar sebagai admin, maka kamu akan masuk ke menu admin.
<img width="670" height="432" alt="Screenshot 2025-10-26 174439" src="https://github.com/user-attachments/assets/93d42ef5-1db3-4790-838c-50fbcac10e0c" />


- **MENU 1**\
Pada menu 1 ini, kamu sebagai admin bisa melihat rekapan harian pemesanan customer dari Washify Laundry. 
<img width="672" height="418" alt="Screenshot 2025-10-26 174854" src="https://github.com/user-attachments/assets/a52c4dc8-a9c1-4c92-a2c1-ecf752e5d73f" />
<img width="1402" height="278" alt="Screenshot 2025-10-26 175153" src="https://github.com/user-attachments/assets/2b27096f-6125-449d-b221-99c5bd6148a7" />
Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu admin.


- **MENU 2**\
Pada menu 2 ini, kamu sebagai admin bisa melakukan update harga pada layanan yang dimiliki oleh Washify Laundry.
<img width="565" height="368" alt="image" src="https://github.com/user-attachments/assets/79f41c13-b296-48f9-8de8-262ae17d0aa8" />


Lalu kamu akan diminta untuk memilih nomor layanan mana yang ingin kamu update harganya, semisal disini kami memilih nomor 5 (Cuci Satuan) dan kami ingin mengubah harganya menjadi Rp 5.000,00.\
<img width="552" height="339" alt="image" src="https://github.com/user-attachments/assets/7fffab8e-2660-4a73-b78e-784fe43094fb" />


Maka selanjutnya akan muncul output tabel yang sudah ter-update harganya. 
<img width="552" height="342" alt="image" src="https://github.com/user-attachments/assets/45cb447d-2e22-4835-8e7c-696552843f44" />\
Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu admin.


- **MENU 3**\
Pada menu 3 ini, kamu sebagai admin bisa menambahkan layanan yang ingin disajikan oleh Washify Laundry ke customer.
<img width="561" height="364" alt="image" src="https://github.com/user-attachments/assets/f3d8300a-99b1-46d2-8c30-ba5a149f2d64" />


Lalu kamu akan diminta untuk input nama layanan terbaru beserta dengan harganya, semisal disini kami akan menambahkan layanan "Cuci Gorden" dengan harga Rp 30.000,00. Maka kita akan memasukkan data itu ke masing-masing input data sesuai dengan yang sudah disediakan Washy.\
<img width="558" height="340" alt="image" src="https://github.com/user-attachments/assets/b3f488ee-434e-4c77-899b-50a73f990936" />


Selanjutnya akan muncul output tabel yang sudah tertambahkan layanan baru beserta harganya.
<img width="547" height="368" alt="image" src="https://github.com/user-attachments/assets/8895ca6c-2119-4aa5-9bf1-d7a44c5a14c7" />\
Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu admin.


- **MENU 4**\
Pada menu 4 ini, kamu sebagai admin bisa menghapus layanan yang sudah ada.
<img width="565" height="365" alt="Screenshot 2025-10-26 181746" src="https://github.com/user-attachments/assets/809ebf77-492a-4212-8d88-21c61f742669" />


Lalu kamu akan diminta untuk memilih nomor layanan mana yang ingin kamu hapus dari tabel layanan, semisal disini kami memilih nomor 7 (Cuci Gorden). Maka kami hanya perlu untuk input nomor 7 saja dan layanan akan terhapus permanen.\
<img width="553" height="348" alt="image" src="https://github.com/user-attachments/assets/0198a488-de73-4def-aac6-a2f99f763a92" />


Selanjutnya akan muncul output tabel yang nomor layanannya kita pilih sudah terhapus dari tabel.
<img width="552" height="345" alt="image" src="https://github.com/user-attachments/assets/b2490ddb-35ef-4c36-80f9-27c64a2737a9" />


Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu admin.


- **MENU 5**\
Pada menu 5 ini, kamu bisa melakukan Log-Out atau keluar dari program.
<img width="552" height="362" alt="image" src="https://github.com/user-attachments/assets/dfd51420-bf2a-42bb-a346-b7ed69124ce8" />


Setelahnya kamu akan ditanya apakah yakin ingin log-out, jika kamu menjawab "yes" maka kamu akan keluar atau log-out dari sistem.
<img width="556" height="470" alt="image" src="https://github.com/user-attachments/assets/dc6c8d6a-e213-403e-9f3b-b959c1a74586" />


Namun jika kamu menjawab "no" maka kamu akan kembali ke menu admin.
<img width="551" height="469" alt="image" src="https://github.com/user-attachments/assets/9f95f9d5-7c4b-459c-b724-ca0e229cec93" />



# MENU CUSTOMER
ketika kamu sudah berhasil Log-in, maka Washy akan mengecek apakah akunmu ini Admin atau Customer sesuai dengan role yang ada di database.\
<img width="551" height="182" alt="Screenshot 2025-10-26 183522" src="https://github.com/user-attachments/assets/3767bd8d-8936-4366-b7be-75c2a1d3f36f" />


Jika kamu terdaftar sebagai customer, maka kamu akan masuk ke menu customer.
<img width="548" height="358" alt="Screenshot 2025-10-26 183539" src="https://github.com/user-attachments/assets/f68ab701-bf6c-4a53-9cc5-372ea0e72a58" />


- **MENU 1**\
Pada menu 1 ini, kamu sebagai customer bisa melihat layanan apa saja yang disediakan oleh Washify Laundry.
<img width="566" height="366" alt="image" src="https://github.com/user-attachments/assets/7ef62b0f-4d75-4a6b-8e19-ad7fe97046ce" />
<img width="561" height="348" alt="image" src="https://github.com/user-attachments/assets/9f8503dc-d676-48d8-8968-ca492dccaec6" />\
Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu customer.


- **MENU 2**\
Pada menu 2 ini, kamu sebagai customer bisa melihat layanan apa saja yang disediakan oleh Washify Laundry dan melakukan pemesanan layanan beserta transaksi pembayaran.
<img width="552" height="350" alt="image" src="https://github.com/user-attachments/assets/e6182d0b-35e6-42aa-8852-931e1ceb1211" />

Setelah itu akan muncul pertanyaan nomor layanan mana yang ingin kamu pesan dan berapa jumlah (Baju atau per-Kg) yang ingin kamu laundry kan. Semisal kami ingin memesan layanan nomor 2 dengan jumlah 2 Kg, maka tinggal kami masukkan ke masing-masing input sesuai dengan apa yang ditanyakan.\
<img width="557" height="395" alt="image" src="https://github.com/user-attachments/assets/cdaadd2f-ffb7-4ade-ad70-fba75dd72bb2" />

Setelahnya akan muncul catatan singkat mengenai layanan yang kamu pesan dan total pembayarannya, selain itu akan muncul pertanyaan apakah kamu ingin menambahkan add-on.\
<img width="561" height="543" alt="image" src="https://github.com/user-attachments/assets/04672940-68ff-4b20-b838-521834a46be1" />

jika kamu menjawab "no", maka akan langsung muncul output format pemesanan.\
<img width="303" height="128" alt="Screenshot 2025-10-26 195724" src="https://github.com/user-attachments/assets/9c46f640-c760-4fe9-913d-9252bebbea06" />

Jika kamu menjawab "yes", maka akan muncul tabel yang berisikan layanan tambahan atau "add-on" dan kemudian akan Washy akan meminta kita untuk memilih nomor layanan yang ingin kita tambahkan. Semisal kami ingin memilih nomor 4 (Antar-Jemput), maka input nomor 4 dan setelahnya akan ditanya lagi apakah kamu ingin menambah add-on lagi.\
<img width="556" height="547" alt="image" src="https://github.com/user-attachments/assets/dc37ced1-4712-48b6-b9f4-93ffa458016e" />
<img width="556" height="366" alt="image" src="https://github.com/user-attachments/assets/aacdf1c0-564b-4488-87e0-6cd996e20e3d" />

Jika kamu menjawab yes, maka kamu akan memasukkan lagi ingin menambah add on berapa. Lalu jika kamu jawab no, maka akan langsung lanjut ke format pemesanan.\
<img width="303" height="128" alt="Screenshot 2025-10-26 195724" src="https://github.com/user-attachments/assets/9c46f640-c760-4fe9-913d-9252bebbea06" />

Format pesanan ini kita diminta untuk mengisi nama, tanggal pemesanan, dan alamat.\
<img width="301" height="149" alt="Screenshot 2025-10-26 200449" src="https://github.com/user-attachments/assets/63d71976-605c-49f5-8ab3-fd67809db01b" />

Jika semua input yang diminta sudah terisi, maka akan langsung menampilkan invoice dari pesanan.\
<img width="304" height="208" alt="image" src="https://github.com/user-attachments/assets/26da6db3-b4f0-4ae7-8abf-55463fb50d55" />


- **MENU 3**\
Pada menu 3 ini, kamu sebagai customer bisa melihat berapa isi saldo yang kamu miliki pada akun sekarang.
<img width="548" height="367" alt="image" src="https://github.com/user-attachments/assets/2966a3a0-425d-4488-8dd3-cad5046fd52b" />
<img width="552" height="170" alt="image" src="https://github.com/user-attachments/assets/f5d4ecc6-8ea1-4284-978d-4bd8aa508318" />\
Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu admin.

- **Menu 4**\
Pada menu 4 ini, kamu sebagai customer bisa melakukan top-up saldo ke akun kamu sekarang.
<img width="550" height="367" alt="Screenshot 2025-10-26 190728" src="https://github.com/user-attachments/assets/a7afac65-c10f-4bbc-a793-df1ab91fcd25" />

Setelahnya akan ditampilkan kembali saldo yang kamu miliki sekarang dan Washy akan memintamu untuk memasukkan nominal yang kamu ingin top-up, dengan syarat minimal Rp 10.000,00 dan maksimal Rp 200.000,00. Semisal disini kami ingin melakukan top-up sebanyak Rp 100.000,00 maka kita akan meng-input sebanyak Rp 100.000,00 pada pertanyaan yang telah disediakan. Setelahnya, akan ada output bahwa saldo berhasil ditambahkan dan Washy juga menampilkan saldo terbarumu.\
<img width="710" height="332" alt="image" src="https://github.com/user-attachments/assets/5e958147-be49-47f7-bd0f-c7d2331d82a4" />\
Lalu jika kamu klik "Enter" pada keyboardmu maka, dia akan kembali ke menu customer.

Namun jika kamu input nominal di bawah batas minimal atau di atas batas maksimal, maka dia akan menampilkan output seperti pada gambar di bawah dan dia akan terus mengulang sampai kamu memasuki nominal sesuai dengan persyaratannya.\
<img width="705" height="369" alt="image" src="https://github.com/user-attachments/assets/5ac42c2c-6a32-47d7-b415-b02b49ba629f" />

- **MENU 5**\
Pada menu 5 ini, kamu bisa melakukan Log-Out atau keluar dari program.
<img width="551" height="361" alt="image" src="https://github.com/user-attachments/assets/9331aebe-8f80-4185-b702-db7c24dc2743" />

Setelahnya kamu akan ditanya apakah yakin ingin log-out, jika kamu menjawab "yes" maka kamu akan keluar atau log-out dari sistem.
<img width="555" height="470" alt="image" src="https://github.com/user-attachments/assets/05b086af-1101-4a5f-9170-c97fbbcc613b" />

Namun jika kamu menjawab "no" maka kamu akan kembali ke menu admin.
<img width="556" height="470" alt="image" src="https://github.com/user-attachments/assets/ca4cd262-01a8-4b0d-ba65-be98cef0ea40" />


# ERROR HANDLING
Error Handling yang di terapkan pada sistem manajemen laundry ini, sebagai berikut:  
- except KeyboardInterrupt : Jika pengguna menekan ctrl+c pada saat program berjalan.    
- except EOFError : Jika pengguna menekan ctrl+z enter pada saat program berjalan.  
- except ValueError : Jika kamu menginput yang tidak sesuai. misalnya, jika harusnya pengguna menginput angka tapi pengguna menginput huruf

**Halaman Awal**  
- except KeyboardInterrupt  
<img width="573" height="256" alt="Screenshot 2025-10-26 212037" src="https://github.com/user-attachments/assets/e20928f3-64ab-4406-9c62-9bfcf67c924d" />
<img width="649" height="334" alt="Screenshot 2025-10-26 213736" src="https://github.com/user-attachments/assets/df6efca3-b893-4675-b16f-b93653fa7195" />

- except EOFError  
<img width="596" height="264" alt="Screenshot 2025-10-26 212047" src="https://github.com/user-attachments/assets/781ee48a-0a97-4144-b2da-a7389b844f03" />  
<img width="640" height="338" alt="Screenshot 2025-10-26 213752" src="https://github.com/user-attachments/assets/53e3d83a-8d81-463e-9d91-51b63ded2e12" />


**Log in**  
- except KeyboardInterrupt dan except EOFError  
<img width="649" height="346" alt="Screenshot 2025-10-26 213550" src="https://github.com/user-attachments/assets/9975e89c-9e1c-4b63-ab21-c07e0f05bcc0" />

**Sign up**  
- except KeyboardInterrupt dan except EOFError  
<img width="618" height="290" alt="Screenshot 2025-10-26 214052" src="https://github.com/user-attachments/assets/de94ffcc-267a-40c0-91d8-a9df01f1a9b3" />  

**Daftar Menu Admin**
- except KeyboardInterrupt  
<img width="678" height="462" alt="Screenshot 2025-10-26 214351" src="https://github.com/user-attachments/assets/2f318f04-ff61-4b0d-9af2-26f9b7f44a6a" />

- except EOFError  
<img width="667" height="470" alt="Screenshot 2025-10-26 214358" src="https://github.com/user-attachments/assets/5d332998-fb41-4e7d-9045-98bacc0e5d5a" />

- except ValueError  
<img width="616" height="441" alt="Screenshot 2025-10-26 214335" src="https://github.com/user-attachments/assets/beba5c53-ad56-42ac-a9f3-4f16a9170163" />

1. **Recap Pesanan**  
- except KeyboardInterrupt  
<img width="1494" height="415" alt="Screenshot 2025-10-26 214824" src="https://github.com/user-attachments/assets/a70ad031-8c29-4750-ab5d-df93c1ffda47" />

- except EOFError  
<img width="1441" height="388" alt="Screenshot 2025-10-26 214850" src="https://github.com/user-attachments/assets/29f6533d-0b89-474b-8651-c8f21e8628fc" />

2. **Update Harga**  
- except KeyboardInterrupt   
<img width="615" height="351" alt="Screenshot 2025-10-26 215139" src="https://github.com/user-attachments/assets/d2166b3e-6ef0-46e3-be97-a64d1bccd415" />

- except EOFError    
<img width="723" height="377" alt="Screenshot 2025-10-26 215149" src="https://github.com/user-attachments/assets/0ba4c9f8-81ba-4686-9bfb-b60be7284426" />

- except ValueError    
<img width="643" height="381" alt="Screenshot 2025-10-26 215201" src="https://github.com/user-attachments/assets/3c769311-5892-4b60-b906-4f5181a06a1d" />
<img width="672" height="407" alt="Screenshot 2025-10-26 215522" src="https://github.com/user-attachments/assets/ff87d822-908c-4809-9a16-9111982a04cb" />

3. **Menambah Layanan**  
- except KeyboardInterrupt  
<img width="720" height="425" alt="Screenshot 2025-10-26 215808" src="https://github.com/user-attachments/assets/af019b10-766d-416c-83b5-5933fc0c8cb8" />

- except EOFError     
<img width="696" height="378" alt="Screenshot 2025-10-26 215817" src="https://github.com/user-attachments/assets/a5cf82bd-5f7c-48d4-8c02-b5bb7657f6a9" />

- except ValueError    
<img width="648" height="407" alt="Screenshot 2025-10-26 215745" src="https://github.com/user-attachments/assets/ec48a3c9-c594-4a33-b9ea-3522b995e1b0" />

4. **Hapus Layanan**
- except KeyboardInterrupt  
<img width="550" height="377" alt="Screenshot 2025-10-26 220011" src="https://github.com/user-attachments/assets/beae0319-563a-4b79-8b84-6742014b327a" />

- except EOFError     
<img width="577" height="390" alt="Screenshot 2025-10-26 220018" src="https://github.com/user-attachments/assets/6c4a7e7d-ac92-4f78-97c2-73fd2badfdce" />

- except ValueError    
<img width="560" height="396" alt="Screenshot 2025-10-26 220031" src="https://github.com/user-attachments/assets/b8dd1fb6-12fb-488c-ad6f-a8408d2321c9" />

5. **Keluar (menu admin)**
- except KeyboardInterrupt  
<img width="619" height="412" alt="Screenshot 2025-10-26 220209" src="https://github.com/user-attachments/assets/aa4167a3-227c-47f7-a278-bf9444cf533d" />

- except EOFError  
<img width="676" height="427" alt="Screenshot 2025-10-26 220222" src="https://github.com/user-attachments/assets/f0d6c9fe-9abd-490a-a02a-6789c345a336" />

**Daftar Menu Customer**
- except KeyboardInterrupt  
<img width="523" height="407" alt="Screenshot 2025-10-26 220950" src="https://github.com/user-attachments/assets/f6655022-a355-4588-84e9-111d787c2ec2" />

- except EOFError  
<img width="541" height="441" alt="Screenshot 2025-10-26 220958" src="https://github.com/user-attachments/assets/110475b0-b27e-439a-a396-a97018b8c358" />

- except ValueError    
<img width="515" height="431" alt="Screenshot 2025-10-26 221018" src="https://github.com/user-attachments/assets/2c377c0d-9e96-495a-a526-b24fff137f5b" />

1. **Daftar Layanan**
- except KeyboardInterrupt  
<img width="533" height="367" alt="Screenshot 2025-10-26 221034" src="https://github.com/user-attachments/assets/1854e78b-6085-499f-a93d-ad47bcced17e" />

- except EOFError  
<img width="539" height="405" alt="Screenshot 2025-10-26 221048" src="https://github.com/user-attachments/assets/20fd39eb-b437-4009-9407-ffe1463e2d52" />

2. **Pesan Layanan**
- except KeyboardInterrupt  
<img width="503" height="394" alt="Screenshot 2025-10-26 221350" src="https://github.com/user-attachments/assets/1c319dea-c065-454f-b8f0-fd4859a8a8a3" />

- except EOFError  
<img width="519" height="423" alt="Screenshot 2025-10-26 221358" src="https://github.com/user-attachments/assets/4fb4029b-7806-44ef-b1a7-5e40fbe126fe" />

- except ValueError    
<img width="524" height="438" alt="Screenshot 2025-10-26 221427" src="https://github.com/user-attachments/assets/ce724d28-d04a-4735-a01b-2efbd4ffdd98" />
<img width="585" height="226" alt="Screenshot 2025-10-26 221457" src="https://github.com/user-attachments/assets/80fd7db9-a516-4456-a31e-65e1f0e08bc7" />

**Add on**
- except KeyboardInterrupt, except EOFError, & except ValueError    
<img width="537" height="522" alt="Screenshot 2025-10-26 222204" src="https://github.com/user-attachments/assets/25b782c8-9282-47df-ab7b-3e259a09cd67" />

**Format Pesanan**
- except KeyboardInterrupt  
<img width="647" height="312" alt="Screenshot 2025-10-26 222352" src="https://github.com/user-attachments/assets/7c0c78db-5b81-4a05-9d7e-8c2d7685c81a" />

- except EOFError
<img width="538" height="175" alt="Screenshot 2025-10-26 222410" src="https://github.com/user-attachments/assets/38fb969d-7f31-41da-a278-ed7e6a3b00cd" />

3. **Lihat Saldo**
- except KeyboardInterrupt dan except EOFError  
<img width="570" height="340" alt="Screenshot 2025-10-26 222711" src="https://github.com/user-attachments/assets/2fac2b27-02a1-48db-bf2a-9b54c68029ea" />

4. **Top Up**
- except KeyboardInterrupt  
<img width="630" height="265" alt="Screenshot 2025-10-26 222914" src="https://github.com/user-attachments/assets/e3b5a2dd-2a9a-4be7-821e-b82565b465fd" />

- except EOFError
<img width="649" height="295" alt="Screenshot 2025-10-26 222920" src="https://github.com/user-attachments/assets/8a51f563-96d9-40f1-83af-efb8a3567cde" />

- except ValueError    
<img width="665" height="329" alt="Screenshot 2025-10-26 222933" src="https://github.com/user-attachments/assets/682ef5f6-ca01-4f92-8e0e-0d8b445243cd" />

5. **Keluar(menu customer)**
- except KeyboardInterrupt     
<img width="504" height="204" alt="Screenshot 2025-10-26 223316" src="https://github.com/user-attachments/assets/0fa421a8-e0c2-42f3-a0c7-cfd63ecbbd2b" />

- except EOFError
<img width="511" height="215" alt="Screenshot 2025-10-26 223325" src="https://github.com/user-attachments/assets/585fd2a7-de7d-4654-8a2b-e629e86f6cd2" />

# VALIDASI
Di program sistem manajemen laundry ini terdapat validasi, yaitu sebagai berikut:
- Validasi angka : Memastikan input dari pengguna adalah angka. Mengecek agar angka yang di input di antara batas minimal dan maksimal.
- Validasi Yes or No : Memastikan pengguna untuk menjawab hanya antara yes atau no
- Validasi Teks : Memastikan pengguna menginput sesuai dengan batas minimal
- Validasi tanggal : Memastikan pengguna agar menginput tanggal sesuai dengan format

Contoh dari **validasi angka**:  
<img width="689" height="258" alt="Screenshot 2025-10-26 225015" src="https://github.com/user-attachments/assets/cb8eeadc-bb68-4f07-8790-b369efa1708b" />

Contoh dari **validasi yes or no**:  
<img width="552" height="168" alt="Screenshot 2025-10-26 225137" src="https://github.com/user-attachments/assets/b05b2ef5-46cc-4f12-9c8a-c0f21609b549" />

Contoh dari **validasi teks**:  
<img width="545" height="199" alt="Screenshot 2025-10-26 225337" src="https://github.com/user-attachments/assets/f56dae14-fb92-4177-810b-feb716b9377f" />

Contoh dari **validasi tanggal**:  
<img width="643" height="294" alt="Screenshot 2025-10-26 225559" src="https://github.com/user-attachments/assets/7bb77aad-dbd0-47ea-80e5-d960c84ce328" />

  
  








