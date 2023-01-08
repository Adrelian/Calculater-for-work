from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("calculater.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Рабочие действия для запуска приложения


def click_button_1():
    """
    Кнопка для записи сечения провода в переменную
    :return: Возвращает сечение провода в мм2.
    """
    print("Кнопка записи сечения провода")
    try:
        wire_cross_section = form.input_from_user_1_wire_cross_section.toPlainText()
        wire_cross_section = int(wire_cross_section)
        form.output_value_1_wire_cross_section.setText(f"{wire_cross_section} мм2")
        return wire_cross_section
    except:
        form.output_value_1_wire_cross_section.setText("Ошибка ввода сечения")


# Нажатие на кнопку 1 для записи сечения провода
form.buttom_1_wire_cross_section.clicked.connect(click_button_1)



# Запуск приложения
app.exec()
