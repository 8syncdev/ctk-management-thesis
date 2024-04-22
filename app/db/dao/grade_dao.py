from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Grade, session

class GradeDAO(InterfaceDAO):
        
        def get(self, id) -> Grade:
            return session.query(Grade).filter(Grade.id == id).first()
        
        def get_all(self) -> list[Grade]:
            return session.query(Grade).all()
        
        def create(self, obj: Grade) -> Grade:
            session.add(obj)
            session.commit()
            return obj
        
        def update(self, obj: Grade) -> Grade:
            session.commit()
            return obj
        
        def delete(self, obj: Grade) -> bool:
            session.delete(obj)
            session.commit()
            return True
        
        def delete_all(self) -> bool:
            session.query(Grade).delete()
            session.commit()
            return True
        
        def count(self) -> int:
            return session.query(Grade).count()
