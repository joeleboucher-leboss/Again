"""'is_authenticated_et_debut_classes_Prize_et_Category'

Revision ID: 1bf8879eb117
Revises: 765c96924b5a
Create Date: 2020-04-11 13:47:57.957074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bf8879eb117'
down_revision = '765c96924b5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('is_standart', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=64000), nullable=True),
    sa.Column('standart_product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['standart_product_id'], ['prizes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    op.drop_table('prizes')
    op.drop_table('category')
    # ### end Alembic commands ###