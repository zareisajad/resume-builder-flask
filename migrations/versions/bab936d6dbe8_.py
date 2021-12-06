"""empty message

Revision ID: bab936d6dbe8
Revises: 
Create Date: 2021-12-06 16:51:00.114244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bab936d6dbe8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=150), nullable=False),
    sa.Column('fname', sa.String(length=200), nullable=True),
    sa.Column('lname', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('background',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(length=150), nullable=True),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('employment_date', sa.String(length=80), nullable=True),
    sa.Column('quit_date', sa.String(length=80), nullable=True),
    sa.Column('about_job', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('link_type', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=80), nullable=True),
    sa.Column('about', sa.String(length=700), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
    sa.Column('identifi_number', sa.String(length=80), nullable=True),
    sa.Column('marital_status', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('job_status', sa.String(length=150), nullable=True),
    sa.Column('job_type', sa.String(length=150), nullable=True),
    sa.Column('excepted_salary', sa.String(length=150), nullable=True),
    sa.Column('military_service', sa.String(length=150), nullable=True),
    sa.Column('work_tech', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=100), nullable=True),
    sa.Column('tech', sa.String(length=100), nullable=True),
    sa.Column('about', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill', sa.String(length=200), nullable=True),
    sa.Column('level', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skills')
    op.drop_table('projects')
    op.drop_table('profile')
    op.drop_table('links')
    op.drop_table('background')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###