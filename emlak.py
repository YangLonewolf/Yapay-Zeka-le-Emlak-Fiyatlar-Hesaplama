import pandas as pd
import matplotlib as plt
from sklearn import linear_model

df = pd.read_csv("csv dosyası nerede ise orayı buraya yapıştırın",sep=";")

#linear regresyonunu tanımlıyoruz

reg = linear_model.LinearRegression()
reg.fit(df[["alan","odasayisi","binayasi"]],df["fiyat"])

#prediction yapalım
while True:
    try:
        alan = int(input("mertrekaresini girin:"))
        oda_sayisi = int(input("Oda sayısı girin:"))
        bina_yasi = int(input("Bina yaşını giriniz:"))
        a = reg.predict([[alan,oda_sayisi,bina_yasi]])
        print(a)
    except:
        print("Lütfen Sayı Giriniz")
        pass
