from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Problem(Base):
    __tablename__ = "Problem"
    id = Column(Integer, primary_key=True, index=True)
    statement = Column(String)
    testcases = relationship("TestCase",backref="problem")

class Testcase(Base):
    __tablename__ = "TestCase"
    id = Column(Integer, primary_key=True, index=True)
    input = Column(String)
    output = Column(String)

