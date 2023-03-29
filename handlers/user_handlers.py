from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner, wins

router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def start_com(message: Message):
    await message.answer(LEXICON_RU['/start'],
                         reply_markup=yes_no_kb)



# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def help_com(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=yes_no_kb)



# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(Text(text=LEXICON_RU['yes_button']))
async def yes_answer(message: Message):
    await message.answer(LEXICON_RU['yes'],
                         reply_markup=game_kb)

# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(Text(text=LEXICON_RU['no_button']))
async def no_answer(message: Message):
    await message.answer(LEXICON_RU['no'])




# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['scissors'],
                           LEXICON_RU['paper']]))
async def game_buttons(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                         f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(wins())
    await message.answer(text=LEXICON_RU[winner],
                         reply_markup=yes_no_kb)

