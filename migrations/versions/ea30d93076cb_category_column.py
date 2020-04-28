"""'Category_column'

Revision ID: ea30d93076cb
Revises: db252af2e8e9
Create Date: 2020-04-21 14:51:05.517880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea30d93076cb'
down_revision = 'db252af2e8e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prizes', sa.Column('category', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'prizes', 'category', ['category'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'prizes', type_='foreignkey')
    op.drop_column('prizes', 'category')
    # ### end Alembic commands ###