from fastapi import FastAPI

app = FastAPI(
    title="rent-a-room",
    description="Book your room !",
    version="1.0.0",
    contact={"name": "himu", "email": "xyz@gmail.com"},
)

rooms = [
    {
        "id": 1,
        "name": "Cozy Beachfront Villa",
        "price_per_night": 250.00,
        "bedrooms": 3,
        "bathrooms": 2,
    },
    {
        "id": 2,
        "name": "Downtown Modern Loft",
        "price_per_night": 135.50,
        "bedrooms": 1,
        "bathrooms": 1,
    },
    {
        "id": 3,
        "name": "Rustic Mountain Cabin",
        "price_per_night": 180.00,
        "bedrooms": 2,
        "bathrooms": 1,
    },
    {
        "id": 4,
        "name": "Luxury Suburban Estate",
        "price_per_night": 420.00,
        "bedrooms": 5,
        "bathrooms": 4,
    },
    {
        "id": 5,
        "name": "Lakeside Studio Cottage",
        "price_per_night": 95.00,
        "bedrooms": 1,
        "bathrooms": 1,
    },
]


@app.get("/", status_code=200)
def get_home_page():
    return {"message": "This is Home Page!!"}


@app.get("/rooms", status_code=200)
def get_rooms():
    return rooms


@app.get("/rooms/{room_id}", status_code=200)
def get_room(room_id: int):
    for room in rooms:
        if room["id"] == room_id:
            return room
