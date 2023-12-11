"""Renaming students to scholars

Revision ID: 2e66f176812d
Revises: 791279dd0760
Create Date: 2023-12-11 05:46:59.990369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e66f176812d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
