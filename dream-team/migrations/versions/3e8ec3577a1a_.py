"""empty message

Revision ID: 3e8ec3577a1a
Revises: 557b80819dc1
Create Date: 2018-03-14 15:18:38.430589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8ec3577a1a'
down_revision = '557b80819dc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_subscribed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_subscribed')
    # ### end Alembic commands ###