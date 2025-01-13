from sqlalchemy.orm import Session
from app.models import Item, User
from .schemas import Item as ItemSchema, User as UserSchema

# CRUD operations for items
def get_items(db: Session):
    return db.query(Item).all()

# CRUD operations for users
def get_users(db: Session):
    return db.query(User).all()