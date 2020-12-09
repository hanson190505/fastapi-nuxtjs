from fastapi import FastAPI, Query, Depends, HTTPException
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


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


# @app.get("/books/")
# def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     books = get_books(db, skip=skip, limit=limit)
#     return books
