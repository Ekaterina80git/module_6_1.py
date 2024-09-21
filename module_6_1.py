
class Animal:
    alive = True # живой
    fed = False # накормленный
    def __init__(self,name):  # название животного
         self.name = name

    def __eat__(self,food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
              print(f'{self.name} не стал есть  {food.name}')
              self.alive = False
class Plant:
    edible = False # съедобность
    def __init__(self,name): # название растения
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass
class Flower(Plant):
     edible = False #цветы не съедобны
class Fruit(Plant):
      edible = True

a1= Predator("Волк с Уол-Стрит")
a2= Mammal("Хатико")
p1=Flower("Цветик семицветик")
p2= Fruit("Заводной апельсин")

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.__eat__(p1)
a2.__eat__(p2)


print(a1.alive)
print(a2.fed)