from fastapi import FastAPI
import uvicorn

from src.api.user import user_router
from src.api.order import order_router
from src.api.user__order import user__order_router


app = FastAPI()

app.include_router(user_router)
app.include_router(order_router)
app.include_router(user__order_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 