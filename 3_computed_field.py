from pydantic import BaseModel,Field, EmailStr,computed_field
from typing import List,Dict,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    # married:bool
    # allergies:List[str]
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
        

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    # print(patient.allergies)
    # print(patient.married)
    print(patient.bmi)
    print("succeed")
    
    
patient_info={"name":"nitish","email":"abc@hdfc.com","age":'8',"weight":72.5,
              "height":78,"contact_details":{"mobile":"9012345"}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)