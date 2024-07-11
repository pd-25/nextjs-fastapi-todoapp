"""create todo table

Revision ID: 81283ab3dc13
Revises: 
Create Date: 2024-07-11 13:45:22.999779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81283ab3dc13'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('is_complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
