from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from pydantic import AfterValidator
from pydantic_core import PydanticCustomError

app = FastAPI(
    title="rent-a-room",
    description="Book your room !",
    version="1.0.0",
    contact={"name": "himu", "email": "xyz@gmail.com"},
)


def fail_if_funny(search):
    if search and "lol" in search:
        raise PydanticCustomError(
            "validation_error", "No funny things, Only serious businesses"
        )
    return search


SearchQuery = Annotated[
    str | None, Query(min_length=3, max_length=10), AfterValidator(fail_if_funny)
]

PriceQuery = Annotated[int | None, Query(ge=10, le=10000)]

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

rooms = [
    {
        "id": 1,
        "name": "Cozy Beachfront Villa",
        "price_per_night": 250.00,
        "bedrooms": 3,
        "bathrooms": 2,
        "price": 20000,
    },
    {
        "id": 2,
        "name": "Downtown Modern Loft",
        "price_per_night": 135.50,
        "bedrooms": 1,
        "bathrooms": 1,
        "price": 10000,
    },
    {
        "id": 3,
        "name": "Rustic Mountain Cabin",
        "price_per_night": 180.00,
        "bedrooms": 2,
        "bathrooms": 1,
        "price": 15000,
    },
    {
        "id": 4,
        "name": "Luxury Suburban Estate",
        "price_per_night": 420.00,
        "bedrooms": 5,
        "bathrooms": 4,
        "price": 5000,
    },
    {
        "id": 5,
        "name": "Lakeside Studio Cottage",
        "price_per_night": 95.00,
        "bedrooms": 1,
        "bathrooms": 1,
        "price": 1000,
    },
]


@app.get("/", status_code=200)
def get_home_page():
    return {"message": "This is Home Page!!"}


@app.get("/rooms", status_code=200)
def get_rooms(
    search: SearchQuery = None,
    max_price: PriceQuery = None,
):
    results = rooms.copy()

    if search:
        results = [room for room in results if search.lower() in room["name"].lower()]

    if max_price is not None:
        results = [room for room in results if room["price"] <= max_price]

    return results


@app.get("/rooms/{room_id}", status_code=200)
def get_room(room_id: int):
    for room in rooms:
        if room["id"] == room_id:
            return room
    raise HTTPException(status_code=404, detail="Room Not Found")
