import random


class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self):
        items = self.model.read_items()
        if items.rowcount:
            self.view.table_rows_display(items)
            return
        self.view.message_print("This table was already empty\n")

    def enter_items(self, table_item_names):
        return_array = []
        for name in table_item_names:
            self.view.enter_cortege_item_display(name)
            inp = str(input())
            return_array.append(inp)
        return return_array

    def table_type_select(self):
        self.view.table_name_select_display()
        while True:
            table_type = str(input())
            if 0 < int(table_type) < 7:
                if table_type == "1":
                    self.model.present_table_type = "employeers"
                elif table_type == "2":
                    self.model.present_table_type = "kitchen_department"
                elif table_type == "3":
                    self.model.present_table_type = "quality_certificate"
                elif table_type == "4":
                    self.model.present_table_type = "menu"
                elif table_type == "5":
                    self.model.present_table_type = "bookkeping"
                elif table_type == "6":
                    self.model.present_table_type = "storage"
                elif table_type == "7":
                    self.model.present_table_type = "storage_department"
                return
            self.view.message_print("Error:enter number from 1 to 7\n")
    

    def action_type_select(self):
        self.view.action_type_select_display()
        while True:
            action_type = str(input())
            if action_type != "1" and action_type != "2" and action_type != "3":
                self.view.message_print("Error:enter number from 1 to 3\n")
                continue
            break
        return action_type

    def action_select(self):
        self.view.action_select_display()
        while True:
            action = str(input())
            if action == "1":
                self.show_items()
            elif action == "2":
                self.update_item()
            elif action == "3":
                self.insert_item()
            elif action == "4":
                self.delete_item()
            elif action == "5":
                self.delete_all()
            else:
                self.view.message_print("Error:Enter number from 1-5\n")
                continue
            break

        self.model.connection.commit()

    def question_about_end(self):
        self.view.question_about_end_display()
        while True:
            inp = str(input())
            if inp == "Y" or inp == "y":
                return True
            elif inp == "N" or inp == "n":
                return False
            else:
                self.view.message_print("""Error:enter "Y" or "N"\n """)

    def disconnect_from_db(self):
        self.model.disconnect_from_db()

    def insert_item(self):
        while True:
            if self.model.present_table_type == 'employeers':
                list = self.enter_items(("name", "phone_number", "position", "salary",  "department_id"))
            elif self.model.present_table_type == 'kitchen_department':
                list = self.enter_items(("name_of_department", "employeers_count", "certificate_id", "book_id"))
            elif self.model.present_table_type == 'quality_certificate':
                list = self.enter_items(("date_of_issue","expirition_date","authority_that_issued"))
            elif self.model.present_table_type == 'menu':
                list = self.enter_items(("name","department_id"))
            elif self.model.present_table_type == 'bookkeping':
                list = self.enter_items(("salary",))
            elif self.model.present_table_type == 'storage':
                list = self.enter_items(("count_number",))
            else:
                list = self.enter_items(("kitchen_id","storage_id"))
            try:
                self.model.create_item(list)
                self.view.message_print("Row was inserted successfully\n")
                break
            except Exception as error:
                print(error)
                break
            finally:
                self.model.connection.commit()

    def update_item(self):
        while True:
            if self.model.present_table_type == 'employeers':
                list = self.enter_items(("Id", "name", "phone_number", "position", "salary", "department_id"))
            elif self.model.present_table_type == 'kitchen_department':
                list = self.enter_items(("Id", "name_of_department", "employeers_count", "certificate_id", "book_id"))
            elif self.model.present_table_type == 'quality_certificate':
                list = self.enter_items(("Id", "date_of_issue","expirition_date","authority_that_issued"))
            elif self.model.present_table_type == 'menu':
                list = self.enter_items(("Id", "name","department_id"))
            elif self.model.present_table_type == 'bookkeping':
                list = self.enter_items(("Id", "salary",))
            elif self.model.present_table_type == 'storage':
                list = self.enter_items(("Id", "count_number",))
            else:
                list = self.enter_items(("Id", "kitchen_id","storage_id"))
            try:
                self.model.update_item(list)
                self.view.message_print("Row was updated successfully\n")
                break
            except Exception as error:
                print(error)
            finally:
                self.model.connection.commit()

    def delete_item(self):
        id = self.enter_items(["id"])
        try:
            if self.model.delete_item(id):
                self.view.message_print("Row was deleted successfully\n")
            else:
                self.view.message_print("There isn't row for deleting with such attribute value\n")
        except Exception as error:
                print(error)
        finally:
                self.model.connection.commit()

                
    def delete_all(self):
        if self.model.delete_all():
            self.view.message_print("All rows in table were deleted successfully\n")
        else:
            self.view.message_print("Table was already empty\n")

    def random_insert(self):
        self.view.message_print("How many random records do you want to enter?\n")
        value = str(input())
        self.model.random(value)
        self.model.connection.commit()



    def static_search(self):
        self.view.table_name_select_display()
        while True:
            table_type = str(input())
            if 0 < int(table_type) < 7:
                if table_type == "1":
                    name = "employeers"
                    break
                elif table_type == "2":
                    name = "kitchen_department"
                    break
                elif table_type == "3":
                    name = "quality_certificate"
                    break
                elif table_type == "4":
                    name = "menu"
                    break
                elif table_type == "5":
                    name = "bookkeping"
                    break
                elif table_type == "6":
                    name = "storage"
                    break
                elif table_type == "7":
                    name = "storage_department"
                    break
        items = self.model.static_search(name)
        if items.rowcount:
            self.view.table_rows_display(items)
            return
        self.view.message_print("This table was already empty\n")
        

 