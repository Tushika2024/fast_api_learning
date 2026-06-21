from fastapi import FastAPI, Path, HTTPException, Query
import json
app=FastAPI()


##function to read and return complete json data
def load_data():
    with open("patients.json",'r') as f:
        data=json.load(f)
    return data



@app.get("/")  ##route /
def hello():
    return {"message : Patient Mangament System"}

@app.get("/about")
def about():
    return {"message : A fully functional API to manage patient records"}


@app.get("/view")
def view():
    data= load_data()
    return data

@app.get("/patient/{patient_id}")  ##path params ###.... indicates that path params is requires field
def view_particular_patient(patient_id:str = Path(..., description="ID of patient in the DB", example="P008")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")


@app.get("/sort") ## query params
def sort_patients(sort_by:str = Query(..., description="Sort on the basis of height,weight or bmi"),
                  order:str = Query('asc',description="sort in ascending or descending order")):
    valid_fields=["height","weight","bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field select from {valid_fields}")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid order select asc or desc")
    
    data=load_data()
    
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data