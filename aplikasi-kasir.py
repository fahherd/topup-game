import sys
import os
cart = []  # Mengganti `total` menjadi `cart` untuk menyimpan informasi produk

# memastikan input id hanya angka
def input_angka(prompt):
    while True:
        try:
            angka = int(input(prompt))
            return angka
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi!")

# melakukan clear pada terminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# list produk yang tersedia
products = [
    {"id": 1, "nama": "| 50  Diamond |", "harga": 10000},
    {"id": 2, "nama": "| 100 Diamond |", "harga": 20000},
    {"id": 3, "nama": "| 150 Diamond |", "harga": 30000},
    {"id": 5, "nama": "| 200 Diamond |", "harga": 40000},
    {"id": 6, "nama": "| 1x  WDP     |", "harga": 100000},
    {"id": 7, "nama": "| 2x  WDP     |", "harga": 190000},
]

# input data user
def input_user_data():
    clear_screen()
    global userName, userID
    print("-------------------------------")
    print("       TOPUP GAME ONLINE       ")
    print("-------------------------------")
    userName = input("Masukkan username  : ")
    userID = input_angka("Masukkan nomor ID  : ")
    print(f"\nSelamat datang, {userName} (ID: {userID})!")

# program utama 
def main():
    clear_screen()

    # proses pembelian produk
    print("-------------------------------")
    print("       TOPUP GAME ONLINE       ")
    print("-------------------------------")

    print("\n ID | Nama produk | Harga")
    print("-------------------------------")
    for product in products:
        print(f"{product['id']}. {product['nama']} - Rp{product['harga']:,}")
    print("-------------------------------")
    kode = input_angka("Masukkan id produk  : ")

    # Cari produk berdasarkan kode
    product = next((p for p in products if p['id'] == kode), None)
    if product:
        kuantitas = input_angka(f"Masukkan kuantitas untuk {product['nama']} (minimal 1): ")
        if kuantitas < 1:
            print("Kuantitas minimal adalah 1. Silakan coba lagi.")
            main()
        else:
            # Tambahkan produk ke keranjang dengan kuantitas
            cart.append({
                "nama": product['nama'], 
                "harga": product['harga'], 
                "kuantitas": kuantitas
            })
            print("-------------------------------")
            print(f"\n{product['nama']} Qty. x{kuantitas} | berhasil ditambahkan ke keranjang!")
            tanya()
    else:
        print("\nProduk tidak ditemukan. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        main()


def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    if tanya == "y":
        main()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")
        main()

def akhir():
    clear_screen()
    print("\n-------------------------------")
    print("       STRUK PEMBELIAN         ")
    print("-------------------------------")
    print(f"Username: {userName}")
    print(f"User ID : {userID}")
    print("\nDaftar Produk:")

    # Variabel untuk menyimpan struk ke file
    struk = []
    struk.append("\n-------------------------------")
    struk.append("       STRUK PEMBELIAN         ")
    struk.append("-------------------------------")
    struk.append(f"Username: {userName}")
    struk.append(f"User ID : {userID}")
    struk.append("\nDaftar Produk:")

    # Tampilkan daftar produk di keranjang dan hitung subtotal
    subtotal = 0
    for idx, item in enumerate(cart, start=1):
        total_harga = item['harga'] * item['kuantitas']  # Hitung total harga berdasarkan kuantitas
        product_line = f"{idx}. {item['nama']} x{item['kuantitas']} - Rp{total_harga:,}"
        print(product_line)
        struk.append(product_line)
        subtotal += total_harga

    # Hitung pajak dan diskon
    tax = subtotal * 0.1
    diskon = subtotal * 0.05 if subtotal > 300000 else 0
    totalakhir = subtotal + tax - diskon

    # Tampilkan rincian pembayaran
    struk.append("\n-------------------------------")
    struk.append(f"SubTotal         : Rp{subtotal:,}")
    struk.append(f"Pajak (10%)      : Rp{tax:,}")
    struk.append(f"Potongan Harga   : Rp{diskon:,}")
    struk.append("note: potongan didapat jika\n      berbelanja lebih dari Rp50,000")
    struk.append("-------------------------------")
    struk.append(f"Total            : Rp{totalakhir:,}")
    struk.append("-------------------------------")

    print("\n-------------------------------")
    print(f"SubTotal         : Rp{subtotal:,}")
    print(f"Pajak (10%)      : Rp{int(tax):,}")
    print(f"Potongan Harga   : Rp{int(diskon):,}")
    print("note: potongan didapat jika\n      berbelanja lebih dari Rp50,000")
    print("-------------------------------")
    print(f"Total            : Rp{int(totalakhir):,}")
    print("-------------------------------")

    # Proses pembayaran
    bayar = input_angka("Bayar            : Rp")
    if bayar < totalakhir:
        input("Uang tidak cukup untuk pembayaran. Silakan coba lagi.")
        akhir()
    else:
        kembalian = bayar - totalakhir
        print(f"Kembalian        : Rp{int(kembalian):,}")
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")

        # Tambahkan pembayaran dan kembalian ke struk
        struk.append(f"Bayar            : Rp{bayar:,}")
        struk.append(f"Kembalian        : Rp{kembalian:,}")
        struk.append("-------------------------------")
        struk.append("          Terima Kasih         ")
        struk.append("-------------------------------")

        # Simpan struk ke file
        save_struck = input("Apakah anda ingin menyimpan struck? (y/n): ")
        if save_struck == "y":
            with open("struk.txt", "w", encoding="utf-8") as file:
                for line in struk:
                    file.write(line + "\n")
            print("\nStruk telah disimpan ke file 'struk.txt'.")
        else: None

    
# function yang akan di eksekusi
input_user_data() #eksekusi pertama
main() #eksekusi kedua