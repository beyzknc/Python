workshop2 = open("employees.txt", "a")
workshop3 = open("employees.txt", "r")
oku = workshop3.read()

try:
    employeesCount = int(input("Calisan sayisi giriniz"))
    
    for i in range(employeesCount):
        isim = str(input("Calisan ismi giriniz"))
        soyIsim = str(input("Calisan soyismi giriniz"))
        maas = int(input("Calisan maasi giriniz"))

        
        workshop2.write(f"{isim}, {soyIsim}, {maas}\n")
       
except:
     print("Hatali giris yaptiniz.")

finally:
    print("Calisan Kaydedildi.")
    workshop2.close()

print(oku)