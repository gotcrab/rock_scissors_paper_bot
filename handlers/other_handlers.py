from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

router: Router = Router()

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def other_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])