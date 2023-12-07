#döngüler

# for i in range(10):
#     print(i)
    
# tek ve çift sayıları ayırma
# sayilar = [1,2,3,4,5,6,7,8,9,10]
# teksay = []
# çiftsay = []
# for i in sayilar:
#     if i % 2 == 0:
#         çiftsay.append(i)
#     else:
#         teksay.append(i)
# print(teksay)
# print(çiftsay)


# list = [1,3,2]
# minsay = 0
# maxsay = 0
# for i in list:
#     if minsay < i:
#         minsay =i
#     if maxsay > i:
#         maxsay = i
# print(minsay,maxsay)
        
# student_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95
# }

# for student, score in student_scores.items():
#     print(student,score)
#     print(student, "adlı öğrencinin notu:", score)

# 5 tane sayı girilsin ibput ile ve kaç defa döngüye girileceğini sorulsun

# s1 = int(input("sayı giriniz"))
# s2 = int(input("sayı giriniz"))
# s3 = int(input("sayı giriniz"))
# s4 = int(input("sayı giriniz"))
# s5 = int(input("sayı giriniz"))
# s6 = int(input("döngü kaç defa tekrar etsin"))

# list = [s1,s2,s3,s4,s5]

# for i in range(s6):
#     print(list)

#* while 

#faktoriyel hesaplama 

# n = 5
# fac = 1
# c = 1

# while c <= n:
#     fac *= c
#     c +=1
    
# print(fac) 

#! 1 den 10 a kadar olan tek sayıları yazdıran kodu bulalım

# list = []
# for i in range(1,10):
#     if i % 2 == 1:
#         list.append(i)
# print(list)

#! kullanıcının girdiği sayıları toplamını hesaplayın, ancak sayı 0 olduğunda hesaplamayı durdursun
# top = 0
# cikar = 50
# while(True):
#     soru = int(input("sayı girin"))
#     if soru ==0:
#         break
#     top+= soru
    
#! aşağıdaki cümlede kaç tane a ve e harfi bulunduğunu yazdıran çıktıyı bulalım

text = "bu gün pyhton tekrarı yapıyoruz"

# count_a = text.count("a")
# count_b = text.count("e")

# print(f"bu yazıda geçen a sayısı:{count_a} bu yazıda geçen e sayısı: {count_b}")

# a = 0
# e = 0
# for i in text:
#     if i =="a":
#         a +=1
#     elif i =="e":
#         e+=1
# print(a,e)      

#! her kelime içerisinde kaç tane e harfi olduğunu bulan kodu yazdıralım

# text1 = "her defasında ekinlerin biçenler ekmek için yemek yemeye geldiler"

# text2 = text1.split()
# for i in text2:
#     sayac = i.count("e")
#     print(f"{i} içerisinde {sayac} tane e vardır")













