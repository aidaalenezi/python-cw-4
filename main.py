def my_name():
    print('my name is aida')

def my_meal(food , drink):
    print(f'I like to eat{food} and while drinking {drink}')


def cube(number):
    return number**3
def by_three(number):
      if number%3==0:
           return cube(number)
      else:
           return False
      
my_name()
my_meal('pizza', 'water')
print(cube(6))
print(by_three(5))


