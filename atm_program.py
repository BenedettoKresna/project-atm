# Code sebagai mesin ATM

from customer import Customer
import random
import datetime

atm = Customer(id)

while True:
    id = int(input("Masukkan nomor pin Anda :"))
    trial = 0
    print(atm.id)

    while (id != int(atm.check_pin_customer()) and trial < 3):
        id = int(input("Pin yang anda masukkan salah.\nSilahkan coba lagi:"))
        trial += 1

        if trial == 3:
            print("Error")
            exit()

    while True:
        print("Selamat datang")
        print("1-Cek Saldo \n2-Debet \n3-Simpan\n4-Ganti Pin \n5-Keluar")

        custumer_menu = int(input("Masukkan menu (1-5):"))

        if custumer_menu == 1:
            print("Saldo Anda sekarang : Rp.%s,00" % str(atm.check_balance_customer()))

        elif custumer_menu == 2:
            nominal = int(input("Masukkan nominal debet Anda :"))
            verify = input("Anda yakin untuk melakukan debet sejumlah %s (y/n) :" % str(nominal))
            if verify == "y":
                print("Saldo awal Anda : Rp.%s,00" % str(atm.check_balance_customer()))
            else:
                break
            if nominal < atm.custBalance:
                atm.menu_debet(nominal)
                print("Transaksi Berhasil!")
                print("Sisa saldo Anda : Rp.%s,00" % str(atm.check_balance_customer()))
            else:
                print("Saldo Anda tidak mencukupi, silahkan isi saldo terlebih dahulu.")

        elif custumer_menu == 3:
            nominal = int(input("Masukkan nominal simpan Anda :"))
            verify = input("Anda yakin untuk melakukan simpan sejumlah %s (y/n) :" % str(nominal))
            if verify == "y":
                atm.menu_simpan(nominal)
                print("Transaksi Berhasil!")
                print("Saldo Anda sekarang : Rp.%s,00" % str(atm.check_balance_customer()))
            else:
                break
 
        elif custumer_menu == 4:
            verify_pin = int(input("Masukkan pin Anda :"))

            while verify_pin != atm.check_pin_customer():
                print("Maaf pin Anda salah")

            update_pin = int(input("Masukkan pin baru Anda :"))
            print("Pin Anda berhasil diganti")

            verify_updated_pin = int(input("Cocokkan pin anda :"))

            if update_pin == verify_updated_pin:
                print("Berhasil")
            else:
                print("Error")

        elif custumer_menu == 5:
            print("Resi bukti transaksi Anda.")
            print("Nomor : ", random.randint(100000, 1000000))
            print("Tanggal :", datetime.datetime.now())
            print("Saldo :", atm.check_balance_customer())
            print("Terima Kasih")
            exit()
            
        else:
            print("Menu belum tersedia")
