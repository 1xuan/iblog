# singleton pattern

#### Advantages of design patterns

- They are reusable across multiple projects
- The architectural level of problems can be solved
- They are time-tested and well-proven, which is the experience of developers and architects
- They have reliability and dependence

#### Classifying patterns

- Creational patterns
- Structural patterns
- Behavioral patterns

### understanding singleton pattern

In brief, the intentions of the Singleton design pattern are as follows:

- Ensuring that one and only one object of the class gets created
- Providing an access point for an object that is global to the program
- Controlling concurrent access to resources that are shared

***Implementing a classical Singleton in Python***
~~~python
class Singleton:
    __instance = None
    def __init__(self):
	if not Singleton.__instance:
	    print(" __init__ method called..")
	else:
	    print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
	if not cls.__instance:
	    cls.__instance = Singleton()
	return cls.__instance

s = Singleton() ## class initialized, but object not created
print("Object created", Singleton.getInstance()) # Object gets created here
s1 = Singleton() ## instance already created
~~~
	
***create singleton pattern by metaclass programming***
	
	class MetaSingleton(type):
	    _instances = {}
	    def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
		    cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


	class Logger(metaclass=MetaSingleton):
	    pass


	logger1 = Logger()
	logger2 = Logger()

	print(logger1, logger2)
	

***

# The Factory Pattern

In object-oriented programming, the term factory means a class that is responsible for creating objects of other types.Typically, the class that acts as a factory has an object and methods associated with it. The client calls this method with certain parameters; objects of desired types are created in turn and returned to the client by the factory.

A factory provides certain advantages that are listed here:

- The first advantage is loose coupling in which object creation can be independent of the class implementation.
- The client need not be aware of the class that creates the object which, in turn, is utilized by the client. It is only necessary to know the interface, methods, and parameters that need to be passed to create objects of the desired type. This simplifies implementations for the client.
- Adding another class to the factory to create objects of another type can be easily done without the client changing the code. At a minimum, the client needs to pass just another parameter.
- The factory can also reuse the existing objects. However, when the client does direct object creation, this always creates a new object.

***The Simple Factory pattern***

~~~python
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('Bhow Bhow')


class Cat(Animal):
    def do_say(selfs):
        print('Mhow Mhow')


## forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Which animal should make sound Dog or Cat? \n')
    ff.make_sound(animal)

~~~

***The Factory Method pattern***

It brings in a lot of flexibility and makes the code generic, not being tied to a certain class for instantiation.

~~~
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class PatentSection(Section):
    def describe(self):
        print("Petent Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSection(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())


class facebook(Profile):
    def createProfile(self):
        self.addSection(PatentSection)


if __name__ == '__main__':
    profile_type = input("which profile do you want to create facebook or linkedin?")
    profile = eval(profile_type.lower())()
    print("create profile...", type(profile).__name__)
    print("profile has sections -", profile.getSection())

~~~

***The Abstract Factory pattern***

The main objective of the Abstract Factory pattern is to provide an interface to create families of related objects without specifying the concrete class.

~~~
from abc import ABCMeta, abstractmethod
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass
    @abstractmethod
    def createNonVegPizza(self):
        pass
class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()
    def createNonVegPizza(self):
        return ChickenPizza()
class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()
    def createNonVegPizza(self):
        return HamPizza()

class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)
class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)
class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)
class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)

class PizzaStore:
    def __init__(self):
        pass
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()
~~~

***

# The Façade Pattern

***Understanding the Façade design pattern***

- It provides a unified interface to a set of interfaces in a subsystem and defines a high-level interface that helps the client use the subsystem in an easy way.
- Façade discusses representing a complex subsystem with a single interface object. It doesn't encapsulate the subsystem but actually combines the underlying subsystems.
- It promotes the decoupling of the implementation with multiple clients

~~~
# Facade
class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


# subsystem
class Hotelier:
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking \n\n")


class Florist:
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer:
    def __init__(self):
        print("Food Arrangements for the Event --")

    def setCuisine(self):
        print("Chinese & Continental cuisine to be served\n\n")


class Musician:
    def __init__(self):
        print("Musical Arrangements for the marriage -- ")

    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")


