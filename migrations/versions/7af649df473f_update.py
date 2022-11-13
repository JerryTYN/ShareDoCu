"""update

Revision ID: 7af649df473f
Revises: 710b3b7e259b
Create Date: 2022-11-06 15:11:40.651881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7af649df473f'
down_revision = '710b3b7e259b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CATEGORY',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('CITY',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('USER',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=True),
    sa.Column('UserName', sa.String(), nullable=True),
    sa.Column('Password', sa.String(), nullable=True),
    sa.Column('PhoneNumber', sa.String(), nullable=True),
    sa.Column('Address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('PRODUCT',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=True),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('ImageUrl', sa.String(), nullable=True),
    sa.Column('Status', sa.Integer(), nullable=True),
    sa.Column('Surcharge', sa.Integer(), nullable=True),
    sa.Column('UserId', sa.Integer(), nullable=True),
    sa.Column('CategoryId', sa.Integer(), nullable=True),
    sa.Column('CityId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['CategoryId'], ['CATEGORY.Id'], ),
    sa.ForeignKeyConstraint(['CityId'], ['CITY.Id'], ),
    sa.ForeignKeyConstraint(['UserId'], ['USER.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PRODUCT')
    op.drop_table('USER')
    op.drop_table('CITY')
    op.drop_table('CATEGORY')
    # ### end Alembic commands ###
