from sqlalchemy.orm import Session

from app.db.session import engine
from app.db.base import Base
from app.email_record import EmailRecord


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)

    db_obj = EmailRecord(email='the_first_email@test.com')
    db.add(db_obj)
    db.commit()
