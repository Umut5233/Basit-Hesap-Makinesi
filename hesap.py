sistem = True

while sistem:
    print("HESAP MAKİNESİ")
    print("                 ")
    girdi1 = input("Bir sayı giriniz:                            (Çıkmak için 'q' yazınız.)")

    if girdi1.lower() == 'q':
        print("Program kapatılıyor...")
        break

    girdi2 = input("Bir sayı daha giriniz:                       (Çıkmak için 'q' yazınız.)")

    if girdi2.lower() == 'q':
        print("Program kapatılıyor...")
        break

    try:
        sayı1 = float(girdi1)
        sayı2 = float(girdi2)
  

    except ValueError:
        print("                 ")
        print("HATA!")
        print("Yanlış giriş yaptınız lütfen sadece sayı yazınız.")
        continue


    işlem = input("Yapmak istediğiniz işlemi yazınız:    (çarpma,toplama.çıkarma.bölme)")

    if işlem.lower() == "çarpma":
        sonuç = sayı1 * sayı2
        print(sonuç)

    elif işlem.lower() == "toplama":
        sonuç = sayı1 + sayı2
        print(sonuç)

    elif işlem.lower() == "çıkarma":
        sonuç = sayı1 - sayı2
        print(sonuç)

    elif işlem.lower() == "bölme":
        if sayı2 == 0:
            print("HATA! Bir sayı sıfıra bölünemez")
        else:
            sonuç = sayı1 / sayı2
            print(sonuç)


    else:
        print("                 ")
        print("HATA!")
        print("Lütfen belirtilen işlemlerden birini yazınız.")
        print("Sistem Yeniden Başlatılıyor...")
