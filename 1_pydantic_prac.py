from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):  ##pydantic model
    name: Annotated[str,Field(max_length=50, title="name of patient", 
        description="give name in less than 50 chars", examples=["Nitish","Tushika"])]
    ##title , description, examples metadata, max_length=data validation
    email: Optional[EmailStr]
    likedlnurl:Optional[AnyUrl]
    age:int=Field(gt=0, lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)] ## strict=True stop typecoercing
    married: Annotated[bool,Field(default=None, description="enter married or not")]
    allergies: Optional[List[str]]=None  ##None is default value is value not provided for allergies optional field
    contact_details: Dict[str,str]
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("succeed")
    
    
patient_info={"name":"nitish","age":30,"weight":-72.5,
              "contact_details":{"email":"abc@gmail.com", "mobile":"9012345"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)