#bankamatik uygulaması
musteri_bilgileri = {
'hesap_1' : {'hesap_no' : '12345678', 'ad': 'Enes', 'bakiye' : 3000, 'ek_hesap' : 2000},
'hesap_2' : {'hesap_no' : '87654321', 'ad': 'Salih Asaf', 'bakiye' : 2000, 'ek_hesap' : 1000}
}


def para_cek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    # cekilecek_para = int(input('Çekmek İstediğiniz Miktarı Giriniz: '))
    if (miktar <= hesap['bakiye']):
       hesap['bakiye'] -= miktar
       print(f'''paranızı alınız, hesabınızda {hesap['bakiye']} TL kalmıştır''')
    else:
        toplam = hesap['bakiye'] + hesap['ek_hesap']
        if miktar <= toplam :
             sorgu = input(f'Çekmek istediğiniz miktar bakiyede bulunmamaktadır. Ek hesabı kullanmak ister misiniz: ').lower()
             if sorgu == 'evet' :
                #print(f"çekmek istediğiniz miktar için ek hesap kullanılmıştır hesabınız -{miktar-hesap['bakiye']-hesap['ek_hesap']} TL dir")
                hesap['ek_hesap'] = (hesap['bakiye'] + hesap['ek_hesap']) - (miktar)
                hesap['bakiye'] = 0
                print(f"çekmek istediğiniz miktar için ek hesap kullanılmıştır hesabınız {hesap['ek_hesap']} TL dir")

             else:
                  print('Lütfen Çekmek istediğiniz miktarı düzelterek tekrar giriniz')
                  miktar = int(input('Çekmek istediğiniz miktarı giriniz: '))
                  hesap['bakiye'] -= miktar
                  print(f"paranızı alınız. hesabınızda {hesap['bakiye']} TL kalmıştır")
        else:
            print(f"yetersiz bakiye....!!!! lütfen paranız kadar koşusun... hesabınıza tanımlı toplam {hesap['bakiye'] + hesap['ek_hesap']} TL vardır")
            miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
            if (miktar <= hesap['bakiye']):
                hesap['bakiye'] -= miktar
                print(f"paranızı alınız hesabınızda {hesap['bakiye']} TL kalmıştır")
            else:
                toplam = hesap['bakiye'] + hesap['ek_hesap']
                if miktar <= toplam :
                   sorgu = input(f'Çekmek istediğiniz miktar bakiyede bulunmamaktadır. Ek hesabı kullanmak ister misiniz(evet/hayır): ').lower()
                   if sorgu == 'evet':
                       hesap['ek_hesap'] = (hesap['bakiye'] + hesap['ek_hesap']) - (miktar)
                       hesap['bakiye'] = 0
                       print(f"çekmek istediğiniz miktar için ek hesap kullanılmıştır hesabınız {hesap['ek_hesap']} TL dir")
                   else:
                       print('Lütfen Çekmek istediğiniz miktarı düzelterek tekrar giriniz')
                       miktar = int(input('Çekmek istediğiniz miktarı giriniz: '))
                       hesap['bakiye'] -= miktar
                       print(f"paranızı alınız. hesabınızda {hesap['bakiye']} TL kalmıştır")

def bakiye_sorgula(hesap):
    print(f"""{hesap['hesap_no']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.\nEk hesap limitiniz {hesap['ek_hesap']} TL dir""")

def para_yatir(hesap,nakit):
    print(f"""Merhaba {hesap['ad']}\nHesabınıza {nakit} TL yatırılıyor.\nLütfen Bekleyiniz....""")
    hesap["bakiye"] = hesap["bakiye"] + nakit
    print(f"""Sayın {hesap['ad']} Paranız Hesabınıza Yatırılmıştır\nHesabınızda {hesap['bakiye']} bulunmaktadır""")

def islem_sec():
    hesap_adı = input("İşlem yapmak istediğiniz hesabı seçiniz: ")
    print(f"Merhaba {musteri_bilgileri[hesap_adı]['ad']}")

    while True:
        print("*" * 75)
        islem_turu = input("""Hoşgeldiniz\nPara Çekmek için (pc)\nPara Yatırmak için (py)\nBakiye sorgulamak için (bs)\nUygulamadan çıkmak için (q) kısa yollarını kullanınız\nLütfen Yapmak istediğiniz işlemin kısayolunuz yazınız (pc/py/bs/q): """)
        if islem_turu == "pc":
            print(f"""Hesabınızda {musteri_bilgileri[hesap_adı]['bakiye']} TL bulunmaktadır\nEk hesap limitiniz {musteri_bilgileri[hesap_adı]['ek_hesap']} TL dir.""")
            cekilen_miktar = int(input("Çekmek İstediğiz Miktarı Giriniz: "))


            para_cek(musteri_bilgileri[hesap_adı],cekilen_miktar)

        elif islem_turu == "py":
            yatirilan_miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
            para_yatir(musteri_bilgileri[hesap_adı],yatirilan_miktar)

        elif islem_turu == 'bs':
            bakiye_sorgula(musteri_bilgileri[hesap_adı])

        elif islem_turu == "q":
            break



islem_sec()
