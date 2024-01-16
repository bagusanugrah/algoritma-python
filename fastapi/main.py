from fastapi import FastAPI

app = FastAPI()

data_user = {
    'email': '',
    'password': ''
}

@app.get('/')
def root():
    return {'message': 'salah route harusnya ke /data-user'}

@app.post('/data-user')
def post(email: str, password: str):
    global data_user
    posted_data = {
        'email': email,
        'password': password
    }

    data_user = posted_data
    return data_user

@app.get('/data-user')
def get():
    return data_user

#jalankan dengan uvicorn main:app --host 0.0.0.0 --port 8000