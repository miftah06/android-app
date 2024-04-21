import random
import numpy as np
import requests
import json

def generate_voucher():
    voucher_length = 8
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    voucher = ''.join(random.choice(characters) for _ in range(voucher_length))
    return voucher

def generate_promo_code(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    promo_code = ''.join(random.choice(characters) for _ in range(length))
    return promo_code

def apply_promo_code(website, promo_code):
    # Logika untuk menerapkan promo code ke website
    print(f"Promo code {promo_code} telah diterapkan pada {website}")

def generate_coupons_and_titles():
    list_of_coupons_and_title = [
        {"coupon": generate_voucher(), "title": "Discount on item A"},
        {"coupon": generate_voucher(), "title": "Free shipping for item B"},
        {"coupon": generate_voucher(), "title": "50% off on item C"},
        {"coupon": generate_voucher(), "title": "Special offer for item D"},
    ]
    return list_of_coupons_and_title

def apply_coupons_to_items(list_of_coupons_and_title):
    for indx, coupon_and_title in enumerate(list_of_coupons_and_title):
        coupon = coupon_and_title["coupon"]
        title = coupon_and_title["title"]
        # Logika untuk menerapkan kupon pada item tertentu
        print(f"Kupon {coupon} ({title}) telah diterapkan pada item ke-{indx+1}")

def main():
    # Membaca konfigurasi website dari host.json atau package.name aplikasi
    with open("host.json", "r") as f:
        config = json.load(f)
        website = config.get("website", "default_website.com")

    # Atau jika ingin membaca dari package.name aplikasi, gantilah dengan cara yang sesuai
    # website = get_package_name()

    # Menghasilkan promo code dan menerapkannya pada website
    promo_code = generate_promo_code(8)
    apply_promo_code(website, promo_code)

    # Menghasilkan daftar kupon dan judul
    list_of_coupons_and_title = generate_coupons_and_titles()

    # Menerapkan kupon pada item-item
    apply_coupons_to_items(list_of_coupons_and_title)

if __name__ == "__main__":
    main()
