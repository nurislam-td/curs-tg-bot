from app.services.abstract.unit_of_work import UnitOfWork


async def download_report(uow: UnitOfWork):
    async with uow:
        await uow.report.create_for_week()
        await uow.commit()
