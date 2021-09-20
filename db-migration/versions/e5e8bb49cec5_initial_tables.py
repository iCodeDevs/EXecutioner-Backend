"""Initial tables

Revision ID: e5e8bb49cec5
Revises: 
Create Date: 2021-09-20 17:15:53.246796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5e8bb49cec5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Problem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('statement', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Problem_id'), 'Problem', ['id'], unique=False)
    op.create_table('TestCase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('input', sa.String(), nullable=True),
    sa.Column('output', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_TestCase_id'), 'TestCase', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_TestCase_id'), table_name='TestCase')
    op.drop_table('TestCase')
    op.drop_index(op.f('ix_Problem_id'), table_name='Problem')
    op.drop_table('Problem')
    # ### end Alembic commands ###