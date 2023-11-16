import random

rastgele_sayi = random.randint(1,100)
print (rastgele_sayi)

print('Aklımdan 1-100 arasında bir sayı tutuyorum \n orun kolay mı olsun zor mu ')
zorluk = input('zorluğu yaz: ').lower()
can = 5
if zorluk == 'zor':
    print('5 hakkın var')
    for i in range(1,6):
        print(rastgele_sayi)
        tahmin = int(input('sayıyı tahminin nedir: '))
        can -=1
        if tahmin == rastgele_sayi:
            print('tebrikler sayıyı buldun')
            break
        elif can == 0:
            print('canların bitti')
            break
        print (' kalan can: ',can)
        if rastgele_sayi + 10 > tahmin > rastgele_sayi-10:
            print('sayıya çok yakınsın')
        elif rastgele_sayi + 20 > tahmin > rastgele_sayi -20:
            print('sayıya yaklaştın')
        elif rastgele_sayi + 30 > tahmin > rastgele_sayi -30:
            print('sayıya uzaksın')
        elif rastgele_sayi + 40 > tahmin > rastgele_sayi -40:
            print('sayıya çok uzak')
        else:
            print('sayıya alakan yok')
        
else:
    can = 10
    for i in range(1,11):
        print(rastgele_sayi)
        tahmin = int(input('sayıyı tahminin nedir: '))
        can -=1
        if tahmin == rastgele_sayi:
            print('tebrikler sayıyı buldun')
            break
        elif can == 0:
            print('canların bitti')
            break
        print (' kalan can: ',can)
        if rastgele_sayi + 10 > tahmin > rastgele_sayi-10:
            print('sayıya çok yakınsın')
        elif rastgele_sayi + 20 > tahmin > rastgele_sayi -20:
            print('sayıya yaklaştın')
        elif rastgele_sayi + 30 > tahmin > rastgele_sayi -30:
            print('sayıya uzaksın')
        elif rastgele_sayi + 40 > tahmin > rastgele_sayi -40:
            print('sayıya çok uzak')
        else:
            print('sayıya alakan yok')



