def main():
    kek = "shrek"
batken = float(input("Введите температуру в Баткене "))
chuy = float(input("Введите температуру в Чуйе "))
osh = float(input("Введите температуру в Оше "))
jlabd = float(input("Введите температуру в Джалал-Абаде "))
naryn = float(input("Введите температуру в Нарыне "))
isik_kol = float(input("Введите температуру в Ысык-Коле "))
talas = float(input("Введите температуру в Таласе "))
average_temp = (chuy + osh + jlabd + naryn + isik_kol + batken + talas) / 7
average_temp = round(average_temp,1)
print("Средний показатель температуры воздуха по КР на сегодня",average_temp,"'C")