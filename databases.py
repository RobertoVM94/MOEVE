from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Tarea  # Importa el modelo Tarea
from schemas import TaskData  # Importa el esquema para la creación

# Define la URL de la base de datos (la misma que en database.py)
DATABASE_URL = "sqlite:///./tasks.db" #<--- Esta será la ruta de un archivo que tendrás que crear previamente

# Crea el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crea las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Crea una sesión de base de datos
localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_database():
    db = localSession()
    try:
        # Datos de las tareas iniciales
        task_to_create = [
            {"name": "Hacer Tabla", "done": "False"},
        ]
        for task_data in task_to_create:
            # Crea un esquema TaskData para la validación (opcional aquí, pero buena práctica)
            task_schema = TaskData(**task_data)
            db_task = Tarea(**task_schema.dict())
            db.add(db_task)

        db.commit()
        print("Volcado inicial de tareas completado.")

    except Exception as e:
        db.rollback()
        print(f"Error al realizar el volcado inicial: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()