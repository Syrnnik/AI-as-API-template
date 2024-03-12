import uvicorn
from fastapi import FastAPI

from controllers.generate_controller import generate_router

app = FastAPI()

app.include_router(generate_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
