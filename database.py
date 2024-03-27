#this is the where we create a engine and session 


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


URL_DATABASE= "postgresql://postgres:root@localhost:5432/db_demo"
    #for postregres to create change //username:password@localhost:port/database_name


engine = create_engine(URL_DATABASE, echo=True)#declare engine and echo=true to help logging option

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #using session local to avoid autocommit and binding engine
Base = declarative_base() #we declare a base to create models in seprate it inherites it 