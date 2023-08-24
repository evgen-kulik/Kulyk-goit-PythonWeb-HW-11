from typing import List

from sqlalchemy.orm import Session

from src.database.models import User, Contact
from src.schemas import UserModel, UserResponse


async def read_users(skip: int, limit: int, db: Session) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


async def read_user(user_id: int, db: Session) -> User:
    return db.query(User).filter(User.id == user_id).first()


async def create_user(body: UserModel, db: Session) -> User:
    contacts = db.query(Contact).filter(Contact.id.in_(body.contacts)).all()
    user = User(name=body.name, last_name=body.last_name, day_of_born=body.day_of_born, email=body.email,
                description=body.description, contacts=contacts)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def remove_user(user_id: int, db: Session) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


async def update_user(user_id: int, body: UserModel, db: Session) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        phones = db.query(Contact).filter(Contact.id.in_(body.contacts)).all()
        user.title = body.title
        user.description = body.description
        user.phones = phones
        db.commit()
    return user
