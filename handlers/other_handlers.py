from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


@router.message()
async def send_answer(msg: Message):
    """Хэндлер для сообщений, которые не попали в другие хэндлеры"""
    await msg.answer(text=LEXICON_RU["other_answer"])
