from app.db.interface_dao import InterfaceDAO
from app.db.init_db import TechnologyCategory, session


class TechnologyCategoryDAO(InterfaceDAO):
        
        def get(self, id) -> TechnologyCategory:
            return session.query(TechnologyCategory).filter(TechnologyCategory.id == id).first()
        
        def get_all(self) -> list[TechnologyCategory]:
            return session.query(TechnologyCategory).all()
        
        def create(self, obj: TechnologyCategory) -> TechnologyCategory:
            session.add(obj)
            session.commit()
            return obj
        
        def update(self, obj: TechnologyCategory) -> TechnologyCategory:
            session.commit()
            return obj
        
        def delete(self, obj: TechnologyCategory) -> bool:
            session.delete(obj)
            session.commit()
            return True
        
        def delete_all(self) -> bool:
            session.query(TechnologyCategory).delete()
            session.commit()
            return True
        
        def count(self) -> int:
            return session.query(TechnologyCategory).count()