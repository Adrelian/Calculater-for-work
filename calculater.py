from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculater.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Рабочие действия для запуска приложения

# Словарь из необходимых электрических величин
electric_value = {
    'wire_cross_section': 0,  # Сечение провода
    'lenght_jumper_battery': 0,  # Длинна перемычек между АКБ
    'lenght_wire_to_positive': 0,  # Длинна до + контакта автомата
    'lenght_wire_to_negative': 0,  # Длинна до - контакта автомата
    'battery_voltage': 0,  # Напряжение одного АКБ
    'battery_internal_resistance': 0,  # Внутреннее сопротивление одного АКБ
    'battery_quantity': 0,  # Кол-во АКБ в щите
    'current_consumer': 0  # Ток потребителя
    }
# Словарь сечений проводов и их токов
value_wire = {
    "0.5": 11, '0.75': 15, '1': 17, '1.5': 23, '2.5': 30, '4': 41, '6': 50,
    '10': 80, '16': 100, '25': 140, '35': 170, '50': 215, '70': 270, '95': 330
    }


def click_button_1():
    """
    Кнопка для записи сечения провода в переменную
    :return:
    """
    print("Кнопка записи сечения провода")
    try:
        wire_cross_section = form.input_from_user_1_wire_cross_section.toPlainText()

        if wire_cross_section in value_wire:
            wire_cross_section = float(wire_cross_section)
            form.output_value_1_wire_cross_section.setText(f"{wire_cross_section} мм2")
            electric_value['wire_cross_section'] = wire_cross_section
            print(f"Сечение провода = {electric_value['wire_cross_section']}")
        else:
            form.output_value_1_wire_cross_section.setText("Ошибка")
            form.output_to_user_fault.setText(f"Сечение провода {wire_cross_section}мм2 не существует")

    except:
        form.output_value_1_wire_cross_section.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода сечения провода")


def click_button_2():
    """
    Кнопка для записи длинны перемычки между АКБ
    :return:
    """
    print("Кнопка записи длинны перемычки")
    try:
        lenght_jumper_battery = form.input_from_user_2_lenght_jumper_battery.toPlainText()
        lenght_jumper_battery = int(lenght_jumper_battery)

        form.output_value_2_lenght_jumper_battery.setText(f"{lenght_jumper_battery} мм")
        electric_value['lenght_wire_to_positive'] = lenght_jumper_battery
        print(f"Длинна перемычки между АКБ = {electric_value['lenght_wire_to_positive']} мм")

    except:
        form.output_value_2_lenght_jumper_battery.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода длинны перемычки")

def click_button_3():
    """
    Кнопка для записи длинны провода до положительного полюса автомата
    :return:
    """
    print("Кнопка записи длинны провода до положительного полюса автомата")
    try:
        lenght_wire_to_positive = form.input_from_user_3_lenght_wire_to_positive.toPlainText()
        lenght_wire_to_positive = int(lenght_wire_to_positive)
        form.output_value_3_lenght_wire_to_positive.setText(f"{lenght_wire_to_positive} мм")
        electric_value['lenght_wire_to_positive'] = lenght_wire_to_positive
        print(f"Длинна провода до положительного полюса АКБ = {electric_value['lenght_wire_to_positive']} мм")

    except:
        form.output_value_3_lenght_wire_to_positive.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода длинны провода до положительного полюса АКБ")

def click_button_4():
    """
    Кнопка для записи длинны провода до отрицательного полюса автомата
    :return:
    """
    print("Кнопка записи длинны провода до отрицательного полюса автомата")
    try:
        lenght_wire_to_negative = form.input_from_user_4_lenght_wire_to_negative.toPlainText()
        lenght_wire_to_negative = int(lenght_wire_to_negative)
        form.output_value_4_lenght_wire_to_negative.setText(f"{lenght_wire_to_negative} мм")
        electric_value['lenght_wire_to_negative'] = lenght_wire_to_negative
        print(f"Длинна провода до отрицательного полюса АКБ = {electric_value['lenght_wire_to_negative']} мм")

    except:
        form.output_value_4_lenght_wire_to_negative.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода длинны провода до отрицательного полюса автомата")

