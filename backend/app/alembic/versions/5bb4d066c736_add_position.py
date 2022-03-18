"""Add position

Revision ID: 5bb4d066c736
Revises: d21ea487c241
Create Date: 2022-03-18 10:41:57.674923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bb4d066c736'
down_revision = 'd21ea487c241'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('declination_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'position', 'declination', ['declination_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'position', type_='foreignkey')
    op.drop_column('position', 'declination_id')
    # ### end Alembic commands ###