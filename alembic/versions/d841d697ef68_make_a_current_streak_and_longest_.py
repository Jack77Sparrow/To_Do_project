"""make a current_streak and longest_streak NOT NULL

Revision ID: d841d697ef68
Revises: 0d9de231c408
Create Date: 2026-02-09 21:26:27.425099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd841d697ef68'
down_revision: Union[str, Sequence[str], None] = '0d9de231c408'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
