import datetime

# groceries.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

item_list = []
while True:
    item_id = input("Please Input Item ID (#1-20) else enter DONE:")
    if item_id == "DONE":
        break
    else:
        item_list.append(item_id)

product_ids = [3, 12, 15, 5, 7]


def matching_product(pid):
    products_list = [p for p in products if p["id"] == pid]
    return products_list[0]


raw_total = 0
now = datetime.datetime.now()
str_now = now.strftime("%m/%d/%Y, %I:%M %p")

print("--------------------------------------")
print("Jason's Grocery Store")
print("286 East 10th St, New York, New York")
print("--------------------------------------")

print("Date: " + str_now)
print("Shopping Cart Items:")

for pid in product_ids:
    product = matching_product(pid)
    raw_total = raw_total + product["price"]
    print(" + " + product["name"] + " " + '${0:.2f}'.format(raw_total))

tax = raw_total * 0.0875
grand_total = raw_total + tax

str_raw_total = '${0:.2f}'.format(raw_total)
str_tax = '${0:.2f}'.format(tax)
str_grand_total = '${0:.2f}'.format(grand_total)

print("Subtotal: " + str_raw_total)
print("NYC Tax: " + str_tax)
print("Grand Total: " + str_grand_total)
print("--------------------------------------")
print("Thank you for shopping with us.")
print("Have a good day!")
