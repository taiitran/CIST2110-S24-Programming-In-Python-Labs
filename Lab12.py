# Lab 12
# Author: Tai Tran

# Lab 12 will show basic understanding of Object Oriented Programming in Python.


# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)

class Product:
    """
    Product class that has a name, price, and product_id
    """

    def __init__(self, name: str, price: float, product_id:int) -> None: 
        self.name = name
        self.price = price
        self.product_id = product_id

    


# 2. Create a method called __str__ that returns a string with the following format:
# Product: <name>, Price: <price>, ID: <product_id>
# Hint: use f-strings to format the string.
    def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}"
    

# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.
# also create a __str__ method that returns a string with the following format:
# Customer: <name>, ID: <customer_id>
# Hint: use f-strings to format the string.

class Customer:
    def __init__(self, name: str, customer_id: int) -> None:
        self.name = name
        self.customer_id = customer_id 
        self.cart = []

    def __str__(self) -> str:
        return f"Customer: {self.name}, ID: {self.customer_id}" 


# 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was added and the customer's name.
    def add_to_cart(self, product: Product) -> None:
        """Adds a product to the cart list.

        Args: 
            product (Product): Product to add
        """
        self.cart.append(product)
        print(f"{product.name} was added to {self.name}'s cart")  


# 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.
    def remove_from_cart(self, product: Product) -> None:
        """
        Removes a product from the cart list.

        Args:
        product (Product): Product to remove   
        """
        self.cart.remove(product)
        print(f"{product.name} was removed from {self.name}'s cart") 


    # 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After printing out the total, empty the cart.
    # Hint: you will need to loop through the cart and add up the prices.
    def checkout(self) -> None:
            """Calculates the total price of all the products in the cart and prints out the total. Empty the cart after printing out the total."""
            total = 0
            for product in self.cart:
                total += product.price
            print(f"{self.name}'s total is: {round(total, 2)}")
            self.cart = []


 
# 7. Create a method called display_products that prints out all the products in the cart list.(use the __str__ method from the Product class)
    def display_products(self) -> None:
        """Prints out all the products in the cart list."""
        print(f"{self.name}'s cart:") 
        for product in self.cart:
            print(product)

# 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. (use the tabulate library)
# Make a nice table table using the tabulate library.
    def print_products_pretty(self) -> None:
        """Prints out all the products in the cart list in a nice table."""
        from tabulate import tabulate
        
        print(f"{self.name}'s cart:")
        print(
            tabulate(
                [
                    {
                        "Name": product.name,
                        "Price": product.price,
                        "Product ID": product.product_id
                    } 
                    for product in self.cart
                ],
                headers="keys",
                tablefmt="fancy_grid"  
        )
    )
 
                  
# 9. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.

class Store:
    """Store class that has products and customers."""

    def __init__(self) -> None:
        self.products = [] 
        self.customers = []
    

# 10. Create a method called add_product that takes in a Product object and adds it to the products list.
    def add_product(self, product: "Product") -> None:
        """Adds a product to the products list.

        Args:
            product (Product): Product to add
        """
        self.products.append(product) 
        print(f"{product} was added to the store.")


# 11. Create a method called add_customer that takes in a Customer object and adds it to the customers list.
    def add_customer(self, customer: "Customer") -> None:
        """Adds a customer to the customers list.

        Args:
            customer (Customer): Customer to add
        """
        self.customers.append(customer)
        print(f"{customer} was added to the store")


# 12. Create a method called display_products that prints out all the products in the products list.
    def display_products(self) -> None:
        """Prints out all the products in the products list."""
        for product in self.products:
            print(product)

# 13. Create a method called display_customers that prints out all the customers in the customers list.
    def display_customers(self) -> None:
        """Prints out all the customers in the customers list."""
        for customer in self.customers:
            print(customer)

# Typically we would create another file and import the classes we created. For this lab, we will just create the objects in this file to show how its possible.

# 14. Create a store object called store.
marlton_apple = Store()

# 15. Create a product object called product1 with the following attributes:
# name: "iPhone 12"
# price: 799.99
# product_id: 1

product1 = Product("iPhone 12", 799.99, 1)
 
# 16. Create a product object called product2 with the following attributes:
# name: "iPhone 12 Pro"
# price: 999.99
# product_id: 2

product2 = Product("iPhone 12 Pro", 999.99, 2)


# 17. Create a product object called product3 with the following attributes:
# name: "iPhone 12 Pro Max"
# price: 1099.99
# product_id: 3

product3 = Product("iPhone 12 Pro Max", 1099.99, 3)

# 18. Create a customer object called customer1 with the following attributes:
# name: "John"
# customer_id: 1

customer1 = Customer("John", 1)
print(customer1)

# 19. Create a customer object called customer2 with the following attributes:
# name: "Jane"
# customer_id: 2

customer2 = Customer("Jane", 2)

# 20. Add product1 to the store using the add_product method.
marlton_apple.add_product(product1)

# 21. Add product2 to the store using the add_product method.
marlton_apple.add_product(product2)

# 22. Add product3 to the store using the add_product method.
marlton_apple.add_product(product3)

# 23. Add customer1 to the store using the add_customer method.
marlton_apple.add_customer(customer1)

# 24. Add customer2 to the store using the add_customer method.
marlton_apple.add_customer(customer2)

# 25. Add product1 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product1)

# 26. Add product2 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product2)

# 27. Add product3 to customer2's cart using the add_to_cart method.
customer2.add_to_cart(product3)

# 28. Display current products in customer1's cart using the display_products method.
customer1.display_products()

# 29. Display current products in customer2's cart using the display_products method.
customer2.display_products()

# 30. Checkout customer1's cart using the checkout method.
customer1.checkout()

# 31. Checkout customer2's cart using the checkout method.
customer2.checkout()

# 32. Display current products in customer1's cart using the display_products method. (should be empty)
customer1.display_products()
 