#rounds = 5
#while rounds != 0:
 #   print(rounds)
  #  rounds -=

cash = 2091093
percents = 50
years = 7
print(cash)
for i in range(1,years+1):
    cash += cash * percents
    print(f'годы: {i} >> {round(cash,0)}')
