#modules used are FastApI for creating an API 



from fastapi import FastAPI, Depends, HTTPException
from typing import List
from pydantic import BaseModel
 
from sqlalchemy.orm import Session, joinedload,relationship
from model import Dress,Variant
import crud,schemas
from database import SessionLocal, Base, engine
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG) #using logging to avoid HTTP error

app = FastAPI(title="VarianControl",
    description="Create Dress with Variants and Manage it ") #creating an app 


from database import Base, engine


Base.metadata.create_all(bind=engine) #use to create a database and binds the engine


def get_session_local():
    yield SessionLocal()


def get_db():     
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
dp_dependency =  Depends(get_db) #used to inject dependency of data

#We use CRUD.py to create all endpints here


@app.get("/dresses/", response_model=List[schemas.Dress]) #calling the function fromc rud 
async def get_all_dresses(db: Session = Depends(get_db)):#so it create a post endpoint for getting all dress
    dresses = crud.get_all_dresses(db)
    return dresses

#this create product and variant
@app.post("/dresses/", response_model=schemas.Dress)
def create_dress_with_variants(dress_Type: schemas.DressCreate, Variants_Type: List[schemas.VariantCreate], db: Session = Depends(get_db)):
    
    db_dress = crud.create_dress(db=db, dress=dress_Type)
    
    
    for variant_data in Variants_Type:
        crud.create_variant(db=db, variant=variant_data, dress_id=db_dress.id)
    
    
    db.refresh(db_dress)
    
    return db_dress

#this update the dress with using id to detect it 
#put function to update it
@app.put("/dresses/{dress_id}", response_model=schemas.Dress)
def update_dress(dress_id: int, dress_update: schemas.DressCreate, db: Session = Depends(get_db)):
    
    updated_dress = crud.update_item(db, dress_id, dress_update)
    return updated_dress


#this update the variant with using id to detect it 
#put function to update it 
@app.put("/update_variant/{variant_id}", response_model=schemas.Variant)
def update_variant(variant_id: int, variant_update: schemas.VariantCreate, db: Session = Depends(get_db)):
    updated_variant = crud.update_variant(db, variant_id, variant_update)
    if updated_variant is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return updated_variant

#it gets or retrives  product along with variants
@app.get("/product/{product_name}", response_model=schemas.Dress)
def get_product_with_variants(product_name: str, db: Session = Depends(get_db)):
    product = crud.get_product_with_variants_by_name(db, product_name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


#this used to handle the logging operation
@app.get("/")
async def read_it():
    logging.debug("Handling root endpoint request")  #  debug log
    return {"message": "This is Variant Control For a Dresses E-Commerce API"}

# help uvicron to run without error  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80) #run the application in localhost
    # it set uvicorn logging level to debug
    uvicorn_config = uvicorn.Config(app='main:app', log_level='debug')
    
    # it help to start uvicorn server
    uvicorn_server = uvicorn.Server(uvicorn_config)
    uvicorn_server.run()
    
