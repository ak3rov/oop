date=int(input("Введите день рождения:"))
month=int(input("Введите месяц рождения:"))
year=int(input("Введите год рождения:"))
if (date>=21 and date<=31 and month==3) or( month==4 and date>=1 and date<=19):
   print("Ваш знак зодиака:Овен")
elif (date>=20 and date<=30 and month==4) or( month==5 and date>=1 and date<=20):
   print("Ваш знак зодиака:Телец")
elif (date>=21 and date<=31 and month==5) or( month==6 and date>=1 and date<=21):
   print("Ваш знак зодиака:Близнецы")
elif (date>=22 and date<=30 and month==6) or( month==7 and date>=1 and date<=22):
   print("Ваш знак зодиака:Рак")
elif (date>=23 and date<=31 and month==7) or( month==8 and date>=1 and date<=22):
   print("Ваш знак зодиака:Лев")
elif (date>=23 and date<=31 and month==8) or( month==9 and date>=1 and date<=22):
   print("Ваш знак зодиака:Дева")
elif (date>=23 and date<=30 and month==9) or( month==10 and date>=1 and date<=23):
   print("Ваш знак зодиака:Весы")
elif (date>=24 and date<=31 and month==10) or( month==11 and date>=1 and date<=22):
   print("Ваш знак зодиака:Скорпион")
elif (date>=23 and date<=30 and month==11) or( month==12 and date>=1 and date<=21):
   print("Ваш знак зодиака:Стрелец")
elif (date>=22 and date<=31 and month==12) or( month==1 and date>=1 and date<=20):
   print("Ваш знак зодиака:Козерог")
elif (date>=21 and date<=31 and month==1) or( month==2 and date>=1 and date<=18):
   print("Ваш знак зодиака:Водолей")
elif (date>=19 and date<=29 and month==2) or( month==3 and date>=1 and date<=20):
   print("Ваш знак зодиака:Рыбы")
else :
   print('Не верно введен день,месяц или год ')