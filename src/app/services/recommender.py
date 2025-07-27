from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Feed, Post

def top_n_posts_by_likes(db: Session, limit: int):
    like_counts = (
        db.query(Feed.post_id.label("post_id"), func.count().label("likes"))
        .filter(Feed.action == "like")
        .group_by(Feed.post_id)
        .subquery()
    )

    posts = (
        db.query(Post)
        .join(like_counts, Post.id == like_counts.c.post_id)
        .order_by(like_counts.c.likes.desc())
        .limit(limit)
        .all()
    )
    return posts

