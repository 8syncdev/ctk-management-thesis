from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Account, session


class AccountDAO(InterfaceDAO):
    
    def get(self, id: int) -> Account:
        return session.query(Account).filter(Account.id == id).first()
    
    def get_all(self) -> list[Account]:
        return session.query(Account).all()
    
    def create(self, obj: Account) -> Account:
        session.add(obj)
        session.commit()
        return obj

    def update(self, obj: Account) -> Account:
        session.commit()
        return obj
    
    def delete(self, obj: Account) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(Account).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(Account).count()
    