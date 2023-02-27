"""add foreign-key to post table

Revision ID: 8953b16fa2ac
Revises: 11860304897e
Create Date: 2023-02-27 12:06:06.992194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8953b16fa2ac'
down_revision = '11860304897e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
