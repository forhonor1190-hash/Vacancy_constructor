from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(keyboard=[
               KeyboardButton(text='Создать вакансию'),
               #KeyboardButton(text='Редактировать вакансию'),
               #KeyboardButton(text='Снять вакансию с размещения')
], 
          resize_keyboard=True,     #изменения размера клавиатруры
          input_field_placeholder='Выберите действие ниже'    #в поле для ввода сообщений идет подсказка пользователю
)

#Тип организации (единичый выбор, нельзя оставлять пустым)
type_forms = InlineKeyboardMarkup(inline_keyboard=[
               InlineKeyboardButton(text='ГБУ г. Москвы', callback_data='type_forms_GBU'),
               InlineKeyboardButton(text='КУ г. Москвы', callback_data='type_forms_KU'),
               InlineKeyboardButton(text='ГАУ г. Москвы', callback_data='type_forms_GAU'),
               #InlineKeyboardButton(text='Назад', callback_data=''),
          ])

#Должность (единичый выбор, нельзя оставлять пустым)
position = InlineKeyboardMarkup(inline_keyboard=[
               InlineKeyboardButton(text='Специалист по закупкам', callback_data='position_specialist'),
               InlineKeyboardButton(text='Работник контрактной службы', callback_data='position_worker_KU'),
               InlineKeyboardButton(text='Контрактный управляющий', callback_data='position_KU'),
               #InlineKeyboardButton(text='Другое', callback_data=''),
               #InlineKeyboardButton(text='Назад', callback_data=''),
          ])


#Функционал (множественный выбор, нельзя оставлять пустым)
functions = InlineKeyboardMarkup(inline_keyboard=[
               InlineKeyboardButton(text='Инициатор закупки (формирование потребности)', callback_data='functions_iniciator'),
               InlineKeyboardButton(text='Предварительный сбор данных о потребностях, ценах на товары, работы, услуги (анализ рынка)', callback_data='functions_analiz_runka'),
               InlineKeyboardButton(text='Разработка технической документации, в т. ч. технического задания под конкретные потребности заказчика', callback_data='functions_razrabotka'),
               #InlineKeyboardButton(text='Другое', callback_data=''),
               #InlineKeyboardButton(text='Назад', callback_data=''),
          ])


#Дополнительные требования (множественный выбор, можно оставлять пустым)
requirements = InlineKeyboardMarkup(inline_keyboard=[
               InlineKeyboardButton(text='Наличие действующего сертификата ЕАИСТ', callback_data='requirements_EAIST'),
               InlineKeyboardButton(text='На момент отклика на вакансию состоит в реестре работников КС и членов комиссий по осуществлению закупок', callback_data='requirements_REESTR'),
               InlineKeyboardButton(text='Готов пройти оценочные мероприятия', callback_data='requirements_OM'),
               #InlineKeyboardButton(text='Другое', callback_data=''),
               #InlineKeyboardButton(text='Готово', callback_data=''),
               #InlineKeyboardButton(text='Назад', callback_data=''),
          ])