"""Initial database setup

Revision ID: d81952a870bb
Revises: 
Create Date: 2025-06-14 22:51:36.926695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd81952a870bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aula',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('tema', sa.String(length=30), nullable=False),
    sa.Column('chave', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('data')
    )
    op.create_table('membro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_completo', sa.String(length=120), nullable=False),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('data_recepcao', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('campus', sa.String(length=50), nullable=False),
    sa.Column('ativo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('contribuicao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('membro_id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=30), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('data_lanc', sa.Date(), nullable=False),
    sa.Column('forma', sa.String(length=20), nullable=False),
    sa.Column('observacoes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['membro_id'], ['membro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('contribuicao', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_contribuicao_data_lanc'), ['data_lanc'], unique=False)
        batch_op.create_index(batch_op.f('ix_contribuicao_membro_id'), ['membro_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_contribuicao_tipo'), ['tipo'], unique=False)

    op.create_table('jornada_evento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('membro_id', sa.Integer(), nullable=False),
    sa.Column('data_evento', sa.DateTime(), nullable=True),
    sa.Column('descricao', sa.Text(), nullable=False),
    sa.Column('tipo_evento', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['membro_id'], ['membro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('presenca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('membro_id', sa.Integer(), nullable=False),
    sa.Column('aula_id', sa.Integer(), nullable=False),
    sa.Column('avaliacao', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aula_id'], ['aula.id'], ),
    sa.ForeignKeyConstraint(['membro_id'], ['membro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('presenca')
    op.drop_table('jornada_evento')
    with op.batch_alter_table('contribuicao', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_contribuicao_tipo'))
        batch_op.drop_index(batch_op.f('ix_contribuicao_membro_id'))
        batch_op.drop_index(batch_op.f('ix_contribuicao_data_lanc'))

    op.drop_table('contribuicao')
    op.drop_table('user')
    op.drop_table('membro')
    op.drop_table('aula')
    # ### end Alembic commands ###
