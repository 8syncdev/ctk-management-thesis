from app.db.interface_dao import InterfaceDAO
from app.db.init_db import Comment, session

class CommentDAO(InterfaceDAO):
    
    def get(self, id: int) -> Comment:
        return session.query(Comment).filter(Comment.id == id).first()
    
    def get_all(self) -> list[Comment]:
        return session.query(Comment).all()
    
    def create(self, obj: Comment) -> Comment:
        session.add(obj)
        session.commit()
        return obj

    def update(self, obj: Comment) -> Comment:
        session.commit()
        return obj
    
    def delete(self, obj: Comment) -> bool:
        session.delete(obj)
        session.commit()
        return True
    
    def delete_all(self) -> bool:
        session.query(Comment).delete()
        session.commit()
        return True
    
    def count(self) -> int:
        return session.query(Comment).count()