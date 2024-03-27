#importing schemas amd model to Create,Update,Read and Delete
#So CRUD is short form for it, we didn't create delete function 
#Also maintaing seperate file alone to decode error easily and smalles the main.py

from sqlalchemy.orm import Session,joinedload
from model import Dress

import schemas,model

#create function of dress
def create_dress(db: Session, dress: schemas.DressCreate):#dress parameter to create DressCreate from schemas
    db_dress = model.Dress(Product=dress.Product)#get product
    db.add(db_dress)#add it and commit to database and refresh it
    db.commit()
    db.refresh(db_dress)
    return db_dress



def create_variant(db: Session, variant: schemas.VariantCreate, dress_id: int): #getting dress_id to link dress of varaint
    db_variant = model.Variant(Size=variant.Size, Color=variant.Color, Material=variant.Material, dresses_id=dress_id)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant 

#this update for dress and variant so we uses the id to update it and we use same schema as creating
#to update 


def update_item(db: Session, dress_id: int, dress_update: schemas.DressCreate):
    item_to_update = db.query(model.Dress).filter(model.Dress.id == dress_id).first()
    if item_to_update:
        item_to_update.Product = dress_update.Product
        db.commit()
    return item_to_update




def update_variant(db: Session,variant_id: int,variant_update: schemas.VariantCreate):
    variant_to_update = db.query(model.Variant).filter(model.Variant.id == variant_id).first()
    if variant_to_update:
        variant_to_update.Size = variant_update.Size
        variant_to_update.Color = variant_update.Color
        variant_to_update.Material = variant_update.Material
        db.commit()
    return variant_to_update
        
        
#it gets the all database as it querys it ,we use joinedload to get varaint also      
def get_all_dresses(db: Session):
    return db.query(model.Dress).options(joinedload(model.Dress.variants)).all()
   
#it gets product  by name and filter it , so filter command is uses   
def get_product_with_variants_by_name(db: Session, product_name: str):
    return db.query(model.Dress).filter(model.Dress.Product == product_name).options(joinedload(model.Dress.variants)).first()