"""empty message

Revision ID: befeff15f315
Revises: 
Create Date: 2018-01-31 19:40:25.652791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'befeff15f315'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('showName', sa.String(length=64), nullable=True),
    sa.Column('showNameEN', sa.String(length=64), nullable=True),
    sa.Column('director', sa.String(length=32), nullable=True),
    sa.Column('leadingRole', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=32), nullable=True),
    sa.Column('language', sa.String(length=32), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningModel', sa.String(length=16), nullable=True),
    sa.Column('openDay', sa.Date(), nullable=True),
    sa.Column('backgroundPicture', sa.String(length=256), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isDelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
