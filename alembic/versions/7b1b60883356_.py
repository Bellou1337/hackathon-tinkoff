"""empty message

Revision ID: 7b1b60883356
Revises: 33419a72bf7b
Create Date: 2024-11-22 21:29:43.294249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7b1b60883356'
down_revision: Union[str, None] = '33419a72bf7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('date', sa.TIMESTAMP(), nullable=False))
    op.drop_column('transaction', 'registered_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('transaction', 'date')
    # ### end Alembic commands ###