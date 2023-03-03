class Cat:
    xвост = True

    def init(self, name, age):
        self._name = name
        self.age = age


    @property.name
    def name(self, name):
        self._name = name
    def name(self):
        print(self._name)

    def __may(self):
        print(self._name, 'мяукает')

    def __str__(self):
        return f'name is {self._name}\n' \
               f'age is {self.age}'

    def __len__(self):
        return len(self._name)

    def _x2(self):
        self.__age *= 9
        print(self)

