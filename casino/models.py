from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker




'''
    Database definition
'''

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    player_name = Column(String, unique=True, nullable=False)
    balance = Column(Float, default= 100.0)
    transactions = relationship("Transaction", back_populates="player")


class Transaction(Base):
    __tablename__= 'transactions'
    id = Column(Integer, primary_key=True)
    player_id =  Column(Integer, ForeignKey('players.id'))
    type = Column(String)
    amount = Column(Float)
    player = relationship("Player", back_populates="transactions")


# Conect DB via SQLite

engine = create_engine('sqlite:///casino.db')
Base.metadata.create_all(engine)

# Session to interact with DB
Session = sessionmaker(bind=engine)
session = Session()