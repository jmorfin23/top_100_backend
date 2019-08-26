"""empty message

Revision ID: 6b8b9509abf1
Revises: 
Create Date: 2019-07-18 10:23:37.092410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b8b9509abf1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('message', sa.String(length=500), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('contact_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=150), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tweet', sa.String(length=140), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('contact')
    # ### end Alembic commands ###
