from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, Text

from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(msg: Message):
    """Этот хэндлер срабатывает на команду /start"""
    await msg.answer(text=LEXICON_RU["/start"], reply_markup=yes_no_kb)


@router.message(Command(commands=["help"]))
async def process_help_command(msg: Message):
    """Этот хэндлер срабатывает на команду /help"""
    await msg.answer(text=LEXICON_RU["/help"], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_RU["yes_button"]))
async def process_yes_answer(msg: Message):
    """Этот хэндлер срабатывает на согласие пользователя играть в игру"""
    await msg.answer(text=LEXICON_RU["yes"], reply_markup=game_kb)


@router.message(Text(text=LEXICON_RU["no_button"]))
async def process_no_answer(msg: Message):
    """Этот хэндлер срабатывает на отказ пользователя играть в игру"""
    await msg.answer(text=LEXICON_RU["no"])


@router.message(Text(text=[LEXICON_RU["rock"],
                           LEXICON_RU["scissors"],
                           LEXICON_RU["paper"]]))
async def process_game_button(msg: Message):
    """Этот хэндлер срабатывает на любую из игровых кнопок"""
    bot_choise = get_bot_choice()
    await msg.answer(text=f"{LEXICON_RU['bot_choice']} - "
                          f"{LEXICON_RU[bot_choise]}")
    winner = get_winner(msg.text, bot_choise)
    await msg.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
