class person:
    def __init__ (self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
person = person("George", 32)
print(person.get_name())
print(person.get_age())
