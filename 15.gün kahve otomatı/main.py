from kahveler import *


def menu ():
    print('Menü')
    for sira,kahveler in enumerate(MENU,1):
        kahve_fiyat = MENU[kahveler]['cost']
        print(f" {sira}. {kahveler} = {kahve_fiyat} TL ")



def kaynak_deger():
    for kaynak,deger in resources.items():
        print(kaynak,deger)


def malzemeler ():
    for kahveler,ozellik in MENU.items():
        print("malzemeler:")
        for malzeme,miktar in ozellik["ingredients"].items():
            print(f" {malzeme}: {miktar} ")
        print(f" para: {ozellik['cost']}\n ")

def secim():
    kahve_secim=input('seçtiğiniz kahveyi yazınız: ')
    return kahve_secim


def kahve_hazırlanış():
    if secilen_kahve in MENU:
        kahve_detaylari = MENU[secilen_kahve]
        print(f"{secilen_kahve.capitalize()} kahvesinin detayları:")
        print(f"Malzemeler: {kahve_detaylari['ingredients']}")
        print(f"Maliyet: {kahve_detaylari['cost']}")
        
    else:
        print("Geçersiz kahve seçimi.")

def urun_eksiltme():
        kahve_parası=MENU[secilen_kahve]['cost']
        malzemeler = MENU[secilen_kahve]["ingredients"]
        if kahve_parası <= kasa:
            for malzeme, miktar in malzemeler.items():
                resources[malzeme] -= miktar
            print("Güncellenmiş kaynaklar:", resources)
            for malzeme,miktar in resources.items():
                if miktar <= 0:
                    print('kahve yapımı için malzemeler yetersizdir paranız iade ediliyor.')
                    exit()
            para_ustu=kasa-MENU[secilen_kahve]['cost']
            print(f"para üstü: {para_ustu} ")
        else:
            print('para yetersiz  paranız iade ediliyor')

def para_at():
    bozuk_para = int(input('bozukt para atınız: '))
    kagıt_para = int(input('kağıt para atın: '))
    toplam =bozuk_para+kagıt_para
    print(toplam)
    return toplam

def iptal_et():
    kullanıcı_iptal_btn = input('1 kahve daha alacakmasınız')
    if kullanıcı_iptal_btn == 'evet':
        return True
    else:
        return False


dongu=True

while  dongu:
    menu()
    kasa=int(para_at())
    secilen_kahve= secim()
    print(secilen_kahve)
    kahve_hazırlanış()
    urun_eksiltme()
    kullanıcı_iptal_btn = input('1 kahve daha alacakmasınız: ').lower()
    if kullanıcı_iptal_btn == 'evet':
        dongu =  True
    else:
        dongu = False