# client
class You:
    def __init__(self):
        print("You:: whoa! Marriage Arrangement??!!!")

    def askEventManager(self):
        print("You:: Let's Contact the Event Manage\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


you = You()
you.askEventManager()
~~~

# The Proxy Pattern

***Understanding the Proxy design pattern***

The Proxy design pattern essentially does the following:

- It provides a surrogate for another object so that you can control access to the original object
- It is used as a layer or interface to support distributed access
- It adds delegation and protects the real component from undesired impact

~~~
from abc import ABCMeta, abstractmethod


# client
class You:
    def __init__(self):
        print("You:: Lets buy the short!")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! shirt is mine!")
        else:
            print("You:: I should earn more money!")


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# realsubject of subject 
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.acount = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False


# proxy of subject
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number:")
        self.bank.setCard(card)
        return self.bank.do_pay()


you = You()
you.make_payment()
~~~

# The Observer Pattern

***Understanding the Observer design pattern***

The main intentions of the Observer pattern are as follows:

- It defines a one-to-many dependency between objects so that any change in one object will be notified to the other dependent objects automatically
- It encapsulates the core component of the Subject

a sample:

~~~
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(*args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, ":: Got", args)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, ":: Got", args)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll('NOTIFICATION')
~~~

**The Observer pattern in the real world**

~~~
from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News:", self.__latestNews


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.addNews('Hello World!')
    news_publisher.notifySubscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.addNews('My second news!')
    news_publisher.notifySubscribers()

~~~

# The Command Pattern

***Understanding the Command designpattern***

The main intentions of the Command pattern are as follows:

- Encapsulating a request as an object
- Allowing the parameterization of clients with different requests
- Allowing to save the requests in a queue
- Providing an object-oriented callback

a sample:

~~~
from abc import ABCMeta, abstractmethod
class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv
    def execute(self):
        pass
class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv
    def execute(self):
        self.recv.action()
class Receiver:
    def action(self):
        print("Receiver Action")
class Invoker:
    def command(self, cmd):
        self.cmd = cmd
    def execute(self):
        self.cmd.execute()
if __name__ == '__main__':
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
~~~

**Implementing the Command pattern in the real world**

~~~
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")


class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':
    # Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)


    # Invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
~~~

# The Template Method Pattern

***Understanding the Template Method design pattern***

In short, the main intentions of the Template Method pattern are as follows:

- Defining a skeleton of an algorithm with primitive operations
- Redefining certain operations of the subclass without changing the algorithm's structure
- Achieving code reuse and avoiding duplicate efforts
- Leveraging common interfaces or implementations

a sample:

~~~
from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectionSource(self):
        pass

    @abstractmethod
    def compilerToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectionSource()
        self.compilerToObject()
        self.run()


class iOSCompile(Compiler):
    def collectionSource(self):
        print("Collecting Swift Source Code")

    def compilerToObject(self):
        print("Compiler Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


iOS = iOSCompile()
iOS.compileAndRun()
~~~

# The State Design Pattern

***Understanding the State design pattern***

- State : This is considered to be an interface that encapsulates the object's behavior. This behavior is associated with the state of the object.
- ConcreteState : This is a subclass that implements the State interface.ConcreteState implements the actual behavior associated with the object's particular state.
- Context : This defines the interface of interest to clients. Context also maintains an instance of the ConcreteState subclass that internally defines the implementation of the object's particular state.

a sample:

~~~
from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self):
        pass

class ConcreteStateB(State):
    def Handle(self):
        print("ConcreteStateB")


class ConcreteStateA(State):
    def Handle(self):
        print("ConcreteStateA")


class Context(State):

    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def Handle(self):
        self.state.Handle()
        

context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()

context.setState(stateA)
context.Handle()
~~~

**Let's now take a look at a real-world use case for the State design pattern.**

~~~
class ComputerState:
    name = 'state'
    allowed = []

    def swith(self, state):
        if state.name in self.allowed:
            print('Current:',self,' => switched to new state',state.name)
            self.__class__ = state
        else:
            print('Current:',self,' => switching to',state.name,'notpossible.')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.swith(state)


if __name__ == '__main__':
    comp = Computer()
    comp.change(On)
    comp.change(Off)

    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)

~~~


























