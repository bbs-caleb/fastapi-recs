from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas import PostGet
from app.services.recommender import top_n_posts_by_likes

router = APIRouter()

@router.get("/post/recommendations/", response_model=List[PostGet])
def get_post_recommendations(
    id: int,
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    return top_n_posts_by_likes(db, limit)

