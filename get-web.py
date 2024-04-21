import web
import promos
import kode
import requests
import socket
import pandas as pd
import numpy as np
import threading

def main():
    # Contoh penggunaan fungsi-fungsi dari modul web.py, promos.py, dan kode.py
    web.web_function()
    promos.promo_function()
    kode.kode_function()

    # Fungsi dan fitur baru yang ditambahkan
    print("Memulai proses untuk mendapatkan data dari web...")
    web_data = web.get_web_data()
    print("Data berhasil didapatkan.")
    print("Memulai proses untuk mendapatkan promo...")
    promo_data = promos.get_promo_data()
    print("Promo berhasil didapatkan.")
    print("Memulai proses untuk mendapatkan kode...")
    kode_data = kode.get_kode_data()
    print("Kode berhasil didapatkan.")

    # Mengeksekusi fungsi untuk mendeteksi kata kunci diskon menggunakan threading
    print("Memulai proses deteksi kata kunci diskon...")
    thread = threading.Thread(target=detect_diskon_keywords)
    thread.start()
    thread.join()
    print("Proses deteksi kata kunci diskon selesai.")

def detect_diskon_keywords():
    # Fungsi ini akan menggunakan threading untuk mendeteksi kata kunci diskon
    pass

if __name__ == "__main__":
    main()
