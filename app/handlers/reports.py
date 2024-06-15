from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app import dependencies
from app.services.abstract.unit_of_work import UnitOfWork
from app.services import reports

router = Router(name=__name__)


@router.message(Command("download_report"), dependencies.UnitOfWork())
async def download_report(message: Message, uow: UnitOfWork):
    await reports.download_report(uow)
