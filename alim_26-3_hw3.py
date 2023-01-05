# rus_alph = "йцукенгшщзхъфывапролджэячсмитьбю"
# eng_alph = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# while True:
#     word = input('\nвведите слово: ').lower()
#     for letter in word:
#         if letter in rus_alph:
#             print(eng_alph[rus_alph.index(letter)], end='')
#         else:
#             print(rus_alph[eng_alph.index(letter)], end='')
#     if word == 'exit' or word == 'выход' :
#         print('\nЗавершение работы...')
#         break
quest = int(input('Сколько будет строк? '))
gls = sgl=0
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я",'а','е','i','o','u','y']
# amount_letters = 16
# average_sum = vse_gls / amount_letters
# avarage_sum = '%.2f' % average_sum
count = 0
while quest > count:
    ls=gl=0
    word = input()
    for i in word:
        if i.isalpha():
            if i in vse_gls:
                ls += 1
            else:
                gl += 1
    print('Количество гласных:', ls,'Количество согласных:', gl)
    gls+=ls
    sgl+=gl
    count += 1

print('Количество гласных во всем тексте:', gls,'Количество согласных во всем тексте:', sgl)
# print(average_sum)



