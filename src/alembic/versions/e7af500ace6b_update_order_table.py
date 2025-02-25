"""update_order_table

Revision ID: e7af500ace6b
Revises: 84b4bf824da9
Create Date: 2025-02-23 13:51:04.731807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e7af500ace6b'
down_revision: Union[str, None] = '84b4bf824da9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('order', sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False))
    op.add_column('order', sa.Column('status', sa.Enum('designed', 'sent', 'delivered', name='statusenum'), nullable=False))
    op.add_column('order', sa.Column('description', sa.String(), nullable=True))
    op.drop_column('order', 'total_sum')


def downgrade() -> None:
    op.drop_column('order', 'description')
    op.drop_column('order', 'status')
    op.drop_column('order', 'total_amount')
    op.execute("DROP TYPE statusenum;") 
    op.add_column('order', sa.Column('total_sum', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False))

