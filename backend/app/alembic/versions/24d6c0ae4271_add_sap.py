"""Add sap

Revision ID: 24d6c0ae4271
Revises: 6b2e1cda837a
Create Date: 2022-03-17 13:33:55.717309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24d6c0ae4271'
down_revision = '6b2e1cda837a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gender_id'), 'gender', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_gender_id'), table_name='gender')
    op.drop_table('gender')
    # ### end Alembic commands ###
