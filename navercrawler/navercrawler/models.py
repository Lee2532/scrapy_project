# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.engine.base import Engine
# from sqlalchemy.engine.url import URL
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.asyncio import AsyncSession
#
# # from navercrawler.navercrawler import settings
#
# DeclarativeBase = declarative_base()
#
# class PG_CONN:
#     def __init__(self):
#         self.user = "postgres"
#         self.password = "0000"
#         self.host = "localhost"
#         self.port = "5432"
#         self.database = "postgres"
#
#     def db_connect(self) -> Engine:
#         url = ""
#         return create_engine(url)
#
#
# def create_items_table(engine: Engine):
#     """
#     Create the Items table
#     """
#     DeclarativeBase.metadata.create_all(engine)
#
#
# class Items(DeclarativeBase):
#     """
#     Defines the items model
#     """
#
#     __tablename__ = "items"
#
#     name = Column("name", String, primary_key=True)
#     price = Column("price", Integer)