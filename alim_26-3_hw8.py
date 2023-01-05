low = 0
high = 100
guesses = []


def print_result(result):
    print(f"Число: {result}")
    with open("results.txt", "w", encoding='utf-8') as file:
        file.write(f"Количество попыток: {len(guesses)}\n")
        file.write("Попытки: " + ", ".join(str(g) for g in guesses) + "\n")
        file.write(f"Число: {result}")
        while low != high:
            guess = (low + high) // 2
            guesses.append(guess)

            response = input(
                f"Число {guess}? Введите 'больше', если число больше, 'меньше', если число меньше, или 'да', если число верное: ")
            if response == "больше":
                low = guess + 1
            elif response == "меньше":
                high = guess - 1
            elif response == "да":
                high = guess
                low = guess
            else:
                print("Неверный ввод. Пожалуйста, введите 'больше', 'меньше' или 'да'.")

        print_result(high)


while low != high:
    guess = (low + high) // 2
    guesses.append(guess)

    response = input(
        f"Число {guess}? Введите 'больше', если число больше, 'меньше', если число меньше, или 'да', если число верное: ")
    if response == "больше":
        low = guess + 1
    elif response == "меньше":
        high = guess - 1
    elif response == "да":
        high = guess
        low = guess
    else:
        print("Неверный ввод. Пожалуйста, введите 'больше', 'меньше' или 'да'.")
