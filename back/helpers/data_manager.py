from data.model import db
from sqlalchemy.exc import SQLAlchemyError

class DataManager():
    # CREATE
    def add(self, *args):
        try:
            for request in args:
                db.session.add(request)
                db.session.commit()
                return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'
    
    # UPDATE
    def update(self):
        try:
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'
    
    # DELETE
    def delete(self,id_a):
        try:
            db.session.delete(id_a)
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    # INDIVIDUAL QUERY BY ID
    def individual_query(self):
        pass

    # QUERY ALL
    def query_all(self):
        pass