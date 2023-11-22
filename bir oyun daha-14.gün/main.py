from veriler import veriler
from art import logo, vs


def ekran_temizle():
    print('\033c')




def sorular ():
    score=0
    print('gelecek sorulara şıklar halinde cevap vermeye çalışın')
    for sorunumarası , soru_verileri in veriler.items():
        print(logo)
        soru_metni = soru_verileri['soru']
        cevap = soru_verileri['cevap']
        print(f"soru: {soru_metni}")
        print(vs)
        kullanici_cevap=input('yanıtınızı giriniz: ')
        if kullanici_cevap == cevap:
            score += 1
            ekran_temizle()
            print('yanıtınız doğru ')
        else:
            print('cevabınız yanlış')
            print(f" doğru sayınız: {score} ")
            break

sorular()