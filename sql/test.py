class RemoveStaff():
    # Struct:
    emp_id: int
    first_name: str
    last_name: str
    department: str
    reason: str
    notes: str
    total_elements = 6

    def reset(self):
        self.emp_id = -1
        self.first_name = 'NULL'
        self.last_name = 'NULL'
        self.department = 'NULL'
        self.reason = 'NULL'
        self.notes = 'NULL'
        return


emp = RemoveStaff()

emp.reset()

print(emp.emp_id)

emp.emp_id = 12
emp.first_name = 'Dante'

print(emp.emp_id, emp.first_name)

emp.reset()

print(emp.emp_id, emp.first_name)
emp.total_elements = 99
print(emp.total_elements)