from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_home_page():
    return {"message": "This is Home Page!!"}
