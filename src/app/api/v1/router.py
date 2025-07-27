from fastapi import APIRouter
from app.api.v1.endpoints import users, posts, feeds, recommendations

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"])
api_router.include_router(posts.router, tags=["posts"])
api_router.include_router(feeds.router, tags=["feeds"])
api_router.include_router(recommendations.router, tags=["recommendations"])

