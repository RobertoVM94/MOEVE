from sqlalchemy.orm import Session
from models import Tarea
from schemas import TaskData

def get_tasks(db: Session):
    return db.query(Tarea).all()

def create_task (db: Session, task: TaskData):
    new_task = Tarea(name=task.name, done=task.done)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task_by_id(db: Session, id: int):
    return db.query(Tarea).filter(Tarea.id == id).first()

def update_task(db: Session, id: int, done: bool):
    task = db.query(Tarea).filter(Tarea.id == id).first()
    if task:
        task.done = done
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_task(db: Session, id: int):
    task =  db.query(Tarea).filter(Tarea.id == id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False