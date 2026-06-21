from pydantic import BaseModel


class Address(BaseModel):
    city:str
    state:str
    pincode:int
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address ##nested model
    
add_dict={"city":"gurgaon","state":"haryana","pincode":"1009"}
add_model=Address(**add_dict)

patient_dict={"name":"abc","gender":"female","age":30,"address":add_model}
patient_model=Patient(**patient_dict)

print(patient_model)
print(patient_model.name)
print(patient_model.address.state)
print(patient_model.address.pincode)


##better organistauon of data

## reusability

##redability

##validation
