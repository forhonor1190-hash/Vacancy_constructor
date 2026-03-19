import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.startup.register(startup) #Начало работы
    dp.shutdown.register(shutdown) #Конец работы
    dp.include_router(router=router)
    await dp.start_polling(bot)


#Начало работы
async def startup(dispatcher: Dispatcher):
    print('Бот запущен ...')


#Конец работы
async def shutdown(dispatcher: Dispatcher):
    print('Бот завершил работу')



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
