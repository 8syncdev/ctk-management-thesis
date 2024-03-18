from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Task, session

class TaskDAO(InterfaceDAO):
    
    def get(self, id) -> Task:
        return session.query(Task).filter(Task.id == id).first()
    
    def get_all(self) -> list[Task]:
        return session.query(Task).all()
    
    def create(self, obj: Task) -> Task:
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, obj: Task) -> Task:
        session.commit()
        return obj
    
    def delete(self, obj: Task) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(Task).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(Task).count()