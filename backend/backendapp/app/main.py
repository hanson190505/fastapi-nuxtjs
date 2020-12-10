import time

from fastapi import FastAPI, Query, Depends, HTTPException, Request
from pydantic.typing import List
from sqlalchemy.orm import Session

from sql import schemas, crud, models
from sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.post("/users/", response_model=schemas.User, tags=['Users'])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered!")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User], tags=['Users'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@app.post("/users/{user_id}/books/", response_model=schemas.Book)
def create_book_for_user(user_id: int, book: schemas.BooksCreate, db: Session = Depends(get_db)):
    return crud.create_user_book(db, book, user_id)


@app.get("/books/", response_model=List[schemas.Book])
def get_book(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)
