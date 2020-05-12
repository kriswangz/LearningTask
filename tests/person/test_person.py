import pytest
import operator
from josephus.person.person import Person


def test_person_with_parameter():
    someone = Person('Chris', '24', 'male')

    assert someone.name == 'Chris'
    assert someone.age == '24'
    assert someone.gender == 'male'


def test_person_without_parameter():
    someone = Person()

    assert someone.name == None
    assert someone.age == '0'
    assert someone.gender == None


def test_person_create_from_reader_without_errors():
    reader = ['Chris', '24', 'male']

    someone = Person.create_from_reader(reader)

    assert someone.name == 'Chris'
    assert someone.age == '24'
    assert someone.gender == 'male'


def test_person_create_from_reader_with_errors():
    reader = [2, -24, 1]

    someone = Person.create_from_reader(reader)

    assert someone.name == None
    assert someone.age == '0'
    assert someone.gender == None
