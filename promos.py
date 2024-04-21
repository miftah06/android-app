import random
import string
import requests
import numpy as np
import threading
from scapy.all import *

class PromoGenerator:
    def __init__(self, currency='USD'):
        self.currency = currency

    def get_flight_ticket_price(self, origin, destination):
        # Fungsi untuk mengambil harga tiket pesawat dari sumber data
        # Misalnya, panggil API dari penyedia layanan penerbangan
        # Mengembalikan harga dalam mata uang yang ditentukan
        return random.randint(100, 1000)

    def calculate_discount(self, price, discount_rate):
        # Fungsi untuk menghitung diskon berdasarkan persentase diskon
        discount_amount = np.round(price * (discount_rate / 100), 2)
        return discount_amount

    def generate_promo_code(self, length=8):
        # Fungsi untuk menghasilkan kode promosi acak
        characters = string.ascii_uppercase + string.digits
        promo_code = ''.join(random.choices(characters, k=length))
        return promo_code

    def process_payment(self, amount):
        # Fungsi untuk memproses pembayaran menggunakan e-wallet
        # Misalnya, panggil API pembayaran
        # Di sini kita akan menggunakan fungsionalitas fiktif untuk tujuan contoh
        response = requests.post("https://example.com/payment", json={"amount": amount})
        if response.status_code == 200:
            return True
        else:
            return False

    def parallel_processing(self):
        # Fungsi untuk melakukan beberapa tugas secara paralel menggunakan threading
        # Misalnya, mendapatkan harga tiket pesawat dan menghasilkan kode promosi
        price = 0
        discount = 0

        def get_price():
            nonlocal price
            price = self.get_flight_ticket_price('JKT', 'NYC')

        def get_discount():
            nonlocal discount
            discount = self.calculate_discount(price, 10)

        thread1 = threading.Thread(target=get_price)
        thread2 = threading.Thread(target=get_discount)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        return price, discount

    def detect_promo_keyword(self, packet):
        # Fungsi untuk mendeteksi kata kunci 'promo' dalam paket jaringan menggunakan Scapy
        if packet.haslayer(Raw):
            raw_data = packet[Raw].load.decode(errors='ignore')
            if 'promo' in raw_data.lower():
                return True
        return False

# Contoh penggunaan:
promo_gen = PromoGenerator()

# Contoh mendapatkan harga tiket pesawat dan menghitung diskon secara paralel
price, discount = promo_gen.parallel_processing()
print("Harga tiket pesawat: {} {}".format(price, promo_gen.currency))
print("Diskon: {} {}".format(discount, promo_gen.currency))

# Contoh menghasilkan kode promosi
promo_code = promo_gen.generate_promo_code()
print("Kode promosi: {}".format(promo_code))

# Contoh pemrosesan pembayaran
payment_success = promo_gen.process_payment(price - discount)
if payment_success:
    print("Pembayaran berhasil!")
else:
    print("Pembayaran gagal!")

# Contoh mendeteksi kata kunci 'promo' dalam paket jaringan
def packet_callback(packet):
    if promo_gen.detect_promo_keyword(packet):
        print("Ditemukan kata kunci 'promo' dalam paket jaringan!")

# Gunakan sniff dari Scapy untuk memantau lalu lintas jaringan
# Anda dapat menyesuaikan filter sesuai kebutuhan Anda
sniff(prn=packet_callback, filter="tcp port 80", store=0)
