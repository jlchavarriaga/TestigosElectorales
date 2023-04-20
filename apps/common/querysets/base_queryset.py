from sqlalchemy.orm import Session


class BaseQuerySet:
    def __init__(self, model, db: Session) -> None:
        self.db = db
        self.model = model

    def get(self):
        return self.db.query(self.model)\
            .where(self.model.deleted_at == None)\
            .all()

    def find(self, id: int):
        return self.db.query(self.model)\
            .where(self.model.id == id)\
            .where(self.model.deleted_at == None)\
            .first()

    def where(self, expr):
        return self.db.query(self.model).where(expr)

    def create(self, item):
        self.db.add(item)
        self.db.commit()

    def create_all(self, items: list):
        self.db.add_all(items)
        self.db.commit()
