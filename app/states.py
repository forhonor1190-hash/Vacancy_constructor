from aiogram.state import State, StatesGroup


class VC(StatesGroup):    
    type_forms = State() #Тип организации
    name = State() #Название организации
    posposition = State() #Должность
    functions = State() #Функции
    requirements = State() #Дополнительные требования
    salary = State() #Зарплата
    email = State() #Почта
    number = State() #Телефон
    