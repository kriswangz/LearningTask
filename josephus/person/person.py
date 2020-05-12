
# 返回对象
class Person(object):
    
    def __init__(self, name=None, age='0', gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def create_from_reader(cls, item):
        obj = cls()

        name = item[0]
        if isinstance(name, str) and name.isalpha() == True:
            obj.name = name
        else:
            obj.name = None
        
        age = item[1]
        try:
            age = int(age)
        except ValueError:
            obj.age = '0'
        else:  
            if age < 0:
                obj.age = '0'
            else:
                obj.age = str(age)

        gender = item[2]    
        if gender in ('male','female'):
            obj.gender = gender
        else:
            obj.gender = None

        return obj

