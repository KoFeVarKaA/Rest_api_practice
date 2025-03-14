"""create user table

Revision ID: 74b928e05406
Revises: 
Create Date: 2025-02-15 12:09:02.624625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '74b928e05406'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('user')
