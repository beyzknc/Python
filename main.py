baslik = "HABERİNİZ OLSUN" #string
vade = 12 #integer
faizOrani1 = 1.47 #float
faizOrani2 = 1.44
faizOrani = 1.47

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi = "Beyza"
musteriSoyadi = "Kınacı"
# print(mesaj+" "+musteriAdi+" "+musteriSoyadi)
sonucMesaj = mesaj+" "+musteriAdi+" "+musteriSoyadi

print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1+sayi2)

print(sonucMesaj)

#..............................................

dolarDun = 13.75
dolarBugun = 13.50

if dolarDun>dolarBugun:
    print("Azalış oku")
    print("Bitti")
elif dolarDun<dolarBugun: 
    print("Artış oku")
else:
     print("eşittir oku")

print("Bitti")

# if dolarDun<dolarBugun:
#    print("Artış oku")

#if dolarDun==dolarBugun:
#    print("eşittir oku")

#..............................................

# Bölüm ödevi 1

number1 = 30
number2 = 23

if number1 > number2:
    print("Birinci sayı büyüktür")

elif number1 < number2:
    print("İkinci sayı büyüktür")

else :
    print("Sayılar birbirine eşittir")

#.............................................

# Bölüm ödevi 2

sayi_1 = 14
sayi_2 = 9
sayi_3 = 2

if sayi_1<sayi_2 and sayi_1<sayi_3:
    print("1. sayı küçüktür =")
    print(sayi_1)

elif sayi_2<sayi_1 and sayi2<sayi_3:
    print("2. sayı küçüktür =") 
    print(sayi_2)
    
else :
    print("3. sayı küçüktür =")
    print(sayi_3)



if sayi_1>sayi_2 and sayi_1>sayi_3:
    print("1. sayı büyüktür =")
    print(sayi_1)

elif sayi_2>sayi_1 and sayi2>sayi_3:
    print("2. sayı büyüktür =") 
    print(sayi_2)
    
else :
    print("3. sayı büyüktür =")
    print(sayi_3)

#.......................................

# Bölüm ödevi 3

# Altın fiyatlarının durumu artış azalış 
# veya sabit okları şarta bağlı değişkenlerdir.


