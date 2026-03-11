from fastapi  import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
  return {
    "message": "Welcome to my FastAPI application",
    "name": "Fefe"
  }

@app.get("/info")
def course_info():
  return{
    "course_name": "FastAPI Fundamentals",
    "instructor": "Your Instructor Name",
    "duration_period": 4
  }

@app.get("/health")
def health_check():
  return {"status": "OK"}