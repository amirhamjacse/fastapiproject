# # main.py
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from . import crud, models, schemas
# from .database import SessionLocal, engine

# # Create all tables
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Create a user
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db=db, user=user)

# # Get a user by ID
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# # Get all users
# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users

# # Delete a user
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = crud.delete_user(db=db, user_id=user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"detail": "User deleted"}


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
