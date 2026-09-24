"""001_initial_skillexa_schema

Revision ID: 001_initial_skillexa_schema
Revises: 
Create Date: 2026-08-16 22:30:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '001_initial_skillexa_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Schema creation managed via SQLAlchemy Base.metadata.create_all() or standard DDL
    pass


def downgrade() -> None:
    pass
