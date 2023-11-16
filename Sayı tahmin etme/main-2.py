import random

kolay_seviye = 10
zor_seviye = 5


def cevap_kontrol(tahmin,cevap,haklar):
    if cevap+5 > tahmin > cevap -5:
        print('çok yakınsınız')
        return haklar -1
    elif tahmin > cevap:
        print('yüksek bir tahminde bulundunuz')
        return haklar -1
    elif tahmin < cevap:
        print('düşük bir tahminde bulundunuz')
        return haklar -1
    else:
        print(f"tebrikler cevap {cevap} idi")

def zorluk_belirleme():
    zorluk = input('zorluk seçin kolay/zor').lower()
    if zorluk == 'kolay':
        return kolay_seviye
    else:
        return zor_seviye

def oyun ():
    print('sayı tahmin oyununa hoş geldiniz')
    print('1-100 arasında bir sayı tutuldu')
    cevap = random.randint(1,100)
    haklar = zorluk_belirleme()
    tahmin = 0
    while tahmin != cevap:
        print(f"kalan haklar: {haklar}")
        tahmin = int(input('Bir tahmin yapın:'))
        
        haklar = cevap_kontrol(tahmin,cevap,haklar)
        if haklar == 0:
            print("Tahmin hakkınız bitti, kaybettiniz")
            return
        elif tahmin != cevap:
            print('Tekrar deneyiniz ')
oyun()