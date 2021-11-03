# Rastgele şifre üretmek için kullanıcağım kütüphane
import random

# Şifre içerisinde olmasını istediğimiz harf, rakam ve semboller
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHİJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#()*;,_-!%&/"

# Tüm harf, rakam ve sembolleri bir araya topla
all = lower + upper + number + symbol

# Oluşturacağım şifrenin uzunluğunu belirle
length = 18

# password değişkeninin içine random metodu ile length içerisinde belirlediğimiz uzunlukta şifre oluştur ve ata
password = "".join(random.sample(all,length))

# Ekrana yazdır.
print("Üretilen şifre = ",password)