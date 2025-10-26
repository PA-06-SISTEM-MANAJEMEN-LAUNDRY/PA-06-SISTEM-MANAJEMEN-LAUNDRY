import time
import json
import pwinput
from prettytable import PrettyTable
from datetime import datetime
import os
os.system('cls')

json_file = 'datauseradmin.json'
json_produk = 'produk.json'
json_pesanan = 'pesanan.json'

#================================== MENU =======================================

menu_admin = {
    "1." : "Lihat Recap Pesanan Laundry",
    "2." : "Update Harga Layanan",
    "3." : "Menambahkan Layanan Laundry Baru",
    "4." : "Menghapus Layanan Laundry",
    "5." : "Log Out"
}

menu_customer = {
    "1." : "Lihat Layanan Laundry",
    "2." : "Pesan Layanan Laundry",
    "3." : "Lihat Saldo",
    "4." : "Top Up Saldo",
    "5." : "Log Out"
}

menu_addon = [
    {"No": 1, "Nama": "Lipat Rapi", "Harga": 7000},
    {"No": 2, "Nama": "Setrika Lipat", "Harga": 12000},
    {"No": 3, "Nama": "Pewangi Tambahan", "Harga": 4000},
    {"No": 4, "Nama": "Antar-Jemput", "Harga": 15000}
]

#================================= BACA FILE JSON ====================================

def datauseradmin():
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        print("Mohon maaf file tidak ditemukan.. -Washy buatkan yang baru yaa <3")
        time.sleep(2)
        data = []
        with open(json_file, 'w') as f:
            json.dump(data, f, indent = 4)
        return data
    except json.JSONDecodeError:
        print("Sepertinya filemu rusak.. -Washy perbaikin yaa <3")
        time.sleep(2)
        data = []
        with open(json_file, 'w') as f:
            json.dump(data, f, indent = 4)
        return data

