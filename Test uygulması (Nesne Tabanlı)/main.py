from data import *
from soru_model import *
from sinav_merkezi import *



soru_bankasi = []

for soru in soru_data:
    soru_metni = soru["question"]
    cevap = soru["correct_answer"]
    yeni_soru = Soru(soru_metni,cevap)
    soru_bankasi.append(yeni_soru)


sinav = SinavHaritasi(soru_bankasi)



while sinav.hala_soru_var():
    sinav.yeni_soru()
print(f"sonuc {sinav.skor}/{sinav.soru_num} ")