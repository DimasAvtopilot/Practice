import psycopg2
from time import time
from model_orm import *
from sqlalchemy.orm import *
from sqlalchemy import create_engine

def insert_one_orm(Session,table_name,list):

    session = Session()

    if table_name == "employeers":
        table_item = Employeers(name = list[0], phone_number = list[1], position = list[2], department_id = list[3], salary = list[4])
    elif table_name == "menu":
        table_item = Menu(name = list[0], department_id = list[1])
    elif table_name == "kitchen_department":
        table_item = Kitchen_department(name_of_department = list[0], employeers_count = list[1], certificate_id = list[2], book_id = list[3])
    elif table_name == "storage_department":
        table_item = Storage_department(kitchen_id = list[0], storage_id = list[1])
    elif table_name == "quality_certificate":
        table_item = Quality_certificate(date_of_issue = list[0], expirition_date = list[1], authority_that_issued = list[2])
    elif table_name == "bookkeping":
        table_item = Bookkeping(salary = list[0])
    else:
        table_item = Storage(count_number = list[0])
    session.add(table_item)
    session.commit()
    session.close()


def select_all_orm(Session,table_name):
    session = Session()
    if table_name == "employeers":
        table_item = session.query(Employeers).all()
    elif table_name == "menu":
        table_item = session.query(Menu).all()
    elif table_name == "kitchen_department":
        table_item = session.query(Kitchen_department).all()
    elif table_name == "storage_department":
        table_item = session.query(Storage_department).all()
    elif table_name == "quality_certificate":
       table_item = session.query(Quality_certificate).all()
    elif table_name == "bookkeping":
       table_item = session.query(Bookkeping).all()
    else:
        table_item = session.query(Storage).all()
    session.close()

    return table_item



def delete_one_orm(Session,table_name,pr_key):
    session = Session()
    pr_key = pr_key[0]
    if table_name == "employeers":
        table_item = session.query(Employeers).filter(Employeers.id == pr_key).first()
    elif table_name == "menu":
        table_item = session.query(Menu).filter(Menu.id == pr_key).first()
    elif table_name == "kitchen_department":
        table_item = session.query(Kitchen_department).filter(Kitchen_department.id == pr_key).first()
    elif table_name == "storage_department":
        table_item = session.query(Storage_department).filter(Storage_department.id == pr_key).first()
    elif table_name == "quality_certificate":
        table_item = session.query(Quality_certificate).filter(Quality_certificate.id == pr_key).first()
    elif table_name == "bookkeping":
        table_item = session.query(Bookkeping).filter(Bookkeping.id == pr_key).first()
    else:
        table_item = session.query(Storage).filter(Storage.id == pr_key).first()
    if table_item is None:
        session.close()
        return 0

    session.delete(table_item)
    session.commit()
    session.close()

    return 1


def delete_all_orm(Session,table_name):
    session = Session()
    if table_name == "employeers":
        tmp = session.query(Employeers).delete()
    elif table_name == "menu":
        tmp = session.query(Menu).delete()
    elif table_name == "kitchen_department":
        tmp = session.query(Kitchen_department).delete()
    elif table_name == "storage_department":
        tmp = session.query(Storage_department).delete()
    elif table_name == "quality_certificate":
        tmp = session.query(Quality_certificate).delete()
    elif table_name == "bookkeping":
        tmp = session.query(Bookkeping).delete()
    else:
        tmp = session.query(Storage).delete()
    
    session.commit()
    session.close()

    return tmp




def update_item_orm(Session,table_name,list):
    session = Session()

    if table_name == "employeers":
        table_item = session.query(Employeers).filter(Employeers.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.name, table_item.phone_number, table_item.position, table_item.department_id, table_item.salary = list[1], list[2], list[3], list[4], list[5]

    elif table_name == "menu":
        table_item = session.query(Menu).filter(Menu.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.name, table_item.department_id = list[1],list[2]
    
    elif table_name == "kitchen_department":
        table_item = session.query(Kitchen_department).filter(Kitchen_department.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.name_of_department, table_item.employeers_count, table_item.certificate_id, table_item.book_id = list[1], list[2], list[3], list[4]

    elif table_name == "storage_department":
        table_item = session.query(Storage_department).filter(Storage_department.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.kitchen_id, table_item.storage_id = list[1], list[2]

    elif table_name == "quality_certificate":
        table_item = session.query(Quality_certificate).filter(Quality_certificate.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.date_of_issue, table_item.expirition_date, table_item.authority_that_issued = list[1], list[2], list[3]

    elif table_name == "bookkeping":
        table_item = session.query(Bookkeping).filter(Bookkeping.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.salary = list[1]

    else:
        table_item = session.query(Storage).filter(Storage.id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.count_number = list[1]
    session.commit()
    session.close()

    return 1




def connect_to_db_orm():
    engine = create_engine('postgresql+psycopg2://postgres:12345@localhost:5432/DB_Lab1')
    session_class = sessionmaker(bind=engine)
    return session_class


