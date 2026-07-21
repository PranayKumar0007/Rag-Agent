from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
	return "HEYY ITS DAY1"
