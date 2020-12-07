# ------------------------------------------------------------------------ #
# Title: Assignment08.py
# Description: Working with classes
# Version: 3.9
# ChangeLog (Who,When,What):
#   RRoot, 1.1.2030, Created started script
#   RRoot, 1.1.2030, Added pseudo-code to start assignment 8
#   e4ster, 12.6.2020, Modified code to complete assignment 8


# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product. \n

    properties:
        product_name: (string) with the product's name. \n
        product_price: (float) with the product's price. \n

    methods:

    changelog:
        RRoot, 1.1.2030, Created Class \n
        e4ster, 12.6.2020, Modified code to complete assignment 8 \n
    """

    def __init__(self, name="", price=0.0):
        self.__product_name = name
        self.__product_price = price

    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, new_name):
        self.__product_name = new_name

    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, new_price):
        self.__product_price = new_price

    def __str__(self):
        return self.product_name + ',' + self.product_price


# Processing  ------------------------------------------------------------- #
class Processor:
    """Processes data to and from a file with a list of product objects. \n

    properties: \n
    methods:
        save_data_to_file(file_name, list_of_product_objects) \n
        read_data_from_file(file_name) \n
    changelog:
        RRoot, 1.1.2030, Created Class \n
        e4ster, 12.6.2020, Modified code to complete assignment 8 \n
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Reads data from a file into a list of rows (objects).

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of objects
        """
        try:
            text_file = open(file_name, "x")
            text_file.close()
        except FileExistsError:
            pass

        text_file = open(file_name, "r+")
        if text_file.readline() == "":
            text_file.write("(Name),(Price)")
        text_file.close()

        lstOfProductObjects.clear()  # clear current data

        text_file = open(file_name, "r")
        for line in text_file:
            try:
                name, price = line.split(",")
                obj_name = Product(name, price)
                list_of_rows.append(obj_name)
            except ValueError:
                continue
        text_file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(name, price, list_of_objects):
        """
        Adds user input to our data table.

        :param name: String of a task name.
        :param price: String of priority level.
        :param list_of_objects: The initial list of objects.
        :returns: A list of dictionaries.
        """
        new_obj = Product(name, price)
        list_of_objects.append(new_obj)
        return list_of_objects

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        Writes the data to the text file.

        :param file_name: String name of the text file.
        :param list_of_rows: Our list of product objects.
        :return: Nothing
        """
        text_file = open(file_name, "w")
        for element in list_of_rows:
            text_file.write(element.product_name + "," + element.product_price + "\n")
        text_file.close()


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from a file and a list of product objects. \n

    properties: \n
    methods: \n
    changelog:
        RRoot, 1.1.2030, Created Class \n
        e4ster, 12.6.2020, Modified code to complete assignment 8 \n
    """

    @staticmethod
    def print_menu():
        """ Display a menu of choices to the user.

        :return: Nothing
        """
        print('''
            Menu of Options
            1) Add data to the list.
            2) Show data in list.
            3) Save the list and exit.     
            ''')
        print()

    @staticmethod
    def input_menu_choice():
        """
        Gets the menu choice from a user.

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_new_product_data():
        """
        Gets and returns user input for name and price.

        :returns: Two strings.
        """
        while True:
            new_product = input("New Product Name?: ").lower().strip()
            if new_product.strip(" ").isalpha() is True:
                break
            else:
                print("The name can only contain letters.")
        while True:
            try:
                new_price = float(input("New Product Price?: ").lower().strip())
                break
            except (ValueError, TypeError):
                print("The price can't have letters or symbols except '.'")
        return new_product, new_price


# Main Body of Script  ---------------------------------------------------- #

# Step 1: Load data from file into a list of product objects when script starts
Processor.read_data_from_file(strFileName, lstOfProductObjects)

while True:

    # Step 2: Show menu and get user choice.
    IO.print_menu()
    strChoice = IO.input_menu_choice()

    # Step 3: If 1, add new data
    if strChoice.strip() == '1':
        strProduct, strPrice = IO.input_new_product_data()
        Processor.add_data_to_list(strProduct, strPrice, lstOfProductObjects)
        continue  # to show the menu

    # Step 4: If 2, show the data
    elif strChoice.strip() == '2':
        for each_element in lstOfProductObjects:
            print(each_element)
            continue  # to show the menu

    # Step 5: If 3, save the data and exit
    elif strChoice.strip() == '3':
        Processor.write_data_to_file(strFileName, lstOfProductObjects)
        input("Data has been saved. Press 'enter' to exit.")
        break

    else:
        print("That's not an option, try again!")
