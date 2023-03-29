import random
from dataclasses import dataclass

from lexicon.lexicon import LEXICON_RU


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'scissors', 'paper'])



# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


@dataclass
class Victories:
    user_victories: int=0
    bot_victories: int=0
    draw: int=0
    games: int=0

    def __call__(self):
        user_name = random.choice(['Bag of bones', 'Leather bag', 'Meat', 'Meatball',
                                   'Soft ass', 'Someone who pushes buttons'])

        return f'{user_name}: {self.user_victories} \n' \
               f'Bot: {self.bot_victories}\n' \
               # f'draw: {wins.draw}'

wins: Victories = Victories()


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choise = _normalize_user_answer(user_choice)

    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    wins.games += 1

    if user_choise == bot_choice:
        wins.draw += 1
        return 'nobody_won'
    elif rules[user_choise] == bot_choice:
        wins.user_victories += 1
        return 'user_won'
    wins.bot_victories += 1
    return 'bot_won'

