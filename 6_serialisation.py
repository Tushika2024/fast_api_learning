from pydantic import BaseModel


class Address(BaseModel):
    city:str
    state:str
    pincode:int
class Patient(BaseModel):
    name:str
    gender:str = "Male"
    age:int
    address:Address ##nested model
    
add_dict={"city":"gurgaon","state":"haryana","pincode":"1009"}
add_model=Address(**add_dict)

patient_dict={"name":"abc","age":30,"address":add_model}
patient_model=Patient(**patient_dict)

##pydantic model to dictionary
patient_dict=patient_model.model_dump()
print(patient_dict)
print(type(patient_dict))


partial_dict=patient_model.model_dump(include=["name","address"])
print(partial_dict)
print(type(partial_dict))

partial_dict=patient_model.model_dump(exclude=["name","address"])
print(partial_dict)
print(type(partial_dict))

partial_dict=patient_model.model_dump(exclude_unset=True)
print(partial_dict)
print(type(partial_dict))

##pydantic model to json
patient_json=patient_model.model_dump_json()
print(patient_json)
print(type(patient_json))