def click_button_5():
    """
    Кнопка для записи напряжения одного АКБ
    :return:
    """
    print("Кнопка записи напряжения одного АКБ")
    try:
        battery_voltage = form.input_from_user_5_battery_voltage.toPlainText()
        battery_voltage = int(battery_voltage)
        form.output_value_5_battery_voltage.setText(f"{battery_voltage} Вольт")
        electric_value['battery_voltage'] = battery_voltage
        print(f"Напряжение одного АКБ = {electric_value['battery_voltage']} Вольт")

    except:
        form.output_value_5_battery_voltage.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода напряжения одного АКБ")

def click_button_6():
    """
    Кнопка для записи внутреннего сопротивления АКБ
    :return:
    """
    print("Кнопка записи внутреннего сопротивления АКБ")
    try:
        battery_internal_resistance = form.input_from_user_6_battery_internal_resistance.toPlainText()
        battery_internal_resistance = int(battery_internal_resistance)
        form.output_value_6_battery_internal_resistance.setText(f"{battery_internal_resistance} мОМ")
        electric_value['battery_internal_resistance'] = battery_internal_resistance
        print(f"Напряжение одного АКБ = {electric_value['battery_internal_resistance']} мОМ")

    except:
        form.output_value_6_battery_internal_resistance.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода внутреннего сопротивления АКБ")

def click_button_7():
    """
    Кнопка для записи кол-ва АКБ
    :return:
    """
    print("Кнопка записи кол-ва АКБ")
    try:
        battery_quantity = form.input_from_user_7_battery_quantity.toPlainText()
        battery_quantity = int(battery_quantity)
        form.output_value_7_battery_quantity.setText(f"{battery_quantity} штук")
        electric_value['battery_quantity'] = battery_quantity
        print(f"Напряжение одного АКБ = {electric_value['battery_quantity']} штук")

    except:
        form.output_value_7_battery_quantity.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода кол-ва АКБ")

def click_button_8():
    """
    Кнопка для записи тока потребителя
    :return:
    """
    print("Кнопка записи тока потребителя")
    try:
        current_consumer = form.input_from_user_8_current_consumer.toPlainText()
        current_consumer = int(current_consumer)
        form.output_value_8_current_consumer.setText(f"{current_consumer} А")
        electric_value['current_consumer'] = current_consumer
        print(f"Ток потребителя = {electric_value['current_consumer']} А")

        if current_consumer > electric_value["wire_cross_section"]:
            form.output_to_user_fault.setText(f"Ток {current_consumer}A больше сечения провода {electric_value['wire_cross_section']} мм2")


    except:
        form.output_value_8_current_consumer.setText("Ошибка")
        form.output_to_user_fault.setText("Ошибка ввода тока потребителя")

def result():
    print("Нажата кнопка результата")
    form.output_to_user_1_result.setText(
        f"Результат расчётов: \n"
       
        f"Сечение провода равно {electric_value['wire_cross_section']} мм2 \n"
        f"Длинна перемычки равна {electric_value['lenght_jumper_battery']} мм \n"
        f"Длинна провода до положительного полюса автомата равна {electric_value['lenght_wire_to_positive']} мм \n"
        f"Длинна провода до негативного полюса автомата равна {electric_value['lenght_wire_to_positive']} мм \n"
        f"Напряжение АКБ равно {electric_value['battery_voltage']} В \n"
        f"Внутреннее сопротивление АКБ равно {electric_value['battery_internal_resistance']} мОМ \n"
        f"Кол-во АКБ равно {electric_value['battery_quantity']} шт \n"
        f"Ток потребителя равен {electric_value['current_consumer']} А \n")


# Нажатие на кнопку 1 для записи сечения провода
form.buttom_1_wire_cross_section.clicked.connect(click_button_1)
form.buttom_2_lenght_jumper_battery.clicked.connect(click_button_2)
form.button_3_lenght_wire_to_positive.clicked.connect(click_button_3)
form.buttom_4_lenght_wire_to_negative.clicked.connect(click_button_4)
form.buttom_5_battery_voltage.clicked.connect(click_button_5)
form.buttom_6_battery_internal_resistance.clicked.connect(click_button_6)
form.buttom_7_battery_quantity.clicked.connect(click_button_7)
form.buttom_8_current_consumer.clicked.connect(click_button_8)
form.start_button.clicked.connect(result)


# Запуск приложения
app.exec()

