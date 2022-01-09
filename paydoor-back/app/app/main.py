from typing import Any

from fastapi import FastAPI, Depends
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app import deps
from app.email_record import EmailRecord


app = FastAPI()


class EmailPayload(BaseModel):
    email: EmailStr


@app.post("/add_email")
async def add_email(
        email_payload: EmailPayload,
        db: Session = Depends(deps.get_db)
) -> Any:
    db_obj = EmailRecord(email=email_payload.email)
    db.add(db_obj)
    db.commit()
    return Response(status_code=200)


@app.get("/get_email_count")
async def add_email(db: Session = Depends(deps.get_db)):
    count = db.query(EmailRecord).count()
    # make it look like there are at least some people on the waiting list
    return JSONResponse(content={'count': count + 8})
