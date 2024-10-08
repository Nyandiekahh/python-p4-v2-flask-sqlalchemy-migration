"""rename address

Revision ID: a6b8b41af47d
Revises: d2942fbaebe8
Create Date: 2024-08-20 22:55:56.845337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6b8b41af47d'
down_revision = 'd2942fbaebe8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###