class Dog():
    def __init__(self,name):
        self.name = name
    
    def bark(self):
        print("I am a dog.My name is:" +self.name)

class labrador(Dog):
    def __init__(self,name,owner):
        self.name=name
        self.owner=owner
    
    def bark(self):
        print("I am Labrador.My master is:"+self.owner)


class GermanShephard(Dog):
    def __init__(self,name,owner):
        self.name=name
        self.owner=owner

        
d=Dog('mark')
l=labrador('Lucy','Billadin')
g=GermanShephard('max','billgate')

d.bark()
l.bark()
g.bark()


        