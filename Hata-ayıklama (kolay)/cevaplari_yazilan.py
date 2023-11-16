############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
#  CEVAP: i 20 ye ulaşamadığı için you got it i yazdıramıyor



# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

#  CEVAP : # dice_num = randint(0, 6) 






# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# CEVAP if year > 1980 and year <= 1994:




# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# CEVAP  kodların düzeltilmiş hali
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")




# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# cevap word_per_page = int(input("Number of words per page: "))  '==' yerine tek '=' kullanımı ile veri değeri değiştirilebilir





# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#  CEVAP      b_list.append(new_item) boşluk ile new_item ile aynı dizine gelmesi lazım 