def pesanan():
    try:
        with open(json_pesanan, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        print("Mohon maaf file tidak ditemukan.. -Washy buatkan yang baru yaa <3")
        time.sleep(2)
        data = []
        with open(json_pesanan, 'w') as f:
            json.dump(data, f, indent = 4)
        return data
    except json.JSONDecodeError:
        print("Sepertinya filemu rusak.. -Washy perbaikin yaa <3")
        time.sleep(2)
        data = []
        with open(json_pesanan, 'w') as f:
            json.dump(data, f, indent = 4)
        return data

def produk():
    try:
        with open(json_produk, 'r') as f:
            data = json.load(f)
        return data

    except FileNotFoundError:
        print("Mohon maaf file tidak ditemukan.. -Washy buatkan yang baru yaa <3")
        time.sleep(2)
        data = []
        with open(json_produk, 'w') as f:
            json.dump(data, f, indent = 4)
        return data
    except json.JSONDecodeError:
        print("Sepertinya filemu rusak.. -Washy perbaikin yaa <3")
        time.sleep(2)
        data = []
        with open(json_produk, 'w') as f:
            json.dump(data, f, indent = 4)
        return data

#================================= VALIDASI INPUT ====================================

def validangka(pesan, minnilai = None, maxnilai = None):
    while True:
        try:
            angka = int(input(pesan))
            if minnilai is not None and angka < minnilai:
                print(f"Angka harus minimal {minnilai}! -Washy")
                continue
            if maxnilai is not None and angka > maxnilai:
                print(f"Angka harus maksimal {maxnilai}! -Washy")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka! Coba lagi -Washy")
            print("\n+---------------------------------------------------------+\n")
            continue

def validyesno(pesan):
    while True:
        jawaban = input(pesan).lower().strip()
        if jawaban in ["yes", "no"]:
            return jawaban
        print("Input harus 'yes' atau 'no'! -Washy")
        print("\n+---------------------------------------------------------+\n")

def validteks(pesan, minpanjang = 1):
    while True:
        text = input(pesan).strip()
        if len(text) >= minpanjang:
            return text
        print(f"Input tidak boleh kosong! Minimal {minpanjang} karakter -Washy")
        print("\n+---------------------------------------------------------+\n")

def validtanggal(pesan):
    while True:
        tanggal = input(pesan).strip()
        try:
            datetime.strptime(tanggal, "%d/%m/%Y")
            return tanggal
        except ValueError:
            print("Gunakan format tanggal yang benar! (contoh: 25/10/2025) -Washy")
            print("\n+---------------------------------------------------------+\n")

#================================= LOGIN DAN SIGN UP ====================================

def signup():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|                 SIGN-UP WASHIFY LAUNDRY                 |")
    print("+---------------------------------------------------------+")

    while True:
        try:
            userbaru = validteks("Masukkan Username (min. 3 karakter): ", 3)
            passbaru = validteks("Masukkan Password (min. 3 karakter): ", 3)
            data = datauseradmin()

            for user in data:
                if user["username"] == userbaru:
                    print("Username sudah digunakan, tolong gunakan username lain! -Washy\n")
                    print("+---------------------------------------------------------+\n")
                    time.sleep(3)
                    break

            else:
                data.append({"username" : userbaru, "password" : passbaru, "role" : "Customer", "saldo" : 0})
                with open(json_file, 'w') as f: 
                    json.dump(data, f, indent=4)
                print("Selamat!! Username berhasil Washy daftarkan <3")
                time.sleep(3)
                return

        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

def login():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|                   LOG-IN WASHIFY LAUNDRY                |")
    print("+---------------------------------------------------------+")

    kesempatan = 3
    while kesempatan > 0:
        try:
            username = validteks("Masukkan Username Anda: ")
            password = pwinput.pwinput("Masukkan Password Anda: ")
            data = datauseradmin()

            for akun in data:
                if akun["username"] == username and akun["password"] == password:
                        role = akun["role"]
                        if role == "Admin":
                            menuadmin(username)
                            return

                        elif role == "Customer":
                            menucust(username)
                            return

            kesempatan -= 1
            if kesempatan > 0:
                print(f"\nmohon maaff, sepertinya ada kesalahan pada input data. Sisa percobaan kamu: {kesempatan}")
                print("Silahkan coba kembali -Washy <3\n")
                time.sleep(3)
            else:
                print("\nmohon maaff kesempatanmu sudah habiss... Try again later yaa -Washy T_T")
                exit()

        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

#================================== MENU ADMIN =======================================

def menuadmin(username):
    print(f"\nSelamat Datang Kembalii {username} -Washy <3")
    time.sleep(2)
    print("Mengalihkan ke menu utama...")
    time.sleep(3)
    print("\nAnda telah ter-login sebagai Admin!")
    os.system('cls')
    while True:
        os.system('cls')
        print("+---------------------------------------------------------+")
        print("|                MENU ADMIN WASHIFY LAUNDRY               |")
        print("+---------------------------------------------------------+")
        for pilihan_admin, akses_admin in menu_admin.items():
            print(f"\n{pilihan_admin} {akses_admin}")
        try: 
            pilih_menuadmin = validangka("\nPilih Menu Admin (1-5): \n> ", 1, 5)
            if pilih_menuadmin == 1:
                recappesanan()
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menuadmin == 2:
                update_produk()
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menuadmin == 3:
                nambah_produk()
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menuadmin == 4:
                hapus_produk()
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menuadmin == 5:
                keluar = validyesno("\nApakah kamu yakin ingin Log-Out? (yes/no)\n> ")
                if keluar == "yes":
                    print("\nTerima kasih sudah menggunakan Washify ⋆｡˚")
                    exit()
                else:
                    print("\nkembali ke menu utama...")
                    time.sleep(3)
                    os.system('cls')
                    continue

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

#================================== MENU CUST =======================================

def menucust(username):
    print(f"\nSelamat Datang Kembalii {username} -Washy <3")
    time.sleep(2)
    print("Mengalihkan ke menu utama...")
    time.sleep(3)
    print("\nAnda telah ter-login sebagai customer Washify!")
    os.system('cls')
    while True:
        os.system('cls')
        print("+---------------------------------------------------------+")
        print("|               MENU CUSTOMER WASHIFY LAUNDRY             |")
        print("+---------------------------------------------------------+")
        for pilihan_cust, akses_cust in menu_customer.items():
            print(f"\n{pilihan_cust} {akses_cust}")
        try: 
            pilih_menucust = validangka("\nPilih Menu Customer (1-5): \n> ", 1, 5)
            if pilih_menucust == 1:
                daftar_produk()
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menucust == 2:
                pesanan = pesan(username)
                if pesanan == True :
                    input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")
                continue

            elif pilih_menucust == 3:
                lihatsaldo(username)
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menucust == 4:
                topup(username)
                input("\nTekan Enter untuk kembali ke Menu Utama -Washy <3")

            elif pilih_menucust == 5:
                keluar = validyesno("\nApakah kamu yakin ingin Log-Out? (yes/no)\n")
                if keluar == "yes":
                    print("\nTerima kasih sudah menggunakan Washify ⋆｡˚")
                    exit()
                else:
                    print("\nkembali ke menu utama...")
                    time.sleep(3)
                    os.system('cls')
                    continue

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

#================================== ADMIN =======================================

def recappesanan():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|               RECAP PESANAN WASHIFY LAUNDRY             |")
    print("+---------------------------------------------------------+")
    try:
        data = pesanan()

        if not data:
            print("Belum ada pesanan di hari ini -Washy <3")
            time.sleep(3)
            return

        recap = PrettyTable()
        recap.field_names = ["No", "Username", "Nama Pelanggan", "Tanggal Pemesanan", "Alamat Lengkap", "Layanan", "Add-ons", "Total Pemesanan"]
        for i, rekap in enumerate(data, start = 1):
            recap.add_row([i, rekap["Username"], rekap["Nama Pelanggan"], rekap["Tanggal Pemesanan"], rekap["Alamat Lengkap"], rekap["Layanan"], rekap["Add-ons"], rekap["Total Pemesanan"]])
        print(recap)

    except KeyboardInterrupt:
        print("\nMohon jangan menekan ctrl + C -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)
    except EOFError:
        print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e} -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)

