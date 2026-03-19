import asyncio
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction
import app.keyboards as kb

router = Router()


@router.message(Command('help'))
async def cmd_help(message: Message):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await message.answer("Если, у вас возникла ошибка <i>(возможно, превышен лимит символов для сообщения (4096 символов)</i> или в поле введено значение, которое не предусмотрено для текущего шага), завершите текущую операцию командой <b>/cancel</b> и введите <b>/start</b> для возвращения на стартовый экран.\n"
    f"\n""Если у вас появятся технические вопросы, пожалуйста, задайте их эксперту Центра юридических и закупочных практик Даниилу Куйдину <a href='https://t.me/KuidinDaniil'>в телеграмме</a> или по почте KuydinDO@edu.mos.ru. Мы всегда рады помочь!\n", parse_mode='HTML', disable_web_page_preview=True)


#Неизвестные команды
@router.message()
async def unknown_command(message: Message):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await message.answer('Это неизвестная команда.')


#Приветствие
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING) #Иммитация жизни от бота, процесс печатания
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await message.answer("Добро пожаловать в <b>конструктор вакансий</b>, разработанный профессиональным сообществом закупщиков Москвы! С помощью конструктора вы можете создать новую вакансию или отредактировать или снять с публикации уже размещенную.\n" 
                        f"\n""Перед стартом работы, пожалуйста, внимательно ознакомьтесь с инструкцией, расположенной ниже.\n"
                        f"\n""<b>Инструкция</b>\n"                                
                        f"\n""1️⃣ С помощью конструктора пошагово заполните обязательные и необязательные поля через контекстное меню: выбирайте из множества готовых вариантов или укажите свой.\n"
                        f"\n""2️⃣ Чтобы вернуться к предыдущему шагу, нажмите на кнопку «Назад».\n"
                        f"\n""3️⃣ Если шаг содержит множественный выбор, отметьте все необходимые пункты и нажмите на кнопку «Готово», чтобы перейти к следующему.\n"                                
                        f"\n""4️⃣ Когда вакансия будет сформирована, появится ее предпросмотр. Выберите доступные действия с помощью специальной иконки в поле для ввода сообщений:\n"
                        f"\n""🙍‍♂️ <b>«Опубликовать»</b> — ваша вакансия отправится на модерацию и в скором времени будет размещена.\n"
                        f"\n""🙍‍♂️ <b>«Редактировать»</b> — вы вернетесь к выбранному шагу, чтобы скорректировать информацию в нем.\n"
                        f"\n""‼️📛 Обратите внимание, что все следующие шаги после выбранного нужно будет заполнить заново. Например, вы решили отредактировать шаг «Номер телефона», значит, шаги «Адрес электронной почты» и «Предпочтительный способ связи» понадобится заполнить заново.\n"                                
                        f"\n""🙍‍♂️ <b>«Отменить публикацию»</b> — ваша вакансия не отправится на модерацию.\n"                                
                        f"\n""5️⃣ После публикации вакансии вы сможете выбрать следующие действия с помощью специальной иконки в поле для ввода сообщений:\n"
                        f"\n""🙍‍♂️ <b>«Создать вакансию»</b> — разместить еще одну вакансию.\n"
                        f"\n""🙍‍♂️ <b>«Редактировать вакансию»</b> — поменять информацию в уже отправленной на модерацию вакансии.\n"                                
                        f"\n""🙍‍♂️ <b>«Снять вакансию с размещения»</b> — убрать вакансию с модерации или удалить ее из целевого чата.\n"
                        f"\n""6️⃣ Чтобы начать работу с чат-ботом, отправьте команду <b>/start</b> в поле для ввода сообщений.\n"
                        f"\n""7️⃣ Если, у вас возникла ошибка <i>(возможно, превышен лимит символов для сообщения (4096 символов)</i> или в поле введено значение, которое не предусмотрено для текущего шага), завершите текущую операцию командой <b>/cancel</b> и введите <b>/start</b> для возвращения на стартовый экран.\n"
                        f"\n""Если у вас появятся технические вопросы, пожалуйста, задайте их эксперту Центра юридических и закупочных практик Даниилу Куйдину <a href='https://t.me/KuidinDaniil'>в телеграмме</a> или по почте KuydinDO@edu.mos.ru. Мы всегда рады помочь!\n"
                        f"\n""Выберите действие (в поле для ввода сообщений появится специальная иконка):", 
    parse_mode='HTML', 
    disable_web_page_preview=True, #Скрытие превью
    reply_murkup=kb.main_menu
)


#Стартовые Reply-кнопки "Создание"
@router.message(F.text == 'Создать вакансию')
async def create_vacancy(message: Message):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await message.answer('Выберите тип организации:',
    reply_markup=ReplyKeyboardRemove(), #убираем reply-клавиатуру                      
    reply_murkup=kb.type_forms
)


#Тип организации 
@router.callback_query(F.data.startswith('type_forms_'))
async def type_forms(callback: CallbackQuery):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await callback.answer('Вы сделали свой выбор!', 
    show_alert=True) #всплывающее уведомление
    await callback.message.answer(f'Тип организации: {callback.data}')


#Название учреждения
async def name(message: Message):
    await message.answer('Введите название учреждения:', 
    ...
)
    
"""
"""


#Должность
async def position(message: Message):
    await message.answer('Выберите должность:', 
    reply_markup=kb.position
)
    
@router.callback_query(F.data.startswith('position_'))
async def position(callback: CallbackQuery):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await callback.answer('Вы сделали свой выбор!', 
    show_alert=True) #всплывающее уведомление
    await callback.message.answer(f'Должность: {callback.data}')
    

#Функционал
async def functions(message: Message):
    await message.answer('Выберите функционал для соискателя (можно выбрать несколько):', 
    reply_markup=kb.functions
)

@router.callback_query(F.data.startswith('functions_'))
async def functions(callback: CallbackQuery):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await callback.answer('Вы сделали свой выбор!', 
    show_alert=True) #всплывающее уведомление
    await callback.message.answer(f'Функционал: - {callback.data}')


#Дополнительные требования
async def functions(message: Message):
    await message.answer('Выберите дополнительные требования (можно выбрать несколько):', 
    reply_markup=kb.requirements
)
    
@router.callback_query(F.data.startswith('requirements_'))
async def requirements(callback: CallbackQuery):
    await asyncio.sleep(1) #ответ после сна в 1 сек.
    await callback.answer('Вы сделали свой выбор!', 
    show_alert=True) #всплывающее уведомление
    await callback.message.answer(f'Дополнительные требования: - {callback.data}')


#Доход
async def salary(message: Message):
    await message.answer('Введите уровень дохода в месяц, в тыс. руб.:', 
    ...
)
"""
"""


    
"""
#Стартовые Reply-кнопки "Редактирование"
@router.message(F.text == 'Редактировать вакансию')
async def create_vacancy(message: Message):
    pass

#Стартовые Reply-кнопки "Снятие с размещения"
@router.message(F.text == 'Снять вакансию с размещения')
async def create_vacancy(message: Message):
    pass
"""
