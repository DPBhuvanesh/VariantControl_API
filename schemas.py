#This Schemas file for the Creating a Dress and Variant it's Attribute  using pydantic module
#So We create a seperate Class for each dress and Variant and Separate VariantCreate and DressCreate
#we pass the varaintBase and DressBase to it, So it inhertiance it
 
 
 
 #pydantic model to import basemodel 
#typing model to import the List



from typing import List
from pydantic import BaseModel

class VariantBase(BaseModel):  #It consits of Size,Color,Material
    Size: str
    Color: str
    Material: str

class VariantCreate(VariantBase):#It inherites VariantBase
    pass

class Variant(VariantBase): #It create indiviual I'd for variant and dresses the variant have
    id: int
    dresses_id: int

    class Config: #ORM mode used to read the attribute of VariantBase Class and its relational mapping it
        orm_mode = True 

class DressBase(BaseModel):
    Product: str      #Product will be string 
 
class DressCreate(DressBase):
    pass #It inherites the DressBase

class Dress(DressBase):
    id: int #dress id 
    variants: List[Variant] = [] #Variant will be in list as it has more than one variant

    class Config:
        orm_mode = True #ORM mode used to read the attribute of DresstBase Class
        #It is relational mapping it 
