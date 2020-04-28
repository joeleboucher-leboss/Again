"""empty message

Revision ID: 942fea0eb4b0
Revises: ea30d93076cb
Create Date: 2020-04-21 21:45:43.703097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942fea0eb4b0'
down_revision = 'ea30d93076cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prizes', sa.Column('prize_category', sa.Integer(), nullable=True))
    op.add_column('prizes', sa.Column('prize_description', sa.String(length=64000), nullable=True))
    op.add_column('prizes', sa.Column('prize_id', sa.Integer(), nullable=False))
    op.add_column('prizes', sa.Column('prize_name', sa.String(length=128), nullable=True))
    op.drop_constraint(None, 'prizes', type_='foreignkey')
    op.create_foreign_key(None, 'prizes', 'prizes', ['standart_product_id'], ['prize_id'])
    op.create_foreign_key(None, 'prizes', 'category', ['prize_category'], ['id'])
    op.drop_column('prizes', 'id')
    op.drop_column('prizes', 'name')
    op.drop_column('prizes', 'category')
    op.drop_column('prizes', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prizes', sa.Column('description', sa.VARCHAR(length=64000), nullable=True))
    op.add_column('prizes', sa.Column('category', sa.INTEGER(), nullable=True))
    op.add_column('prizes', sa.Column('name', sa.VARCHAR(length=128), nullable=True))
    op.add_column('prizes', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'prizes', type_='foreignkey')
    op.drop_constraint(None, 'prizes', type_='foreignkey')
    op.create_foreign_key(None, 'prizes', 'prizes', ['standart_product_id'], ['id'])
    op.drop_column('prizes', 'prize_name')
    op.drop_column('prizes', 'prize_id')
    op.drop_column('prizes', 'prize_description')
    op.drop_column('prizes', 'prize_category')
    # ### end Alembic commands ###