import sqlalchemy as sa

from .base import Base


class User(Base):

    __tablename__ = 'user'

    user_id = Column()
    user_name = Column()
    password = Column()


class UserDetail(Base):

    __tablename__ = 'userdetail'

    user_id = Column()
    first_name = Column()
    last_name = Column()
