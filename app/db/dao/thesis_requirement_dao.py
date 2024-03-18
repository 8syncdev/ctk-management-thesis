from app.db.interface_dao import InterfaceDAO
from app.db.init_db import ThesisRequirement, session

class ThesisRequirementDAO(InterfaceDAO):
    
    def get(self, id) -> ThesisRequirement:
        return session.query(ThesisRequirement).filter(ThesisRequirement.id == id).first()
    
    def get_all(self) -> list[ThesisRequirement]:
        return session.query(ThesisRequirement).all()
    
    def create(self, obj: ThesisRequirement) -> ThesisRequirement:
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, obj: ThesisRequirement) -> ThesisRequirement:
        session.commit()
        return obj
    
    def delete(self, obj: ThesisRequirement) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(ThesisRequirement).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(ThesisRequirement).count()