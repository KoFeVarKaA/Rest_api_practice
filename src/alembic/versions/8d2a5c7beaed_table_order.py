"""table_order

Revision ID: 8d2a5c7beaed
Revises: 74b928e05406
Create Date: 2025-02-20 06:50:18.266622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '8d2a5c7beaed'
down_revision: Union[str, None] = '74b928e05406'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('total_sum', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('order')
