"""add user table

Revision ID: 0f724901c8b4
Revises: db0d54584c7a
Create Date: 2026-02-04 10:03:00.767860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f724901c8b4'
down_revision: Union[str, Sequence[str], None] = 'db0d54584c7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))

    pass


def downgrade():
    """Downgrade schema."""
    op.drop_table('users')
    pass
