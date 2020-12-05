from botbuilder.dialogs.choices import Choice

START = [
    Choice("Как работать с Puma"),
    Choice("Результат"),
    Choice("График закрытия"),
    Choice("Forex rate"),
    Choice("Процедуры"),
    Choice("Cost Control Team"),
    Choice("Контакты Давида")
]

COMPANIES = [
    Choice("Renault"),
    Choice("Nissan"),
    Choice("АвтоВАЗ"),
]

FOREX_RATE = [
    Choice("Текущий"),
    Choice("Прогнозируемый")
]
