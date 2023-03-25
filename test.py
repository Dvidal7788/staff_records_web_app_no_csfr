# s = 'hello123!'

# for char in s:
#     print(not char.isalnum())

# my_list = [{'emp_id': 0, 'name': 'David', 'department': 'Director'}]

# for entry in my_list:
#     print(entry)
#     for key in entry:
#         print(key)


# import os
# filename = 'delete.txt'
# os.system(f'rm {filename}')

# with open('test.csv', 'w') as file:
#     writer = csv.DictWriter(file)

# from werkzeug.security import check_password_hash, generate_password_hash

# import sqlite3

# # print(generate_password_hash('0000', method='pbkdf2:sha512'))

# db = sqlite3.connect("sql/backend.db")
# # # # cur = db.cursor()
# db.execute("INSERT INTO manager_pin VALUES (?)", (generate_password_hash('0000', method='pbkdf2:sha512'),))
# db.commit()


# x = 0
# y = 0

# x = y = 7

# print(x, y)

# access_granted = False
# remove_staff_pg2 = False
# access_granted = remove_staff_pg2 = True

# print(access_granted, remove_staff_pg2)



# # GET COLUMN NAMES
# import sqlite3

# db = sqlite3.connect("staff.db")

# # tmp_cursor = db.execute("SELECT sql FROM sqlite_master WHERE tbl_name = 'staff' AND type = 'table'")
# # tmp_cursor = db.execute("SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('staff')")


# # tmp_cursor = db.execute("PRAGMA table_info('staff')")
# tmp_cursor = db.execute("SELECT name FROM pragma_table_info('staff')")
# # db.commit()

# # tmp_cursor = d

# # print(tmp_cursor)
# for item in tmp_cursor:
#     print(item[0])


# from datetime import datetime

# now = datetime.now()
# print(now)
# print(now.time().hour)

# import re
# email = 'dave@gmail.com'

# if re.search('.+@.+\..+', email):
#     print('valid')
# else:
#     print('invalid')