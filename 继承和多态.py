class Animal(object):
	def run(self):
		print('Animal is running..')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

def run_twice(animal):
	animal.run()
	animal.run()

a = Animal()
b = Dog()
c = Cat()

print('a is Animal?',isinstance(a,Animal))
print('a is Dog?', isinstance(a,Dog))
print('a is Cat?', isinstance(a, Cat))

run_twice(a)
