import web
import requests
import socket
import threading
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import get_web  # Import modul get-web.py

# Global variable untuk menandai status
global no

def main():
    # Memulai proses identifikasi potongan
    potongan = identifikasi_potongan()
    
    # Memulai proses pencarian harga termurah dengan e-wallet android
    harga_murah = cari_harga_murah(e_wallet="android", currency="USD")

    # Melakukan penukaran dengan harga tiket pesawat bersama dengan diskon
    penukaran = lakukan_penukaran(harga_murah, potongan)

    # Mengirimkan hasil penukaran ke web.py
    web.kirim_hasil_penukaran(penukaran)

    # Mendapatkan kode kupon dan voucher dari host.json menggunakan fitur di get-web.py
    kode_kupon = get_web.get_kode_kupon()
    voucher = get_web.get_voucher()

def identifikasi_potongan():
    # Fungsi ini akan mengidentifikasi potongan
    return True  # Contoh sederhana, dapat disesuaikan dengan logika yang sesuai

def cari_harga_murah(e_wallet, currency):
    # Fungsi ini akan mencari harga murah dengan e-wallet dan mata uang tertentu
    # Contoh sederhana, menggunakan pandas untuk mencari kata kunci "price"
    data = {'item': ['Tiket Pesawat', 'Hotel', 'Paket Liburan'],
            'price': [100, 200, 300]}  # Data sementara
    
    df = pd.DataFrame(data)
    if 'price' in df.columns:
        print("Kata kunci 'price' ditemukan dalam data.")
    else:
        print("Kata kunci 'price' tidak ditemukan dalam data.")
    
    # Logika pencarian harga murah bisa ditambahkan di sini
    return 100  # Contoh sederhana, dapat disesuaikan dengan logika yang sesuai

def lakukan_penukaran(harga, potongan):
    # Fungsi ini akan melakukan penukaran dengan harga tiket pesawat bersama dengan diskon
    return harga * 0.9 if potongan else harga  # Contoh sederhana, dapat disesuaikan dengan logika yang sesuai

if __name__ == "__main__":
    main()
