from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Criterion, session

class CriterionDAO(InterfaceDAO):
    
    def get(self, id: int) -> Criterion:
        return session.query(Criterion).get(id)
    
    def get_all(self) -> list[Criterion]:
        return session.query(Criterion).all()
    
    def add(self, obj: Criterion) -> None:
        session.add(obj)
        session.commit()

    def update(self, obj: Criterion) -> None:
        session.commit()

    def delete(self, obj: Criterion) -> None:
        session.delete(obj)
        session.commit()

    def delete_all(self) -> bool:
        try:
            session.query(Criterion).delete()
            session.commit()
            return True
        except Exception as e:
            print('Error: ' + str(e))
            return False
        
    def count(self) -> int:
        return session.query(Criterion).count()
        