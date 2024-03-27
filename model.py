#This module is used to create PostgresSQL Database 
#We use sqlalchemy to create column of table and relationship between tables
#Sqlalchemy module is used to run the postgresSQL so it serves as a Engine



from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#two seperate Table are created to maintain the database




class Dress(Base):
    __tablename__ = 'dresses'  #Table name for Dresses

    id = Column(Integer, primary_key=True, index=True) 
    #We are created the prototype we seen in Schemas
    #So Colum of table are id,product
    
    Product = Column(String)
    variants = relationship("Variant", back_populates="dress")
     # we declare relationship between dress and variant and back populates it to variant 
    def __repr__(self):
       return f"Dress(id={self.id})"
    #return string value of object

class Variant(Base):
    __tablename__ = 'variants'
#this same as VariantCreate schema we created 
    id = Column(Integer, primary_key=True, index=True)#index to recoed the id correctly using Index
    Size = Column(String)
    Color = Column(String)
    Material = Column(String)
    dresses_id=Column(Integer(),ForeignKey("dresses.id"))#forign key for unique key to id to identify
    dress = relationship("Dress", back_populates="variants")
    
    def __repr__(self):
       return f"Variant(id={self.id})"
        #return string value of object