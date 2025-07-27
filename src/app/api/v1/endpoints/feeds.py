from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from app.api.deps import get_db
from app.models import Feed
from app.schemas import FeedGet

router = APIRouter()

@router.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(
    id: int,
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    return (
        db.query(Feed)
        .filter(Feed.user_id == id)
        .order_by(desc(Feed.time))
        .limit(limit)
        .all()
    )

@router.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(
    id: int,
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    return (
        db.query(Feed)
        .filter(Feed.post_id == id)
        .order_by(desc(Feed.time))
        .limit(limit)
        .all()
    )

