from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

data = [
    {"name": "Shaggy Rogers", "occupation": "Freelance food critic", "address": "1234 Oakwood Ave, Springfield"},
    {"name": "Velma Dinkley", "occupation": "Researcher", "address": "5678 Pine St, Oakwood"},
    {"name": "Daphne Blake", "occupation": "Fashion Journalist", "address": "910 Maple Rd, Rivertown"},
    {"name": "Fred Jones", "occupation": "Private Investigator", "address": "1122 Birch Ln, Greenfield"},
    {"name": "Scooby-Doo", "occupation": "Dog Detective", "address": "Mystery Machine, Roaming"}
]

# Define Pydantic model for request validation
class Person(BaseModel):
    name: str
    occupation: str
    address: str

# POST request handler to add a person
@app.post("/person")
async def add_person(person: Person):
    # Check that none of the fields are empty
    if person.name == "" or person.occupation == "" or person.address == "":
        return {
            "success": False,
            "result": {"error_message": "invalid request"}
        }
    
    # Add to the data list
    data.append(person.dict())

    return {
        "success": True,
        "result": person.dict()
    }

# GET request handler to retrieve all people
@app.get("/person")
async def get_people():
    return data

