from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Base(Model, AuditMixin):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    
    
class Category(Base):
    name = Column(String(50), unique = True, nullable=False)
    
    def __repr__(self):
        return self.name