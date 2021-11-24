import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    DateTime,
    Table,
    Float,
    Text,

)


Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(126), unique=False, nullable=False)
    nick = Column(String(126), unique=True, nullable=False)
    location = Column(String(52), unique=False, nullable=True)
    rating = Column(Float, unique=False, nullable=True)

    def __str__(self):
        print(self.name)


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(126), unique=True, nullable=False)
    rating = Column(Float, unique=False, nullable=True)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=True)
    author = relationship(Author, backref='blog')
    post = relationship("Post", backref='blog')


_teg_post = Table(
    "teg_post",
    Base.metadata,
    Column("teg_id", Integer, ForeignKey("teg.id")),
    Column("post_id", Integer, ForeignKey("post.id"))
)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(252), unique=False)
    text = Column(Text, unique=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    blog_id = Column(Integer, ForeignKey("blog.id"), nullable=False)
    tegs = relationship("Teg", secondary=_teg_post, backref='post')


class Teg(Base):
    __tablename__ = 'teg'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(126), unique=True)

    def __str__(self):
        print(self.name)



