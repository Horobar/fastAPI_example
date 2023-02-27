"""add user table

Revision ID: 11860304897e
Revises: 73cca68bd728
Create Date: 2023-02-27 11:58:17.914875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11860304897e'
down_revision = '73cca68bd728'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
