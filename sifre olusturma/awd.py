

import random

def shuffle_text(text):
    text_list = list(text)
    random.shuffle(text_list)
    shuffled_text = ''.join(text_list)
    return shuffled_text

metin = "Merhaba, dünya! 123"
karisik_metin = shuffle_text(metin)
print(karisik_metin)
