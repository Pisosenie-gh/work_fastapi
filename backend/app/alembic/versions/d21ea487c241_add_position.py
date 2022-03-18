"""Add position

Revision ID: d21ea487c241
Revises: 9a845d88a680
Create Date: 2022-03-18 10:28:20.208849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd21ea487c241'
down_revision = '9a845d88a680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('govPositionId', sa.Integer(), nullable=True),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_id'), 'position', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_position_id'), table_name='position')
    op.drop_table('position')
    # ### end Alembic commands ###