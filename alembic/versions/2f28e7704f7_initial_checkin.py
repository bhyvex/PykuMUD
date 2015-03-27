"""Initial checkin

Revision ID: 2f28e7704f7
Revises: 
Create Date: 2015-03-27 11:31:00.004572

"""

# revision identifiers, used by Alembic.
revision = '2f28e7704f7'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('option',
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('version', sa.String(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('wizlock', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('date_created')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('option')
    ### end Alembic commands ###