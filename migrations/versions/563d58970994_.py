"""empty message

Revision ID: 563d58970994
Revises: 6b65c5935c41
Create Date: 2022-10-21 23:21:03.025326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563d58970994'
down_revision = '6b65c5935c41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=120),
               existing_nullable=False)
    op.alter_column('valla', 'light',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=10),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('valla', 'light',
               existing_type=sa.String(length=10),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###
