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

def book(first, second, third):
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

def jobs(*number):
    print('the best job has been ' + number[0])
jobs('none', 'fres', 'this one', 'chilis')

def times(*when):
    print('what time is it? ' + when[4])
times('4', '5', '6', '7', '800')

def math(*answer):
    print('what is two plus two? ' '\n the answer is ' + answer[3])
math('3', '5', '7', '4', '9', '90')

#keyword arguments
def money(optionOne, optionTwo, optionThree):
    print('i usually save money in ' + optionThree)
money(optionThree = 'twenties', optionTwo = 'tens', optionOne = 'ones')

def emotions(One, Two, Three, Four):
    print('usually i feel '+ Three)
emotions(Four = 'fun', Three = 'great', Two = 'sad', One = 'happy') 

def bookes(bookOne, bookTwo, bookThree, bookFour):
    print('my favorite book has been ' + bookThree)
bookes(bookFour = 'boys and sex', bookThree = 'the book of lost things', bookTwo = 'out of this furnace', bookOne = 'dreams from my father')

def laptop(colorOne, colorTwo, colorThree):
    print('i have a macbook that is ' + colorOne)
laptop(colorThree = 'red', colorTwo = 'black', colorOne = 'grey')

def days(dayOne, dayTwo, dayThree):
    print('my favorite day is ' + dayThree)
days(dayThree = 'friday', dayTwo = 'thursday', dayOne = 'wednesday')

def paintings(paintingOne, paintingTwo, paintingThree):
    print('i have three paintings.' '\n my favorite?\n ' + paintingOne)
paintings(paintingThree = 'piano', paintingTwo = 'jesus', paintingOne = 'prague')

def cups(cupOne, cupTwo, cupThree):
    print('my cup is the color: ' + cupOne)
cups(cupThree = 'blue', cupTwo = 'yellow', cupOne = 'white')

#arbitrary keyword arguments
def unknown(**list):
    print('this list is not defined because of this reason: ' + list['reasonOne'])
unknown(reasonZero = 'comps broke down', reasonOne = 'visual studio crashed')

def random(**months):
    print('today\'s month is: ' + months['monthTwo'])
random(monthTwo = 'may', monthOne = 'june', monthThree = 'july')

def drinks(**anyKind):
    print('my favorite drink is: ' + anyKind['thirdOne'])
drinks(firstOne = 'water', secondOne = 'cola', thirdOne = 'energy')

def wallet(**Colors):
    print('my wallet is: ''\n the color ' + Colors['fifth'])
wallet(first = 'pink', second = 'grey', third = 'blue', fourth = 'yellow', fifth = 'brown', sixth = 'black')

def restaurants(**types):
    print('her fav restaurant is: ' + types['two'])
restaurants(one = 'heh', two = 'sizzler', three = 'here', four = 'there')

#(practice problems)
def nam(name, age):
    print(name, age)
nam('david', 20)
def nameAndAge():
    print('david', '20')
nameAndAge()

def func1(number_1, number_2, number_3):
    print(number_1, number_2, number_3)
func1(20, 40, 60)

def calculation(a, b):
    return a+b, a-b
res = calculation(40, 10)
print(res)
def Calculation(a, b):
    return a+b, a-b
add, sub = Calculation(70, 20)
print(add)
print(sub)

def showEmployee(name, salary):
    print(name, salary)
showEmployee('Employee ben\'s salary is: ', '9000')
def showEmployeee(sentence):
    print(sentence)
showEmployeee('employee ben salary is 9000')
def ShowEmployee():
    print('bens salary is 9000.')
ShowEmployee()

def displayStudent(name, age):
    print(name, age)
displayStudent('emma', 20)
showStudent = displayStudent
showStudent('emma', 20)
def books(favorite, leastFavorite):
    print(favorite, leastFavorite)
books('favorite: out of this furnace', '\nleast favoirte: dictionary')
twoBooks = books
twoBooks('favorite: out of this furnace', '\nleast favoirte: dictionary')
def showGrades(fail, passs):
    print(fail, passs)
showGrades('you fail', 'me')
what = showGrades
what('you fail', 'me')



