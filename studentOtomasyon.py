def ogrenci_ekle(ogrenci_listesi):
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")
    numara = input("Öğrencinin numarasını girin: ")
    bolum = input("Öğrencinin bölümünü girin: ")
    not_ort = float(input("Öğrencinin not ortalamasını girin: "))
    yeni_ogrenci = {
        "ad": ad,
        "soyad": soyad,
        "numara": numara,
        "bolum": bolum,
        "not_ort": not_ort
    }
    ogrenci_listesi.append(yeni_ogrenci)
    print("Öğrenci başarıyla eklendi!\n")
    
def ogrenci_listele(ogrenci_listesi):
    if not ogrenci_listesi:
        print("Henüz öğrenci eklenmemiş.\n")
    else:
        for ogrenci in ogrenci_listesi:
            print(f"{ogrenci['numara']}: {ogrenci['ad']} {ogrenci['soyad']}, Bölüm: {ogrenci['bolum']}, Not Ortalaması: {ogrenci['not_ort']}")
        print()

def ogrenci_goruntule(ogrenci_listesi):
    numara = input("Görüntülemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenci_listesi:
        if ogrenci["numara"] == numara:
            print(f"{ogrenci['numara']}: {ogrenci['ad']} {ogrenci['soyad']}, Bölüm: {ogrenci['bolum']}, Not Ortalaması: {ogrenci['not_ort']}")
            return
    print("Öğrenci bulunamadı!\n")

def ogrenci_guncelle(ogrenci_listesi):
    numara = input("Güncellemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenci_listesi:
        if ogrenci["numara"] == numara:
            ogrenci["ad"] = input("Yeni ad: ")
            ogrenci["soyad"] = input("Yeni soyad: ")
            ogrenci["bolum"] = input("Yeni bölüm: ")
            ogrenci["not_ort"] = float(input("Yeni not ortalaması: "))
            print("Öğrenci bilgileri güncellendi!\n")
            return
    print("Öğrenci bulunamadı!\n")

def ogrenci_sil(ogrenci_listesi):
    numara = input("Silmek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenci_listesi:
        if ogrenci["numara"] == numara:
            ogrenci_listesi.remove(ogrenci)
            print("Öğrenci başarıyla silindi!\n")
            return
    print("Öğrenci bulunamadı!\n")

ogrenciler = []
while True:
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Öğrenci Görüntüle")
    print("4. Öğrenci Güncelle")
    print("5. Öğrenci Sil")
    print("6. Çıkış")
    secim = input("Seçiminizi yapın: ")
    
    if secim == "1":
        ogrenci_ekle(ogrenciler)
    elif secim == "2":
        ogrenci_listele(ogrenciler)
    elif secim == "3":
        ogrenci_goruntule(ogrenciler)
    elif secim == "4":
        ogrenci_guncelle(ogrenciler)
    elif secim == "5":
        ogrenci_sil(ogrenciler)
    elif secim == "6":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin!\n")
