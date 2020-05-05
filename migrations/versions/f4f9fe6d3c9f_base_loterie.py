"""'base_loterie'

Revision ID: f4f9fe6d3c9f
Revises: 93754ad8cdea
Create Date: 2020-05-05 11:52:34.747355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4f9fe6d3c9f'
down_revision = '93754ad8cdea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loteries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prize', sa.Integer(), nullable=True),
    sa.Column('vendor', sa.Integer(), nullable=True),
    sa.Column('nb_participants', sa.Integer(), nullable=True),
    sa.Column('vendor_price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prize'], ['prizes.id'], ),
    sa.ForeignKeyConstraint(['vendor'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participants',
    sa.Column('lotery_id', sa.Integer(), nullable=True),
    sa.Column('participant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lotery_id'], ['loteries.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['user.id'], )
    )
    op.create_foreign_key(None, 'prizes', 'category', ['prize_category'], ['id'])
    op.drop_column('prizes', 'name')
    op.drop_column('prizes', 'category')
    op.drop_column('prizes', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prizes', sa.Column('description', sa.VARCHAR(length=64000), nullable=True))
    op.add_column('prizes', sa.Column('category', sa.INTEGER(), nullable=True))
    op.add_column('prizes', sa.Column('name', sa.VARCHAR(length=128), nullable=True))
    op.drop_constraint(None, 'prizes', type_='foreignkey')
    op.drop_table('participants')
    op.drop_table('loteries')
    # ### end Alembic commands ###