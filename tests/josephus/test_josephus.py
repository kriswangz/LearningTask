from josephus.josephus.Josephus import Ring
from josephus.person.person import Person
import operator
from josephus.file_adapter.read_files import ReadTXT, ReadCSV, ReadZIP

def test_Ring_init_from_reader():

    reader = [

        ['Chris','24','male'],
        ['Mary','20','female']

    ]

    ring = Ring(reader)

    assert len(ring) == len(reader)

def test_Ring_create_from_txt():
    txt_reader = ReadTXT('./data','people.txt')

    res = txt_reader.read('r')

    reader = [
        ['name','age','gender'],
        ['Chris','24','male'],
        ['Anna','20','female'],
        ['Bob','30','male'],
        ['David','20','male']
    ]
    assert res == reader

def test_Ring_create_from_csv():
    csv_reader = ReadCSV('./data','people.txt')

    res = csv_reader.read('r')

    reader = [
        ['name','age','gender'],
        ['Chris','24','male'],
        ['Anna','20','female'],
        ['Bob','30','male'],
        ['David','20','male']
    ]
    assert res == reader    

def test_Ring_create_from_zip_txt():
    zip_txt_reader = ReadZIP('./data/data.zip','people.txt')

    res = zip_txt_reader.read('r')

    reader = [
        ['name','age','gender'],
        ['Chris','24','male'],
        ['Anna','20','female'],
        ['Bob','30','male'],
        ['David','20','male']
    ]
    assert res == reader 
    
def test_Ring_create_from_zip_csv():
    zip_csv_reader = ReadZIP('./data/data.zip','people.csv')

    res = zip_csv_reader.read('r')

    reader = [
        ['name','age','gender'],
        ['Chris','24','male'],
        ['Anna','20','female'],
        ['Bob','30','male'],
        ['David','20','male']
    ]
    assert res == reader 