def nambah_produk ():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|              TAMBAH LAYANAN WASHIFY LAUNDRY             |")
    print("+---------------------------------------------------------+")
    while True:
        try:
            daftar_produk()
            data = produk()
            nama = validteks("Masukkan nama produk: ")
            harga = validangka("Masukkan harga (min. Rp1000,00): ", 1000)

            data.append({"Nama Produk": nama, "Harga": harga})
            with open(json_produk, 'w') as f:
                json.dump(data, f, indent=4)

            print("Produk berhasil ditambahkan!")
            print("\nBerikut adalah daftar layanan yang terbaru:")
            daftar_produk()
            return

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

def update_produk():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|               UPDATE HARGA WASHIFY LAUNDRY              |")
    print("+---------------------------------------------------------+")
    while True:
        try:
            daftar_produk()
            data = produk()
            nomorlayanan = validangka("Masukkan Nomor layanan yang ingin diupdate : ", 1, len(data))
            harga_baru = validangka("Masukkan harga baru (min. Rp1000,00) : ", 1000)

            if 1 <= nomorlayanan <= len(data):
                data[nomorlayanan - 1]['Harga'] = harga_baru
                print("Produk berhasil Washy update!")

                with open(json_produk, 'w') as f:
                    json.dump(data, f, indent=4)

                print("\nBerikut Nama Layanan Yang Terbaru:")
                daftar_produk()
                return

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

def hapus_produk():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|              HAPUS LAYANAN WASHIFY LAUNDRY              |")
    print("+---------------------------------------------------------+")
    while True:
        try:
            daftar_produk()
            data = produk()
            nomorlayanan = validangka("Masukkan nomor layanan yang ingin dihapus : ", 1, len(data))

            if 1 <= nomorlayanan <= len(data):
                terhapus = data[nomorlayanan - 1]['Nama Produk']
                del data[nomorlayanan - 1]

                with open(json_produk, 'w') as f:
                    json.dump(data, f, indent=4)

                print(f"Layanan {terhapus} berhasil dihapus! -Washy <3")
                print("\nBerikut adalah daftar layanan yang terbaru:")
                daftar_produk()
                return True

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

#=================================== CUSTOMER ========================================

