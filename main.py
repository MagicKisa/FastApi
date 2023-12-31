from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    return {'service' : "doge-doge"}

@app.post("/post", response_model=Timestamp)
def get_post():
    return 

@app.get("/dog", response_model=Dog)
def get_dogs(kind : DogType):
    filtered_dogs = [dog for dog in dogs_db if dog.kind == kind]
    return filtered_dogs

@app.post("/dog", response_model=Dog)
def create_dog(dog : Dog):
    return dog

@app.get("/dog/{pk}", response_model=Dog)
def get_dog_by_pk(pk : int):
    return dogs_db[pk]

@app.patch("/dog/{pk}", response_model=Dog)
def update_dog(pk : int, dog : Dog):
    dogs_db[pk] = dog

