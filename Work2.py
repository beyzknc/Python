
lessonCount = int(input("Kaç adet ders notu gireceksiniz?"))

passedExams = 0
failedExams  = 0

notlar = []
harfNotlari = []

for i in range(lessonCount):
    lessonExam1 = float(input(f"{i+1}. ders için vize notunuzu giriniz."))
    lessonExam2 = float(input(f"{i+1}. ders için final notunu giriniz."))
    totalExamNote = (lessonExam1 * 0.4) + (lessonExam2 * 0.6)
    notlar.append(totalExamNote)

    if totalExamNote >= 0 and totalExamNote < 50 :
        harfNotlari.append("FF")
    elif totalExamNote >= 50 and totalExamNote < 60 :
        harfNotlari.append("DD")
    elif totalExamNote >= 60 and totalExamNote < 70 :
        harfNotlari.append("CC")
    elif totalExamNote >= 70 and totalExamNote < 80 :
        harfNotlari.append("BB")
    else :
        harfNotlari.append("AA")

for j in range(len(notlar)):
    if (notlar[j]>=50):
         print(f"{j+1}. dersten geçtiniz. Notu:{notlar[j]} Harf notu: {harfNotlari[j]}")
    else:
        print(f"{j+1}. dersten kaldiniz. Notu:{notlar[j]} Harf notu: {harfNotlari[j]} ")


