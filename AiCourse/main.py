from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def read_root() :
  return {'message': 'AI Scholarship API is running!'}

@app.get('/hello/{name}')
def say_hello(name: str) :
  return {'message': f'Hello {name}, welcome to AI course!'}