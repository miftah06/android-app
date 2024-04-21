import random
import numpy as np
import requests
import socket
import queue
import pandas as pd
import json

def generate_gift_voucher():
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

def generate_coupons(num_coupons):
    coupons = np.random.randint(10000000, 99999999, size=num_coupons)
    return coupons

def generate_coupons_file(num_coupons):
    coupons = generate_coupons(num_coupons)
    with open("./coupons.txt", "w", encoding="utf-8") as coupons_file:
        for coupon in coupons:
            coupons_file.write(str(coupon) + "\n")
    print(f"{num_coupons} coupons telah dibuat dan disimpan dalam coupons.txt")

def main():
    with open("host.json", "r") as f:
        config = json.load(f)
        website = config.get("website", "default_website.com")

    num_coupons = 10

    # Membuat file coupons.txt dan menulis coupons ke dalamnya
    generate_coupons_file(num_coupons)

    # Menghasilkan promo code dan menerapkannya pada website
    promo_code = generate_promo_code(8)
    apply_promo_code(website, promo_code)

if __name__ == "__main__":
    main()
