"""refactor product

Revision ID: 33edfde91c4f
Revises: dacb084be73c
Create Date: 2020-12-25 21:24:13.813596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33edfde91c4f'
down_revision = 'dacb084be73c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=True)
    op.create_table('subcategory',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('product_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subcategory_id'), 'subcategory', ['id'], unique=False)
    op.create_index(op.f('ix_subcategory_name'), 'subcategory', ['name'], unique=True)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('number', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('product_sub_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_sub_category_id'], ['subcategory.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=True)
    op.create_index(op.f('ix_product_number'), 'product', ['number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_number'), table_name='product')
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_subcategory_name'), table_name='subcategory')
    op.drop_index(op.f('ix_subcategory_id'), table_name='subcategory')
    op.drop_table('subcategory')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###