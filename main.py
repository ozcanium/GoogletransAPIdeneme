import pandas as pd
from googletrans import Translator

translator = Translator()

word_tr = ["Kırmızı","Mavi", "Yeşil", "Gri", "Pembe", "Mor", "Siyah", "Beyaz", "Toz Pembe", "Uzay Grisi","Seni Seviyorum"]

df = pd.DataFrame(columns=["Türkçe", "İngilizce", "Fransızca",
                           "Almanca","İspanyolca","Arapça","Rusça","İtalyanca", "Bulgarca"])

for word in word_tr:
    df = pd.concat([df, pd.DataFrame([{
        "Türkçe": word,
        "İngilizce": translator.translate(word, dest="en").text,
        "Fransızca": translator.translate(word, dest="fr").text,
        "Almanca": translator.translate(word, dest="de").text,
        "İspanyolca": translator.translate(word, dest="es").text,
        "Arapça": translator.translate(word, dest="ar").text,
        "Rusça": translator.translate(word, dest="ru").text,
        "İtalyanca": translator.translate(word, dest="it").text,
        "Bulgarca": translator.translate(word, dest="bg").text
    }])], ignore_index=True)
    print(df)
