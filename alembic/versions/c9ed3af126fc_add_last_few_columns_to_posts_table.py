"""add last few columns to posts table

Revision ID: c9ed3af126fc
Revises: 6ddb54996104
Create Date: 2026-02-04 10:23:14.257023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9ed3af126fc'
down_revision: Union[str, Sequence[str], None] = '6ddb54996104'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)



def downgrade():
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
