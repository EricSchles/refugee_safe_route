"""empty message

Revision ID: d91a3da4f312
Revises: ee167b4a1da4
Create Date: 2016-06-16 16:46:43.583342

"""

# revision identifiers, used by Alembic.
revision = 'd91a3da4f312'
down_revision = 'ee167b4a1da4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ad_info', sa.Column('latitude', sa.String(), nullable=True))
    op.add_column('ad_info', sa.Column('longitude', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ad_info', 'longitude')
    op.drop_column('ad_info', 'latitude')
    ### end Alembic commands ###
