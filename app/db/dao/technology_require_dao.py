from app.db.interface_dao import InterfaceDAO
from app.db.init_db import TechnologyRequirement, session

class TechnologyRequirementDAO(InterfaceDAO):
    
    def get(self, id) -> TechnologyRequirement:
        return session.query(TechnologyRequirement).filter(TechnologyRequirement.id == id).first()
    
    def get_all(self) -> list[TechnologyRequirement]:
        return session.query(TechnologyRequirement).all()
    
    def create(self, obj: TechnologyRequirement) -> TechnologyRequirement:
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, obj: TechnologyRequirement) -> TechnologyRequirement:
        session.commit()
        return obj
    
    def delete(self, obj: TechnologyRequirement) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(TechnologyRequirement).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(TechnologyRequirement).count()