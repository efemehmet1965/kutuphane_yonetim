import os

class Library:
    def __init__(self):
        self.dosya = open("books.txt", "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0) 
        kitaplar = self.dosya.read().splitlines()
        if kitaplar:
            for kitap in kitaplar:
                kitap_bilgileri = kitap.split(',')
                print(f"Adı: {kitap_bilgileri[0]}, Yazar: {kitap_bilgileri[1]}, Yıl: {kitap_bilgileri[2]}, Sayfa: {kitap_bilgileri[3]}")
        else:
            print("Kütüphanede kitap bulunmamaktadır.")
        print("\nMenüye dönmek için 'q' tuşuna basın.")
        while input().lower() != 'q':
            pass

    def kitap_ekle(self):
        ad = input("Kitabın adını girin: ")
        yazar = input("Yazarın adını girin: ")
        yil = input("İlk yayınlanma yılını girin: ")
        sayfa_sayisi = input("Sayfa sayısını girin: ")
        kitap_satiri = f"{ad},{yazar},{yil},{sayfa_sayisi}\n"
        self.dosya.write(kitap_satiri)
        self.dosya.flush()
        print(f"'{ad}' kitabı başarıyla eklendi.")
        print("\nMenüye dönmek için 'q' tuşuna basın.")
        while input().lower() != 'q':
            pass

    def kitap_sil(self):
        silinecek_ad = input("Kaldırmak istediğiniz kitabın adını girin: ")
        self.dosya.seek(0)
        satirlar = self.dosya.readlines()
        kitap_bulundu = False
        self.dosya.seek(0)
        self.dosya.truncate()
        for satir in satirlar:
            if satir.split(',')[0] != silinecek_ad:
                self.dosya.write(satir)
            else:
                kitap_bulundu = True
        self.dosya.flush()
        if not kitap_bulundu:
            print("Böyle bir kitap bulunamadı. Tam adını giriniz.")
        else:
            print(f"'{silinecek_ad}' adlı kitap başarıyla silindi.")
        print("\nMenüye dönmek için 'q' tuşuna basın.")
        while input().lower() != 'q':
            pass

def ekran_temizle():
    
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

def main():
    kutuphane = Library()
    while True:
        print("*** MENÜ ***\n1) Kitapları Listele\n2) Kitap Ekle\n3) Kitap Sil\n4) Çıkış")
        secim = input("Seçiminizi girin: ")
        if secim == "1":
            kutuphane.kitaplari_listele()
            ekran_temizle() 
        elif secim == "2":
            kutuphane.kitap_ekle()
            ekran_temizle() 
        elif secim == "3":
            kutuphane.kitap_sil()
            ekran_temizle() 
        elif secim == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            ekran_temizle()

if __name__ == "__main__":
    main()