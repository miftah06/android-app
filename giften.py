from googlesearch import search
import random

def generate_gift_code():
    code_length = 8
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    gift_code = ''.join(random.choice(characters) for _ in range(code_length))
    return gift_code

def generate_keyword_list():
    # Membaca kata kunci dari file keyword.txt
    with open("keyword.txt", "r") as file:
        keywords = file.readlines()
        keywords = [keyword.strip() for keyword in keywords if keyword.strip()]
    return keywords

def search_google(keyword):
    # Mencari di Google menggunakan kata kunci tertentu
    search_results = search(keyword, num=5, stop=5, pause=2)
    return search_results

def main():
    # Menghasilkan kata kunci dari file keyword.txt
    keywords = generate_keyword_list()

    for keyword in keywords:
        # Mencari di Google dengan kata kunci tertentu
        search_results = search_google(keyword)

        print(f"Hasil pencarian untuk kata kunci '{keyword}':")
        for idx, result in enumerate(search_results, start=1):
            print(f"{idx}. {result}")

        # Menghasilkan dan mencetak kode hadiah
        gift_code = generate_gift_code()
        print(f"Gift code untuk kata kunci '{keyword}': {gift_code}")
        print()

if __name__ == "__main__":
    main()
