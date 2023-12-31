"""Init

Revision ID: 37102ed61e3d
Revises: ad29a40f9570
Create Date: 2023-08-24 12:58:50.889201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37102ed61e3d'
down_revision: Union[str, None] = 'ad29a40f9570'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone_number', sa.String(length=20), nullable=False))
    op.drop_index('ix_contacts_email', table_name='contacts')
    op.drop_index('ix_contacts_telephone_number', table_name='contacts')
    op.create_index(op.f('ix_contacts_phone_number'), 'contacts', ['phone_number'], unique=False)
    op.drop_column('contacts', 'telephone_number')
    op.drop_column('contacts', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('contacts', sa.Column('telephone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_contacts_phone_number'), table_name='contacts')
    op.create_index('ix_contacts_telephone_number', 'contacts', ['telephone_number'], unique=False)
    op.create_index('ix_contacts_email', 'contacts', ['email'], unique=False)
    op.drop_column('contacts', 'phone_number')
    # ### end Alembic commands ###
