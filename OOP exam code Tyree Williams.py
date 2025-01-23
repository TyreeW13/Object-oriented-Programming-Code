class Product:
    
    """
    This class allows the user to set the values of the product and calculate shipping cost.
    
    Args:
        Name - This is the products name. It helps users find the product.
        Description - This is the product description. It helps users understand what the product is/does.
        Price - This is the products price. It lets the user know the list price.
        Weight -  This is the products weight, It contributes to the calculate shipping algorithm.
    returns:
        This class returns the shipping cost depending on the weight of the product. If the product weights less than 1000g it will cost £5, If it weighs more than 1000g but less than 5000g shipping cost is £8 and if its more than 5000g the shipping cost is £10.
    
    raises:
        This class raises errors if the data entered for the name and description isnt a string it will tell the user to enter text. If the data entered for the Price and weight isnt a integer it will tell the user to enter a number.
    
    
    """
    
    def __init__(self):
        self._name = str
        self._description = str
        self._price = float
        self._weight = int
    
    """The Name getter method"""
    @property
    def name(self):
        return self._name
    
    """This is a setter method for the product name, it checks if data entered is a string and will raise a valueError if not"""
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
            print(f"Product name: {self._name}")
        else:
            raise ValueError("Please enter text!")
        
    """The description Getter method"""
    @property
    def description(self):
        return self._description
    
   
    """This setter method sets the description and checks if data entered is a string/text and will riase a value error if not."""    
    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
            print(f"Product description: {self._description}")
        else:
            raise ValueError("Please enter text!")
    
    """The price getter method"""
    @property
    def price(self):
        return self._price
    
    """This sets the new price and checks if data entered is an integer/number"""
    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self._price = price
            print(f"The price is: £{self.price}")
        else:
            raise ValueError("Please enter a number!")
    
    
    @property
    def weight(self):
        return self._weight
    
    """This setter method and if statemet set the new value, and checks if what is entered is a number"""
    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight
            print(f"The weight of the product in Grams: {self.weight}g")
        else:
            raise ValueError("Please enter a number!")
        
        
    """This is the algorithm for calculating the shipping cost"""
    def calculate_shipping(self):
        if self.weight <= 1000:
            print("The shipping cost is £5")
        elif self.weight > 1000 and self.weight < 5000:
            print("The shipping cost is £8")
        else:
            print("The shipping cost is £10")
            
class Book(Product):
    
    """
    This class is a derived class from the Product parent class, Its purpose is to add two new properties and calculate shipping based on iof a book is paperback or hardback.
    
    Args:
        self.paperback is set to a boolean of True, you can change this to false by calling the property in an instance of Book and changing the value to false.
        
    returns:
        if Self.paperback is true it will return the shipping cost for paperback is £3 if self. paperback is false it will return the shipping cost of hardback is £4
    """
    """This super().__init__ allows inheritance of the superclasses properties and methods which is the product classs"""
    def __init__(self):
        super().__init__()
        self._isbn = int
        self._paperback = True
    
    """This is a getter method for the isbn"""
    @property
    def isbn(self):
        return self._isbn
    
    """This is the setter method for the isbn it raises a value if the value passed isnt an int"""
    @isbn.setter
    def isbn(self,number):
        if isinstance(number, int):
            self._isbn = number
            print(f"ISBN: {self._isbn}")
        else:
            raise ValueError("Please enter a number")
    """This is a paperback propert so we can access the private paperback class"""
    @property
    def paperback(self):
        return self._paperback
        
    """This setter method makes sure that the value entered is a boolean"""
    @paperback.setter
    def paperback(self, value):
        if isinstance(value, bool):
            self._paperback = value
        else:
            raise ValueError("Please eneter either True or False")
    
    
    """The calculate shipping method is polymorphic and has overridden the products class version of calculating shipping."""
    def calculate_shipping(self):
        if self.paperback == True:
            print("The shipping cost for paperback is £3")
        else:
            print("The shipping cost for hardback is £4")


class lord_of_the_rings(Book):
    
    """
    This Shows further inheritance
    
    args:
    None
    
    returns:
    The name of the book and a description
    
    raises:
    none
    """
    
    def __init__(self):
        super().__init__()
        self.name = "The Lord Of The Rings"#
        self.description
"""Here you can edit the weight, paperback or hardback versions to get different outcomes"""
my_product = Product()
my_product.weight = 5060
my_product.calculate_shipping()
my_product.price = 1000.00
my_product.price
my_product.description = "Call people with it"
my_product.description
my_product.name = "Phone"
my_product.name
print("________________________")
my_book = Book()
my_book.name = "This shows inheritance"
my_book.name
my_book.description = "Inheritance again"
my_book.description
my_book.price = 20.50
my_book.price
my_book.weight = 50
my_book.weight
my_book.isbn = 99919
my_book.isbn
my_book.paperback = False
my_book.calculate_shipping()
print("________________________")
fav_book = lord_of_the_rings()
fav_book.paperback = False
fav_book.calculate_shipping()
fav_book.description = "A tale for the ages"
fav_book.description
fav_book.price = 3.50
fav_book.price
fav_book.isbn = 131213
fav_book.isbn
