
class A:
    def __init__(self,a):
        self.a = a

    def run(self):
        print(f'run {self.a}')

class B:
    def run(self):
        print(f'no run')


class D(A,B):
    def Run(self):
        print('run run go away')

human = D('adol')
print(human.run())
