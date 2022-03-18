"""Add trade_union

Revision ID: ec3ff6cd49dc
Revises: d4867f3a4c0a
Create Date: 2022-03-17 05:02:15.215280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec3ff6cd49dc'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade_union_type',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('RU', sa.String(), nullable=True),
    sa.Column('KZ', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_trade_union_type_ID'), 'trade_union_type', ['ID'], unique=False)
    op.create_table('trade_union',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('TYPE_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['TYPE_ID'], ['trade_union_type.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_trade_union_ID'), 'trade_union', ['ID'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_trade_union_ID'), table_name='trade_union')
    op.drop_table('trade_union')
    op.drop_index(op.f('ix_trade_union_type_ID'), table_name='trade_union_type')
    op.drop_table('trade_union_type')
    # ### end Alembic commands ###
