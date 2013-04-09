from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine= create_engine('sqlite:///prueba.db', echo=True)

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category('%s')>" % (self.name)     
        

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone = Column(String(10))
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", backref=backref('companies', order_by=id))

    def __init__(self, name, phone, description):
        self.name = name
        self.phone = phone
        self.description = description
        
    def __repr__(self):
        return "<Company('%s','%s', '%s')>" % (self.name, self.phone, self.description)


Base.metadata.create_all(engine)