# deneme={
#     "1.ders":"matematik",
#     "2.ders":"sosyal",
#     "3.ders":"fen"
# }

# print(deneme["1.ders"])

# for key in deneme:
#     print(key)





# students_score = {
#     "harry": 81,
#     "ron": 78,
#     "hermonie": 99,
#     "draco": 74,
#     "neville": 62,
# }

# sinif = {
#     "mükemmel": [],
#     "iyi": [],
#     "kaldın": [],
# }

# for student, score in students_score.items():
#     if score >= 80:
#         sinif["mükemmel"].append(student)
#     elif score >= 70:
#         sinif["iyi"].append(student)
#     else:
#         sinif["kaldın"].append(student)

# print(sinif)


# for category, students in sinif.items():
#     print(f"{category.capitalize()}: {', '.join(students)}")

# travel_log = [
#     {
#         "ülke": "france",
#         "şehir-ziyaretleri": ["paris", "lille", "djon"],
#         "total_visit": 12
#     },
#     {
#         "ülke": "türkiye",
#         "şehir-ziyaretleri": ["istanbul", "çankırı", "ayvalık"],
#         "total_visit": 5
#     },
# ]

# def add_new_country(ülke,şehirler,total_visit):
#     new_country = {}
#     new_country["ülke"] = ülke
#     new_country["şehir-ziyaretleri"] = şehirler
#     new_country["total_visit"] = total_visit
#     travel_log.append(new_country)


# add_new_country("Russia",["Moscow", "Saint Petersburg"],2)

# print(travel_log)


verenler=[
    {
        
    }
]

n = int(input("ilana kaç kişi katılabilir"))

for i in range(n):
    ad=input("adınız")
    teklif = int(input("teklifiniz"))
    ekle={}
    ekle["ad"]=ad
    ekle["para"]=teklif
    verenler.append(ekle)
print(verenler)


k_teklif=0
kazanan=None

for i in verenler:
    if "para" in i:
        if i["para"]>k_teklif:
            k_teklif=i["para"]
            kazanan=i["ad"]

print(f"en yüksek teklif ile kazanan {kazanan}")