def daftar_produk():
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|              DAFTAR LAYANAN WASHIFY LAUNDRY             |")
    print("+---------------------------------------------------------+")
    try:
        with open(json_produk, 'r') as f:
            data = json.load(f)

        if len(data) == 0:
            print("\nBelum ada layanan yang tersedia.. -Washy")
            return

        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Produk", "Harga"]
        for i, item in enumerate(data, start = 1):
            tabel.add_row([i, item["Nama Produk"], item["Harga"]])
        print(tabel)

    except KeyboardInterrupt:
        print("\nMohon jangan menekan ctrl + C -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)
    except EOFError:
        print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)
    except Exception as e:  
        print(f"\nTerjadi kesalahan: {e} -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)


def add_on():
    print("\n" + "+---------------------------------------------------------+")
    print("|              ADD-ON LAYANAN WASHIFY LAUNDRY             |")
    print("+---------------------------------------------------------+")

    tabeladdon = PrettyTable()
    tabeladdon.field_names = ["No", "Nama Layanan", "Harga (Rp)"]
    for addon in menu_addon:
        tabeladdon.add_row([addon["No"], addon["Nama"], addon["Harga"]])
    print(tabeladdon)

    totaladdon = 0
    addonterpilih = []

    while True:
        try:
            pilihan_addons = validangka("Pilih Nomor Layanan Add-on (1-4) : ", 1, 4)

            if 1 <= pilihan_addons <= len(menu_addon):
                addon = menu_addon[pilihan_addons - 1]
                addonterpilih.append(addon["Nama"])
                totaladdon += addon["Harga"]
                print("Add-on Berhasil ditambahkan -Washy <3")

                lagi = validyesno("\nTambah add-on lagi? (yes/no)\n> ")
                if lagi != "yes":
                    break

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            continue

    return addonterpilih, totaladdon

def pesan(username):
    os.system('cls')
    while True:
        print("+---------------------------------------------------------+")
        print("|              PESAN LAYANAN WASHIFY LAUNDRY              |")
        print("+---------------------------------------------------------+")
        try:
            data = produk()

            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama Produk", "Harga"]
            for i, item in enumerate(data, start=1):
                tabel.add_row([i, item["Nama Produk"], item["Harga"]])
            print(tabel)

            pesanan = validangka("\nSilahkan masukkan layanan yang ingin dipesan : \n> ", 1, len(data))
            jumlah = validangka("Mau Berapa Jumlahnya? ")

            pesan_produk = data[pesanan -1]
            total = pesan_produk["Harga"]*jumlah

            print("\nBerikut Pesanan Anda:")
            print(f"Layanan             : {pesan_produk['Nama Produk']}")
            print(f"Total Pembayaran    : {total}")

            addonterpilih = []

            tanyaadds = validyesno("\nApakah kamu ingin menambahkan add on? (yes/no) \n> ")
            if tanyaadds == "yes":
                addonterpilih, totaladdon = add_on()
                if addonterpilih:
                    print("\n" + "="*50)
                    print("Add-ons                  :")
                    for i, addon in enumerate(addonterpilih, start = 1):
                        print(f"{i}. {addon}")
                    print(f"Total Pemesanan Add-on  : Rp{totaladdon :,}")
                    print("="*50)
                    total = total + totaladdon

            print(f"\nTotal Pembayaran Keseluruhan : Rp{total :,}")
            hasil = transaksi(username, pesan_produk["Nama Produk"], total, addonterpilih)
            return True

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')

def transaksi(username, Nama_Produk, total, addonterpilih):
    os.system('cls')
    print("\n" + "+---------------------------------------------------------+")
    print("|              FORMAT PESANAN WASHIFY LAUNDRY             |")
    print("+---------------------------------------------------------+")
    while True:
        try:
            saldo = bacasaldo(username)
            print(f"\nIsi saldo anda sekarang : Rp {saldo :,}")
            print(f"Total Pembayaran : Rp {total :,}")

            if saldo < total:
                print("\nMohon maaf saldo anda tidak cukup -Washy TT")
                print(f"Anda kekurangan : Rp {total - saldo :,}")
                moneyz = validyesno("\nApakah anda ingin melakukan top-up? (yes/no)\n> ")
                if moneyz == "yes":
                    print("Mengalihkan ke halaman Top-Up....")
                    time.sleep(2)
                    topup(username)

                    saldobarulagi = bacasaldo(username)
                    if saldobarulagi >= total:
                        print("\nSelamat saldo anda sudah cukupp, melanjutkan transaksi pembayaran... -Washy^^")
                        time.sleep(2)
                        return transaksi(username, Nama_Produk, total, addonterpilih)
                    else:
                        print("\nSaldo kamu masih belum cukup.... transaksi dibatalkan -Washy TT")
                        return False

                else:
                    print("\nPemesanan dibatalkan.... -Washy TT")
                    return False

            else:
                print("\nIsilah format di bawah ini!")
                namacust = validteks("Nama : ")
                tanggal = validtanggal("Tanggal Pemesanan (dd/mm/yyyy): ")
                alamat = validteks("Alamat Lengkap : ")

                try:
                    data = pesanan()
                except:
                    data = []

                data.append({"Username" : username, "Nama Pelanggan": namacust, "Tanggal Pemesanan": tanggal, "Alamat Lengkap" : alamat, "Layanan" : Nama_Produk, "Add-ons" : addonterpilih, "Total Pemesanan" : total})
                with open(json_pesanan, 'w') as f:
                    json.dump(data, f, indent=4)

                updatesaldo(username, -total)
                saldobarulagi = bacasaldo(username)

                print("Pesanan Berhasil dibuat -Washy <3")
                print("\n" + "+---------------------------------------------------------+")
                print("|                    INVOICE PEMESANAN                    |")
                print("+---------------------------------------------------------+")
                print("\n" + "="*50)
                print(f"Nama                : {namacust}")
                print(f"Tanggal Pemesanan   : {tanggal}")
                print(f"Alamat Lengkap      : {alamat}")
                print("-"*50)
                print(f"Layanan             : {Nama_Produk}")
                if addonterpilih:
                    print("Add-ons             :")
                    for i, addon in enumerate(addonterpilih, start = 1):
                        print(f"{i}. {addon}")
                print("-"*50)
                print(f"Total Pembayaran    : Rp{total :,}")
                print(f"Saldo Awal          : Rp{saldo :,}")
                print(f"Saldo Sekarang      : Rp{saldobarulagi :,}")
                print("="*50)
                time.sleep(3)
            return True

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')

#================================== SALDO DKK =======================================

def bacasaldo(username):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        for user in data:
            if user['username'] == username:
                return user['saldo']

    except Exception as e:
        print(f"Terjadi kesalahan: {e} -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        return 0

def updatesaldo(username, jumlah):
    try:
        data = datauseradmin()

        for user in data:
            if user["username"] == username:
                user["saldo"] = user.get("saldo", 0) + jumlah
                break

        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        return True

    except Exception as e:
        print(f"Terjadi kesalahan: {e} -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        return False

def topup(username):
    os.system('cls')
    while True:
        print("+---------------------------------------------------------+")
        print("|               TOP-UP SALDO WASHIFY LAUNDRY              |")
        print("+---------------------------------------------------------+")

        saldoskrg = bacasaldo(username)
        print(f"Berikut total saldo yang kamu miliki sekarang\n> Rp {saldoskrg :,}")

        try:
            plus = validangka("\nMasukkan nominal yang ingin di top-up (min. Rp10.000,00 - max. Rp200.000,00)\n> ", 10000, 200000)

            if updatesaldo(username, plus):
                saldonew = bacasaldo(username)
                print("Saldo berhasil ditambahkan -Washy <3")
                print(f"\nBerikut total saldo yang kamu miliki sekarang\n> Rp {saldonew :,}")
                time.sleep(3)
                break
            else:
                print("Gagal menambahkan saldo -Washy")
                time.sleep(3)
                break

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue

def lihatsaldo(username):
    os.system('cls')
    print("+---------------------------------------------------------+")
    print("|          LIHAT SALDO CUSTOMER WASHIFY LAUNDRY           |")
    print("+---------------------------------------------------------+")

    try:
        saldo = bacasaldo(username)
        print(f"Nama Akun : {username}")
        print(f"Isi Saldo : Rp {saldo :,}")
        time.sleep(2)

    except KeyboardInterrupt:
        print("\nMohon jangan menekan ctrl + C -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)
    except EOFError:
        print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e} -Washy T_T")
        print("\n+---------------------------------------------------------+\n")
        time.sleep(3)

#=================================== MASUK PROGRAM ========================================

def Masuk_Washify():
    os.system('cls')
    while True:
        print("+---------------------------------------------------------+")
        print("|               ∘˙○˚.• WASHIFY LAUNDRY ∘˙○˚.•             |")
        print("+---------------------------------------------------------+")

        print("HALLLOOOO!! Selamat Datang ke Washify Laundry ∘˙○˚.•")
        try:
            tanya1 = validyesno("\nApakah kamu sudah memiliki akun? (no/yes)\n> ")

            if tanya1 == "yes":
                print("\nokeeyy, Washy akan mengalihkan kamu ke halaman Log in ^^\n")
                time.sleep(3)
                return login()

            else:
                maunggx = validyesno("\nyahh, apakah kamu ingin membuat akun? (no/yes)\n> ")
                if maunggx == "yes":
                    print("\nokeeyy, Washy akan mengalihkan kamu ke halaman Sign Up ^^\n")
                    time.sleep(3)
                    signup()

                    print("\nSilahkan melakukan Login kembali <3\n")
                    time.sleep(3)
                    return login()
                else:
                    print("Baik... Sampai jumpa di lain waktu yaa..")
                    exit()

        except ValueError:
            print("\nMohon input dalam bentuk angka -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue
        except KeyboardInterrupt:
            print("\nMohon jangan menekan ctrl + C -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue
        except EOFError:
            print("\nMohon jangan menekan ctrl + Z + Enter -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e} -Washy T_T")
            print("\n+---------------------------------------------------------+\n")
            time.sleep(3)
            os.system('cls')
            continue

Masuk_Washify()