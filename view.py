class View(object):
    @staticmethod
    def action_type_select_display():
        print("Choose an action:\n")
        print("1\tDefinite action in definite table\n2\tStatic search\n3\tRandom")


    @staticmethod
    def table_name_select_display():
        print("Choose table name:\n")
        print("1\temployeers\n2\tkitchen_department\n3\tquality_certificate\n4\tmenu\n5\tbookkeping\n6\tstorage\n7\tstorage_department\n")

    @staticmethod
    def action_select_display():
        print("Choose an action with table:\n")
        print("1\tShow items in table\n2\tUpdate item in table\n3\tCreate new item in table\n"
        "4\tDelete table item\n5\tDelete all data from table\n")

    @staticmethod
    def enter_cortege_item_display(item):
        print("Enter {}".format(item))

    @staticmethod
    def table_rows_display(items):
        cursor = items
        row = items.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

    @staticmethod
    def question_about_end_display():
        print("Continue to work with Database?(Yes - y/No - n)\n")

    @staticmethod
    def message_print(message):
        print(message)

