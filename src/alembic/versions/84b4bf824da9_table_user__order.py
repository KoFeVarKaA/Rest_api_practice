"""table_user__order

Revision ID: 84b4bf824da9
Revises: 8d2a5c7beaed
Create Date: 2025-02-23 11:40:39.188116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '84b4bf824da9'
down_revision: Union[str, None] = '8d2a5c7beaed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user__order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    op.drop_table('user__order')
