"""Add military

Revision ID: fce1469a98bd
Revises: a245aacf939c
Create Date: 2022-03-18 06:27:56.967570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fce1469a98bd'
down_revision = 'a245aacf939c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_change_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_change_type_id'), 'order_change_type', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_change_type_id'), table_name='order_change_type')
    op.drop_table('order_change_type')
    # ### end Alembic commands ###
