from application.salary import calculate_salary

from db.people import get_employees

from datetime import datetime

if __name__ == '__main__':
    calculate_salary(30000, 5000)
    get_employees(1)
    print(datetime.now())
