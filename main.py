from aiogram import Bot,Dispatcher, Router
from aiogram.filters.callback_data import CallbackData, CallbackQuery
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from aiogram.types import Message
from aiogram.filters import Command
from Keybords.keybord import builder, Razmer, markup
from Xlam.Consts import TOKEN
from selenium import webdriver
import logging, asyncio

bot = Bot(TOKEN)
router = Router()
a = 0
@router.message(Command("start"))
async def CommandStart(message: Message):
        await message.answer(text = "Введи команду /generate для генерации изображений,\n"
                                    "либо /settings для настройки изображения ", reply_markup= builder)

@router.message(Command("settings"))
async def Settings(message: Message):
    await message.answer(text= "Выбери размер =)", reply_markup= markup)

@router.callback_query()
async def Boobs(callback: CallbackQuery):
        global a
        await callback.answer(text= "Нажми кнопку /generate для получения изображения")
        if callback.data == "little":
            a = 1
        elif callback.data == "middle":
            a = 2
        elif callback.data == 'big':
            a = 3
        return a

@router.message(Command('generate'))
async def Send_Photo(message: Message):
    await message.answer(text= "Обработка запроса...\nЭто может занять несколько минут")
    option = webdriver.ChromeOptions()
    option.add_argument(f"user-agent = {UserAgent().googlechrome}")
    driver = webdriver.Chrome(options=option)
    driver.get("ссылка")
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[3]/button[1]/span").click()
    driver.implicitly_wait(2)
    if a == 1:
            driver.implicitly_wait(2)
            driver.find_element(By.XPATH, '//*[@id="panel:r0:0"]/div[3]/div[2]/div[4]').click()
    elif a == 2:
            driver.implicitly_wait(2)
            driver.find_element(By.XPATH, '//*[@id="panel:r0:0"]/div[3]/div[2]/div[3]').click()
    elif a == 3:
            driver.implicitly_wait(2)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[2]/div[2]').click()
    else:
            print(2)
            print(a)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/button').click()
    await asyncio.sleep(600)    #driver.implicitly_wait(600)
    image = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/a/img')
    await bot.delete_message(chat_id= message.from_user.id, message_id= message.message_id + 1)
    await bot.send_message(chat_id= message.from_user.id, text= "Готово <3")
    await bot.send_photo(chat_id= message.from_user.id, photo= image.get_attribute("src"))

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    asyncio.run(main())