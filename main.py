from fastapi import FastAPI

app = FastAPI(
    title="rent-a-room",
    description="Book your room !",
    version="1.0.0",
    contact={"name": "himu", "email": "xyz@gmail.com"},
)


@app.get("/")
def get_home_page():
    return {"message": "This is Home Page!!"}
