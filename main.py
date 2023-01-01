def wire_resistance():
    """
    Расчёт сопротивления проводов АКБ.
    :return: вернуть полученное сопротивление
    """

    current_of_wire = [
        0.5, 0.75, 1, 1.5, 2.5,
        4, 6, 10, 16, 25,
        35, 50, 70, 95]
    # Проверить ввод, сечение должно быть в диапазоне словаря
    while True:
        try:
            s = int(input("поперечное сечение (мм2): "))
            if s in current_of_wire:
                break
            else:
                print("Такого сечения нет. Попробуйте снова")
        except:
            print("Ошибка ввода данных, вводите фигню какую то")

    # Проверить ввод, длина должна быть целым число и больше нуля
    while True:
        try:
            l = abs(int(input("Введите длину перемычки между АКБ (мм): ")))
            l_positive = abs(int(input("Введите длину провода от автомата до плюсовой клеммы первого АКБ (мм): ")))
            l_negative = abs(int(input("Введите длину провода от автомата до отрицательной клеммы последнего АКБ (мм): ")))
            break
        except:
            print("Ошибка ввода длинны")

    r_wires = round(((0.017 * (l+l_positive+l_negative)) / s), 2)  # Удельное сопротивление меди 0,017

    print("Удельное сопротивление проводника: ", r_wires)

    return r_wires


def short_circuit_current():
    """
    Расчёт ток КЗ для одного АКБ
    :return: возвращаем значение тока КЗ
    """

    u = int(input("Введите напряжение АКБ (В): "))
    r_internal = int(input("Введите внутреннее сопротивление АКБ (мОм) "))

    r_internal = r_internal / 1000  # Перевод мОм в Ом

    i_acc = u / r_internal
    print("Ток короткого замыкания АКБ: ", i_acc)

    return i_acc


wire_resistance()
short_circuit_current()
