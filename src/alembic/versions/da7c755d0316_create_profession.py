"""create_profession

Revision ID: da7c755d0316
Revises: e7af500ace6b
Create Date: 2025-03-01 15:31:44.210627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'da7c755d0316'
down_revision: Union[str, None] = 'e7af500ace6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('profession',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Enum('Frontend_Developer', 'Data_Scientist', 'DevOps_Engineer', 'Backend_Developer', 'Game_Developer', 'Machine_Learning_Engineer', name='professionenum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('profession_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'profession', ['profession_id'], ['id'])


def downgrade() -> None:
    # Bug
    # op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'profession_id')
    op.drop_table('profession')