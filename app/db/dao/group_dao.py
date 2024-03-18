from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Group, session

class GroupDAO(InterfaceDAO):
    
    def get(self, id) -> Group:
        return session.query(Group).filter(Group.id == id).first()
    
    def get_all(self) -> list[Group]:
        return session.query(Group).all()
    
    def create(self, obj: Group) -> Group:
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, obj: Group) -> Group:
        session.commit()
        return obj
    
    def delete(self, obj: Group) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(Group).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(Group).count()