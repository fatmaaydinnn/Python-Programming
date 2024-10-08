###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)


y = 3.2
type(y)


z = 8j + 18
type(z)


a = "Hello World"
type(a)

b = True
type(b)


c = 23 < 22
c


l = [1, 2, 3, 4,"String",3.2, False]
type(l)



d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)


t = ("Machine Learning", "Data Science")
type(t)




s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)




###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
text.upper()
text.split()




###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.

len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.


lst[0]
lst[10]


# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

lst[0:4]


# Adım 4: Sekizinci index'teki elemanı silin.


lst.pop(8)

# Adım 5: Yeni bir eleman ekleyin.

lst.append(5)

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.append("N")

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"]=["England,13"]


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.


type(dict)
dict.items()
dict.update ({ "Ahmet": ["Turkey",24]})



# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

list = [2,13,18,93,22]

pair_new=[]
odd_new=[]
type(list)
def handleNumbers(list):
    pair_new=[]
    odd_new=[]
    for number in list:
        if number %2==0:
        pair_new.append(number)
        else:
        odd_new.append(number)


def hadleNumbers(list):
    pair_new=[]
    odd_new=[]
    for number in list:
        if number %2==0:
            pair_new.append(number)
        else:
            odd_new.append(number)
    return pair_new,odd_new



###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

students = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]


for index, student in enumerate(students):
    if index<3:
        print(f"Müğendislik Fakültesi {index+1}.student:{student}")
    else:
        print(f"Tıp Fakültesi {index -2}.student:{student}")

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu,kredi,kontenjan))



###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume_karsilastirma(k1, k2):
    if k1.issuperset(k2):
        kesisim = k1.intersection(k2)
        print(f"k1 k2 yi kapsiyor. Iki kumenin ortak elemanlari {kesisim}")
    else:
        fark = k2.difference(k1)
        print(f"K1 k2  kapsamiyor. k2'nin k1'den farki {fark}")

kume_karsilastirma(kume1, kume2)