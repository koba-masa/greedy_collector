from sqlalchemy import Column, Integer, String

from models.database import Database

class Announcement(Database):
  id = Column(Integer, primary_key=True)
  key = Column( String, unique=True, nullable=True)
  url = Column(String, nullable=True)
