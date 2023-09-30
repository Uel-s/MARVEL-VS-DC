"""empty message

Revision ID: ab94881868e9
Revises: 1355c9722367
Create Date: 2023-09-29 21:28:14.083261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab94881868e9'
down_revision = '1355c9722367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes_powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(), nullable=True),
    sa.Column('heroes_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['heroes_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('heroe_powers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroe_powers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('strength', sa.VARCHAR(), nullable=True),
    sa.Column('heroes_id', sa.INTEGER(), nullable=True),
    sa.Column('power_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['heroes_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('heroes_powers')
    # ### end Alembic commands ###
