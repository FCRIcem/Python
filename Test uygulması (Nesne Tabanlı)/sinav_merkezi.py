



class SinavHaritasi:
    def __init__(self,soru_list):
        self.soru_num = 0
        self.skor = 0
        self.soru_list = soru_list
    
    def hala_soru_var(self):
        if self.soru_num < len(self.soru_list):
            return True
        else:
            return False
    
    def yeni_soru (self):
        sorulan_soru = self.soru_list[self.soru_num]
        self.soru_num += 1
        kullanici_cevap = input(f"S.{self.soru_num}: {sorulan_soru.soru} (True/False): ")
        self.cevap_kontrol(kullanici_cevap,sorulan_soru.cevap)

    def cevap_kontrol (self,kullanici_cevap,soru_cevap):
        if kullanici_cevap.lower() == soru_cevap.lower():
            self.skor += 1
            print('cevabın doğru')
            
        else:
            print('cevabın yanlış ')
            print(f"doğru cevap: {soru_cevap} skorun: {self.skor}/{self.soru_num}")

