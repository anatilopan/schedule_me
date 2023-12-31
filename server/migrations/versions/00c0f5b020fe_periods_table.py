"""periods table

Revision ID: 00c0f5b020fe
Revises: d7b9bfe1e955
Create Date: 2023-12-20 00:23:54.913803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c0f5b020fe'
down_revision = 'd7b9bfe1e955'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('periods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('periods', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_periods_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_periods_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('periods', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_periods_user_id'))
        batch_op.drop_index(batch_op.f('ix_periods_created_at'))

    op.drop_table('periods')
    # ### end Alembic commands ###
