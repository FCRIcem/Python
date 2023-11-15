# blackjack
import random
cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]

oyuncu_kartlari = random.sample(cards,2)
oyuncu_k_toplam =sum(oyuncu_kartlari)
kurpiyer_kartlari = random.sample(cards,1)
kurpiyer_kartlari2 = random.sample(cards,1)
kurpiyet_top_kart =sum(kurpiyer_kartlari+kurpiyer_kartlari2)





def para_aktarma(basla):
    global kasa
    kasa+=basla
    print(f"bahsiniz: {kasa}$")




def kartlari_dagıt():
    oyuncu_kartlari
    kurpiyer_kartlari
    oyuncu_k_toplam 
    print(f"Kurpiyerin Kartları : [ {kurpiyer_kartlari},~] \n sizin kartlarınız [ {oyuncu_kartlari} ] = {oyuncu_k_toplam} ")
    if oyuncu_k_toplam == 21:
        print('kazandınız')
    elif oyuncu_k_toplam > 21:
        print('kaybettiniz')
def kart_iste():
    global kurpiyer_kartlari
    global kurpiyet_top_kart
    global oyuncu_kartlari
    global oyuncu_k_toplam
    istek=input('kart istiyormusun: ')
    if istek == "e":
        istek_kart = random.sample(cards,1)
        istek_kart2 = istek_kart
        oyuncu_kartlari += istek_kart
        oyuncu_k_toplam += int(istek_kart2[0])
        
        print(f"Kurpiyerin Kartları : [ {kurpiyer_kartlari},{kurpiyer_kartlari2} = {kurpiyet_top_kart}] \n sizin kartlarınız [ {oyuncu_kartlari} ] = {oyuncu_k_toplam} ")
        if kurpiyet_top_kart < 17:
            while kurpiyet_top_kart <= 17:
                kurpiyer_kart_ekle = random.sample(cards,1)
                kurpiyer_kartlari += kurpiyer_kart_ekle
                kurpiyet_top_kart = sum(kurpiyer_kartlari)
                print(f"Kurpiyerin Kartları: {kurpiyer_kartlari} = {kurpiyet_top_kart}\nSizin Kartlarınız: {oyuncu_kartlari} = {oyuncu_k_toplam}")
            print(f"Kurpiyerin Kartları: {kurpiyer_kartlari} = {kurpiyet_top_kart}\nSizin Kartlarınız: {oyuncu_kartlari} = {oyuncu_k_toplam}")
            if kurpiyet_top_kart > oyuncu_k_toplam and kurpiyet_top_kart <= 21 or oyuncu_k_toplam > 21:
                print('Kaybettiniz')
            elif kurpiyet_top_kart == oyuncu_k_toplam or kurpiyet_top_kart > 21 and oyuncu_k_toplam > 21:
                print('berabere')
            else:
                print('kazandınız')
        elif kurpiyet_top_kart > oyuncu_k_toplam and kurpiyet_top_kart <= 21 or oyuncu_k_toplam > 21:
            print('Kaybettiniz')
        elif kurpiyet_top_kart == oyuncu_k_toplam or kurpiyet_top_kart > 21 and oyuncu_k_toplam > 21:
            print('berabere')
        else:
            print('kazandınız')
    else:
        if kurpiyet_top_kart < 17:
            while kurpiyet_top_kart <= 17:
                kurpiyer_kart_ekle = random.sample(cards,1)
                kurpiyer_kartlari += kurpiyer_kart_ekle
                kurpiyet_top_kart = sum(kurpiyer_kartlari)
                print(f"Kurpiyerin Kartları: {kurpiyer_kartlari} = {kurpiyet_top_kart}\nSizin Kartlarınız: {oyuncu_kartlari} = {oyuncu_k_toplam}")
            print(f"Kurpiyerin Kartları: {kurpiyer_kartlari} = {kurpiyet_top_kart}\nSizin Kartlarınız: {oyuncu_kartlari} = {oyuncu_k_toplam}")
            if kurpiyet_top_kart > oyuncu_k_toplam and kurpiyet_top_kart <= 21 or oyuncu_k_toplam > 21:
                print('Kaybettiniz')
            elif kurpiyet_top_kart == oyuncu_k_toplam or kurpiyet_top_kart > 21 and oyuncu_k_toplam > 21:
                print('berabere')
            else:
                print('kazandınız')
        else:
            print(f"Kurpiyerin Kartları: {kurpiyer_kartlari} = {kurpiyet_top_kart}\nSizin Kartlarınız: {oyuncu_kartlari} = {oyuncu_k_toplam}")
            if kurpiyet_top_kart > oyuncu_k_toplam:
                print('Kaybettiniz')
            elif kurpiyet_top_kart == oyuncu_k_toplam:
                print('berabere')
            else:
                print('kazandınız')
        



baslat = True
while baslat:
    kasa=0
    basla = int(input('kaç para yatırıyorsun: '))
    para_aktarma(basla)
    kartlari_dagıt()
    print(oyuncu_k_toplam)
    if oyuncu_k_toplam > 21 or oyuncu_k_toplam == 21:
        break
    kart_iste()
    if oyuncu_devam_istek == 'e':
        baslat = True
    else:
            baslat = False
    
    oyuncu_devam_istek=input('devam edecekmisiniz e/h: ').lower()
