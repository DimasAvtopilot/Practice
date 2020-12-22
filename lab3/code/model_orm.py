from sqlalchemy import Column, Integer, Float, Text, Date, FLOAT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref



class Employeers(declarative_base()):
    __tablename__ = "employeers"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)



class Menu(declarative_base()):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)


class Kitchen_department(declarative_base()):
    __tablename__ = "kitchen_department"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)




class Storage_department(declarative_base()):
    __tablename__ = "storage_department"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)



class Quality_certificate(declarative_base()):
    __tablename__ = "quality_certificate"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)




class Bookkeping(declarative_base()):
    __tablename__ = "bookkeping"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)




class Storage(declarative_base()):
    __tablename__ = "storage"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone_number = Column(Integer)
    position = Column(Text)
    salary = Column(Float)
    department_id = Column(Integer,ForeignKey('kitchen_department.id'))
    department = relationship("kitchen_department", back_populates="kit_dep")

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.id,self.name,self.phone_number,self.position,self.salary,self.department_id)

    def __repr__(self):
        return str(self)



