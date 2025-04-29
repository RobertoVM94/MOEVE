from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
from databases import engine, localSession
from schemas import TaskData, TaskID
from models import Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Función para obtener una sesión de base de datos
def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

# Inicializar la app
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para desarrollo. Luego puedes cambiarlo a ["http://localhost:5500"] o tu dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
@app.get('/')
def root():
    return {'message': 'Bienvenido a tu Lista de Tareas'}

@app.get('/api/tasks/', response_model=list[TaskID])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db=db)

@app.get('/api/tasks/{id}', response_model=TaskID)
def get_task(id: int, db: Session = Depends(get_db)):
    task_by_id = crud.get_task_by_id(db=db, id=id)
    if task_by_id:
        return task_by_id
    raise HTTPException(status_code=404, detail='Task not found!!')

@app.post('/api/tasks/', response_model=TaskID)
def create_task(task: TaskData, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.delete('/api/tasks/{id}', response_model=dict)
def delete_task(id: int, db: Session = Depends(get_db)):
    task_to_delete = crud.get_task_by_id(db=db, id=id)
    if task_to_delete:
        db.delete(task_to_delete)
        db.commit()
        return {"message": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Task not found!!")

@app.patch('/api/tasks/{id}', response_model=TaskID)
def mark_task_done(id: int, db: Session = Depends(get_db)):
    task_to_update = crud.get_task_by_id(db=db, id=id)
    if task_to_update:
        task_to_update.done = True
        db.commit()
        db.refresh(task_to_update)
        return task_to_update
    raise HTTPException(status_code=404, detail="Task not found!!")
