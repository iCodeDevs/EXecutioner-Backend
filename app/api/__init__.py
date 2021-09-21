from fastapi import APIRouter
from .submission import submission_router
api_router = APIRouter()

@api_router.get("/")
def main():
    return {"hello": "world"}

api_router.include_router(submission_router)
