l = "Введите длину"


def check_user(text):
    try:
        number = int(input(f"{text}: "))
        return number
    except:
        print("Ошибка ввода")


l = check_user(l)
