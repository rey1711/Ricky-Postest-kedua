print("="*40)
print("SELAMAT DATANG DI REY'S VAPESTORE")
print("="*40)

while True:
    username = input("Masukkan Nama Anda: ")
    Nim  = input("Masukkan NIM Anda: ")
    password = 123123
    if not Nim.isdigit():
        print("NIM harus diisi dengan angka. Silakan coba lagi.")
        continue
    else:  
        print("Selamat datang", username)
        break

from prettytable import PrettyTable

# list untuk menyimpan data Barang
data_Barang = [
    ["001", "Centaurus", 580000],
    ["002", "Mvp II", 450000],
    ["003", "Drag S", 350000],
    ["004", "Drag X", 350000],
    ["005", "Voltazio", 400000],
    ["006", "Ursa Baby", 200000],
    ["007", "Liquid Vanilla Ice Cream", 140000],
    ["008", "Liquid Savage by Oura", 140000],
    ["009", "Rda Dead Rabbit", 250000],
]


# pembeli
def transaksi():
    while True:
        # menampilkan seluruh Barang yang tersedia
        print("Daftar Barang yang Tersedia")
        show_Barang()
        
        # input id Barang dan jumlah yang ingin dibeli
        id_Barang = input("Masukkan ID Barang yang ingin dibeli: ")
        qty = int(input("Masukkan jumlah Barang yang ingin dibeli: "))
        
        # memeriksa apabila jumlah yang ingin dibeli melebihi stok
        for Barang in data_Barang:
            if Barang[0] == id_Barang:
                if qty > 1:
                    print("Maaf, jumlah maksimum pembelian adalah 1!")
                    break
        else:
            # menampilkan total harga
            for i in range(len(data_Barang)):
                if data_Barang[i][0] == id_Barang:
                    total_harga = data_Barang[i][2] * qty
                    print("Total harga: Rp", total_harga)
                    
        
        # menampilkan kembali tampilan daftar Barang apabila input salah
        print()

# seller
def create():
    # input data Barang yang baru
    id_Barang = input("Masukkan ID Barang: ")
    nama_Barang = input("Masukkan nama Barang: ")
    harga_Barang = int(input("Masukkan harga Barang: "))
    
    # menambahkan Barang yang baru ke dalam database
    data_Barang.append([id_Barang, nama_Barang, harga_Barang])
    
    # menampilkan daftar Barang lengkap dengan Barang baru yang ditambahkan
    show_Barang()

def read():
    # menampilkan seluruh Barang yang terdapat dalam database
    show_Barang()

def update():
    # input id Barang yang ingin diperbarui
    id_Barang = input("Masukkan ID Barang yang ingin di-update data: ")
    for i in range(len(data_Barang)):
        if data_Barang[i][0] == id_Barang:
            # input data Barang yang baru
            nama_Barang = input("Masukkan nama Barang baru: ")
            harga_Barang = int(input("Masukkan Harga Barang baru: "))
            
            # melakukan update Barang yang dipilih
            data_Barang[i][1] = nama_Barang
            data_Barang[i][2] = harga_Barang
            
            # menampilkan daftar Barang yang terbaru
            show_Barang()
            break
    else:
        print("Barang tidak ditemukan")

def delete():
    # input id Barang yang ingin dihapus
    id_Barang = input("Masukkan ID Barang yang ingin dihapus: ")
    for i in range(len(data_Barang)):
        if data_Barang[i][0] == id_Barang:
            # menghapus Barang sesuai input id
            data_Barang.pop(i)
            
            # menampilkan daftar Barang yang terbaru
            show_Barang()
            break
    else:
        print("Barang tidak ditemukan")
    
# menampilkan seluruh Barang yang terdapat dalam database dengan prettytable
def show_Barang():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Barang", "Harga"]
    for Barang in data_Barang:
        table.add_row(Barang)
    print(table)

# program utama
while True:
    print("="*40)
    print("REY'S VAPESTORE")
    print("="*40)
    print("1. Seller")
    print("2. Pembeli")
    print("3. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        print(input("Masukkan password anda: "))
        if password == 123123:
            print("anda berhasil login")
        else :  
            print("Password yang anda masukkan salah")
            print("silahkan masukkan ulang")
        print("="*40)
        print("SELLER VAPESTORE")
        print("="*40)
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Kembali")

        admin_choice = input("Pilih menu: ")
        if admin_choice == "1":
            create()
        elif admin_choice == "2":
            read()
        elif admin_choice == "3":
            update()
        elif admin_choice == "4":
            delete()
        elif admin_choice == "5":
            continue
        else:
            print("Menu tidak tersedia")

    elif choice == "2":
        print("="*40)
        print("PEMBELI")
        print("="*40)
        transaksi()
    elif choice == "3":
        print("Terima kasih telah mengunjungi REY'S VAPESTORE")
        break
    else:
        print("Menu tidak tersedia")

