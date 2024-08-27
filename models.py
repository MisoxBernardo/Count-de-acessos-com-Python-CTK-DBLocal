# models.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    access_count = Column(Integer, default=0)  # Campo para contar acessos

# Configuração do banco de dados (substitua pelo seu banco de dados)
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
