import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.api.deps import get_db
from app.main import app
from app.models import User, Post, Feed

SQLALCHEMY_TEST_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture()
def client(db):
    def _get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = _get_db
    return TestClient(app)

@pytest.fixture()
def seed_data(db):
    u1 = User(id=1, name="John", surname="Doe", age=25, gender=1,
              country="USA", city="NY", exp_group=3, os="Android", source="ads")
    u2 = User(id=2, name="Jane", surname="Roe", age=30, gender=0,
              country="USA", city="NY", exp_group=3, os="iOS", source="organic")

    p1 = Post(id=10, text="Hello World", topic="business", author_id=1)
    p2 = Post(id=11, text="Second Post", topic="tech", author_id=2)

    f1 = Feed(id=100, user_id=1, post_id=10, action="like", time="2024-01-01 10:00:00")
    f2 = Feed(id=101, user_id=2, post_id=10, action="like", time="2024-01-01 11:00:00")
    f3 = Feed(id=102, user_id=1, post_id=11, action="view", time="2024-01-02 10:00:00")

    db.add_all([u1, u2, p1, p2, f1, f2, f3])
    db.commit()

