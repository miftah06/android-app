import random
import requests
from bs4 import BeautifulSoup
import numpy as np
import threading
import json

# Fungsi untuk mengacak kode promo
def generate_promo_code():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    promo_code = ''.join(random.choices(characters, k=8))
    return promo_code

# Fungsi untuk penukaran kupon
def redeem_promo_code(promo_code, expiration_date):
    # Logika penukaran kupon dan pemberian diskon
    # Anda dapat menambahkan logika ini sesuai kebutuhan
    print("Voucher dengan kode {} telah ditukarkan. Tanggal kedaluwarsa: {}".format(promo_code, expiration_date))

# Fungsi untuk menampilkan pesan banner
def show_banner_message():
    banner_msg = "Selamat datang di aplikasi penukaran kupon! Silakan pilih situs web tempat Anda ingin menukarkan kupon."
    print(banner_msg)

# Fungsi untuk melacak kata kunci "link free" dan "discount"
def track_keywords(text):
    keywords = ["link free", "discount"]
    for keyword in keywords:
        if keyword in text:
            return keyword
    return None

# Fungsi untuk mengakses dan mengekstrak informasi dari URL
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Lakukan ekstraksi informasi yang diperlukan dari halaman web
            # Anda dapat menambahkan logika ekstraksi ini sesuai kebutuhan
            return soup
        else:
            print("Gagal mengakses halaman web.")
            return None
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return None

# Fungsi untuk melakukan pencarian dengan threading
def perform_search(keyword, urls):
    results = []
    for url in urls:
        thread = threading.Thread(target=search_keyword, args=(keyword, url, results))
        thread.start()
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    return results

# Fungsi untuk mencari kata kunci di halaman web
def search_keyword(keyword, url, results):
    soup = scrape_website(url)
    if soup:
        text = soup.get_text()
        if keyword in text:
            results.append(url)

# Main program
if __name__ == "__main__":
    # Tampilkan pesan banner
    show_banner_message()
    
    # Baca daftar URL situs web dari file host.json
    try:
        with open("host.json", "r") as file:
            data = json.load(file)
            website_urls = data["websites"]
    except FileNotFoundError:
        print("File host.json tidak ditemukan.")
        exit()
    
    # Kata kunci yang ingin dicari
    search_keyword = "discount"
    
    # Melakukan pencarian dengan threading
    search_results = perform_search(search_keyword, website_urls)
    
    # Menampilkan hasil pencarian
    print("Hasil pencarian untuk kata kunci '{}' :".format(search_keyword))
    for result in search_results:
        print("- ", result)
    
    # Meminta input link, kode voucher, dan tanggal kedaluwarsa voucher
    voucher_link = input("Masukkan link voucher yang ingin ditukarkan: ")
    voucher_code = input("Masukkan kode voucher: ")
    expiration_date = input("Masukkan tanggal kedaluwarsa voucher (format: YYYY-MM-DD): ")
    
    # Melakukan penukaran voucher
    redeem_promo_code(voucher_code, expiration_date)
