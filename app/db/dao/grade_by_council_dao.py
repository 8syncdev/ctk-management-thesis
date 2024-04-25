from app.db.interface_dao import InterfaceDAO
from app.db.init_db import GradeByCouncil, session

class GradeByCouncilDAO(InterfaceDAO):
    
        def get(self, id: int) -> GradeByCouncil:
            return session.query(GradeByCouncil).filter(GradeByCouncil.id == id).first()
        
        def get_all(self) -> list[GradeByCouncil]:
            return session.query(GradeByCouncil).all()
        
        def create(self, obj: GradeByCouncil) -> GradeByCouncil:
            session.add(obj)
            session.commit()
            return obj
    
        def update(self, obj: GradeByCouncil) -> GradeByCouncil:
            session.commit()
            return obj
        
        def delete(self, obj: GradeByCouncil) -> bool:
            session.delete(obj)
            session.commit()
            return True
        
        def delete_all(self) -> bool:
            session.query(GradeByCouncil).delete()
            session.commit()
            return True
        
        def count(self) -> int:
            return session.query(GradeByCouncil).count()