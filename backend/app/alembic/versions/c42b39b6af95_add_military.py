"""Add military

Revision ID: c42b39b6af95
Revises: 11541d9c6f4a
Create Date: 2022-03-18 05:57:22.140841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c42b39b6af95'
down_revision = '11541d9c6f4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('declination',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ruIP', sa.String(), nullable=True),
    sa.Column('ruRP', sa.String(), nullable=True),
    sa.Column('ruDP', sa.String(), nullable=True),
    sa.Column('ruTP', sa.String(), nullable=True),
    sa.Column('ruVP', sa.String(), nullable=True),
    sa.Column('ruPP', sa.String(), nullable=True),
    sa.Column('kzAS', sa.String(), nullable=True),
    sa.Column('kzIS', sa.String(), nullable=True),
    sa.Column('kzBS', sa.String(), nullable=True),
    sa.Column('kzZS', sa.String(), nullable=True),
    sa.Column('kzTS', sa.String(), nullable=True),
    sa.Column('kzSS', sa.String(), nullable=True),
    sa.Column('kzKS', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_declination_id'), 'declination', ['id'], unique=False)
    op.create_table('staff_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_staff_category_id'), 'staff_category', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_staff_category_id'), table_name='staff_category')
    op.drop_table('staff_category')
    op.drop_index(op.f('ix_declination_id'), table_name='declination')
    op.drop_table('declination')
    # ### end Alembic commands ###
