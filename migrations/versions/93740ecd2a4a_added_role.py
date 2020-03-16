"""Added role

Revision ID: 93740ecd2a4a
Revises: 8f7a7e6cb8af
Create Date: 2020-03-16 12:07:39.990012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93740ecd2a4a'
down_revision = '8f7a7e6cb8af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.drop_table('role')
    # ### end Alembic commands ###
