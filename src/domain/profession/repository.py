from sqlalchemy import select
from database import session_factory
from src.domain.profession.model import Profession, ProfessionEnum

class ProfessionRepository:
    @staticmethod
    async def profession_to_id(profession: ProfessionEnum):
        async with session_factory() as session:
            stmt = select(Profession.id).where(Profession.name == profession)
            return (await session.scalars(stmt)).first()