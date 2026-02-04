"""add content column to posts table

Revision ID: db0d54584c7a
Revises: 9b180b09a00a
Create Date: 2026-02-04 09:55:02.170765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db0d54584c7a'
down_revision: Union[str, Sequence[str], None] = '9b180b09a00a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", 'content')
    pass
