class Notebook():
    def __init__(self, year, price):
        self.year = year
        self.price = price

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_info(self):
        return f"Year{self.year}, Price{self.get_price}"

    def __add__(self, otherNotebook):
        print("New notebook: " + 1 + "New price: " + 1200 + "$.")

def main():
    my_notebook = Notebook(2023, 670)
    my_new_notebook = Notebook()
    print(f"notebook year: " {my_} )
