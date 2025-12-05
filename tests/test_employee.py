import pytest
from Employee import Employee

@pytest.mark.parametrize(
    "first,last,holidays,expected_email",[("Safiya", "Makhlouf", 10, "Safiya.Makhlouf@ec-nantes.fr"), ("Alice", "Martin", 5, "Alice.Martin@ec-nantes.fr"), ("Bob", "Martin", -100, "Bob.Martin@ec-nantes.fr"), pytest.param("Bob", "Martin", 10, "Bob.Martin@mail.fr", marks=pytest.mark.xfail)])
def test_employee_parametrize(first, last, holidays, expected_email):
    if holidays <= 0:
        with pytest.raises(AssertionError):
            Employee(first, last, holidays)
    else:
        emp = Employee(first, last, holidays)
        assert emp.email == expected_email

@pytest.fixture
def employee():
    """Fixture pour créer un employé de test"""
    return Employee("Alice", "Dupont", 10)

def test_fullname(employee):
    """Teste la méthode fullname"""
    assert employee.fullname() == "Alice Dupont"

def test_newHoliday(employee):
    """Teste l'ajout de jours de congé"""
    employee.newHoliday(5)
    assert employee.holiday_left == 15

def test_email(employee):
    """Teste l'email généré"""
    assert employee.email == "Alice.Dupont@ec-nantes.fr"

def test_holiday_positive():
    """Teste que l'assertion empêche les congés négatifs"""
    with pytest.raises(AssertionError):s
        Employee("Bob", "Martin", -5)
