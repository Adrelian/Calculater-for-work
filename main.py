def check_user_input(text):
    """
    Функция проверяет пользовательский ввод. Если удается преобразовать в int, всё ОК. Иначе ошибка.
    :param text: Тест сообщения, для того, что бы пользователь понимал, что нужно вводить.
    :return: возвращает число после проверки.
    """
    try:
        number = int(input(f"{text}: "))
        return number
    except:
        print("Ошибка ввода")


def wire_resistance():
    """
    Расчёт сопротивления проводов АКБ.
    :return: вернуть полученное сопротивление
    """

    current_of_wire = [0.5, 0.75, 1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95]  # Возможные сечения кабеля
    # Проверить ввод, сечение должно быть в диапазоне словаря
    while True:
        try:
            s_text_for_user = "Введите поперечное сечение провода (мм2)"
            s = check_user_input(s_text_for_user)
            if s in current_of_wire:
                break
            else:
                print("Такого сечения нет. Попробуйте снова")
        except:
            print("Ошибка ввода данных, вводите фигню какую то")

    l_text_for_user = "Введите длину перемычки между АКБ (мм)"
    l = check_user_input(l_text_for_user)

    l_positive_text_for_user = "Введите длину провода от автомата до плюсовой клеммы первого АКБ (мм)"
    l_positive = check_user_input(l_positive_text_for_user)

    l_negative_text_for_user = "Введите длину провода от автомата до отрицательной клеммы последнего АКБ (мм)"
    l_negative = check_user_input(l_positive_text_for_user)

    common_l = (l + l_positive + l_negative) / 1000  # Общая длинна в метрах

    r_wires = round(((0.017 * common_l) / s), 2)  # Удельное сопротивление меди 0,017

    print(f"Удельное сопротивление проводника: {r_wires} Ом")

    return r_wires


def short_circuit_current(res_wire):
    """
    Расчёт тока короткого замыкания в схеме замещения АКБ.
    :param res_wire: сопротивление проводов.
    :return: значение тока КЗ.
    """

    u = int(input("Введите напряжение АКБ (В): "))

    r_internal_battery_text_for_user = "Введите внутреннее сопротивление АКБ (мОм)"
    r_internal_battery = check_user_input(r_internal_battery_text_for_user)

    quantity_battery_text_for_user = "Введите кол-во аккумуляторов"
    quantity_battery = check_user_input(quantity_battery_text_for_user)

    r_internal = r_internal_battery / 1000  # Перевод мОм в Ом

    i_acc = (u * quantity_battery) / (r_internal * quantity_battery + res_wire)  # Ток короткого замыкания
    print(f"Ток короткого замыкания АКБ: {round(i_acc)} A")

    return i_acc


def voltage_drop(resistance):
    current_circuit_section_text_for_user = "Введите ток потребителя"
    current_circuit_section = check_user_input(current_circuit_section_text_for_user)

    u = current_circuit_section * resistance  # Падение напряжения на участке цепи
    print(f'Падение напряжения для 1 метра кабеля будет составлять {u} V')



common_resistance_wire = wire_resistance()
short_circuit_current(common_resistance_wire)
voltage_drop(common_resistance_wire)
