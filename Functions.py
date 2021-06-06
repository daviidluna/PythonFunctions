def my_Function():
    print('hello world from a function')
my_Function()

def clouds():
    print('clouds look nice')
clouds()

def myFunction():
    print('hi from a function')
myFunction()

def anotherFunction():
    print('this is a new function')
anotherFunction()

def waterbottle():
    print('my water bottle is blue from a function')
waterbottle()

def NoteBook():
    print('this is my notebook from a function')
NoteBook()

#Arguments or args
def function(firstName):
    print(firstName)
function('david')

def firstFunction(first_name):
    print(first_name)
firstFunction('david')
firstFunction('David')
firstFunction('DAVID')

def secondFunction(title):
    print(title)
secondFunction('a promised land')
secondFunction('dreams from my father')

def book(firstname):
    print(firstname + ' luna')
book('david')
book('David')

def game(typ):
    print(typ + ' battles')
game('btd')

def sport(boxing):
    print(boxing + ' gym')
sport('foley\'s')

def name(fname, lname):
    print(fname + ' ' + lname)
name('david', 'luna')

def laptop(color):
    print(color)
laptop('my laptop is grey')

#newlines
def otherName(firstname, middlename, lastname):
    print(firstname +  middlename +  lastname)
otherName('david', ' castro', ' laster')

def cup(color, size):
    print(color + ' ' + size)
cup('blue', 'big')

def book (first, second, third):
    print(first + ' ' + second + third)
book('a', 'promised', ' land')

#arbitrary args
def hats(*colors):
    print('the best hat is the color ' + colors[1])
hats('blue', 'green', 'red', 'purple')

def glass(*tipo):
    print('this is the kind of glass: ' + tipo[3])
glass('float', 'toughened', 'painted', 'patterned', 'solar', 'laminated')

def shoes(*mine):
    print('these are my shoes: ' + mine[4])
shoes('ones', 'elevens', 'fours', 'ones', 'airs')

def airport(*best):
    print('the best airport is the one in ' + best[2])
airport('mexico', 'utah', 'san fran', 'denver', 'cancun')

#(practice problems)
def nam(name, age):
    print(name, age)
nam('david', 20)

def func1(number_1, number_2, number_3):
    print(number_1, number_2, number_3)
func1(20, 40, 60)

def showEmployee(name, salary):
    print(name, salary)
showEmployee('Employee ben\'s salary is: ', '9000')

def showEmployeee(sentence):
    print(sentence)
showEmployeee('employee ben salary is 9000')