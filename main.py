from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - demo2-coll-b8f8a28f4e2448cfa1f851347c690e4f',debug=False,docs_url='/dreamy-bhaskara-a7722ad4c50811ef8a6a0242ac12000513/docs',openapi_url='/dreamy-bhaskara-a7722ad4c50811ef8a6a0242ac12000513/openapi.json')

app.include_router(router, prefix='/dreamy-bhaskara-a7722ad4c50811ef8a6a0242ac12000513/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()