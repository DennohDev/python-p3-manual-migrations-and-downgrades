"""rename name column to first name

Revision ID: 4e3f2bf816dc
Revises: 2e66f176812d
Create Date: 2023-12-11 05:53:58.979440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e3f2bf816dc'
down_revision = '2e66f176812d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('scholars', 'first_name', new_column_name='name')
