"""create tables

Revision ID: a818cdee8359
Revises: 
Create Date: 2021-02-19 20:44:28.333908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a818cdee8359'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.Column('dark_mode', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_config_user_id'), 'config', ['user_id'], unique=True)
    op.create_table('profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.String(length=100), nullable=True),
    sa.Column('surname', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profile_user_id'), 'profile', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_profile_user_id'), table_name='profile')
    op.drop_table('profile')
    op.drop_index(op.f('ix_config_user_id'), table_name='config')
    op.drop_table('config')
    # ### end Alembic commands ###
