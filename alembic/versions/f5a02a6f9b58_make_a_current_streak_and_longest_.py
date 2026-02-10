"""make a current_streak and longest_streak NOT NULL

Revision ID: f5a02a6f9b58
Revises: d841d697ef68
Create Date: 2026-02-09 21:27:36.074142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5a02a6f9b58'
down_revision: Union[str, Sequence[str], None] = 'd841d697ef68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
