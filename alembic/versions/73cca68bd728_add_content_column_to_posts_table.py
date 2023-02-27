"""add content column to posts_table

Revision ID: 73cca68bd728
Revises: b7036a4cfb86
Create Date: 2023-02-27 11:54:06.556699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73cca68bd728'
down_revision = 'b7036a4cfb86'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
