import random

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



# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choise = _normalize_user_answer(user_choice)

    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}

    if user_choise == bot_choice:
        return 'nobody_won'
    elif rules[user_choise] == bot_choice:
        return 'user_won'
    return 'bot_won'