"""add indexTrue

Revision ID: 6e336d296ab4
Revises: 8cea54af4a4a
Create Date: 2020-09-03 19:52:22.917317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e336d296ab4'
down_revision = '8cea54af4a4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'admin', ['admin'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'admin', type_='unique')
    # ### end Alembic commands ###
