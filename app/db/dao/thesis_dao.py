from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Thesis, session

class ThesisDAO(InterfaceDAO):
    

    def get(self, id) -> Thesis:
        return session.query(Thesis).filter(Thesis.id == id).first()
    
    def get_all(self) -> list[Thesis]:
        return session.query(Thesis).all()
    
    def create(self, obj: Thesis) -> Thesis:
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, obj: Thesis) -> Thesis:
        session.commit()
        return obj
    
    def delete(self, obj: Thesis) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(Thesis).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(Thesis).count()