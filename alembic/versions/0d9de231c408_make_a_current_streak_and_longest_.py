"""make a current_streak and longest_streak NOT NULL

Revision ID: 0d9de231c408
Revises: 044847fb644a
Create Date: 2026-02-09 21:25:49.746799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d9de231c408'
down_revision: Union[str, Sequence[str], None] = '044847fb644a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
