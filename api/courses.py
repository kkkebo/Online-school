import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from database.db_setup import get_db
from pydantic_schemas.course import Course, CourseCreate
from api.utils.courses import get_courses, get_course, create_course

router = fastapi.APIRouter()


@router.get("/courses", response_model=list[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course)
async def create_new_course(
    course: CourseCreate, db: Session = Depends(get_db)
):

    return create_course(db=db, course=course)


@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return get_course(db=db, course_id=course_id)


@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}
