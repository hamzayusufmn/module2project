# North Loop Provisions - Donut Shop Management System
# Your first Python program for Module 2

def welcome_message():
    """Display a welcome message for the donut shop."""
    print("🍩 Welcome to North Loop Provisions! 🍩")
    print("Crafting artisanal donuts in Minneapolis's North Loop")
    print("-------------------------------------------")
# this will display an interactive message welcoming the donut shop, print message will show this message
def show_menu():
    """Display our current donut menu."""
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 4.50,
        "Spyhouse Coffee": 4.00,
        "MN Berry": 4.25,
        "Local Honey": 4.00
        # this will show the menu and prices its important to use , after each price or err will appear 
    }
    
    print("\nToday's Donut Menu:")
    print("------------------")
    for donut, price in menu.items():
        print(f"{donut}: ${price:.2f}")

# Main program
if __name__ == "__main__":
    welcome_message()
    show_menu()
    print("\nReady to serve our community with the finest donuts!")

# listing our donut prices for different prices
small_batch_price = 5.50  # Our signature donuts
seasonal_price = 6.50  # Using local seasonal ingredients
collab_price = 7.50  # Local business collaborations

# Set our daily inventory of items
small_batch_inventory = 36  
seasonal_inventory = 24  
collab_inventory = 12  # Special collaboration items

# Calculate our morning inventory value
total_value = (small_batch_price * small_batch_inventory + 
               seasonal_price * seasonal_inventory + 
               collab_price * collab_inventory)


print("Morning inventory value: $" + str("{:.2f}".format(total_value)))

# Customer information
purchase_total = 28
is_local_resident = True
bike_commuter = True
brought_mug = False

# Initialize rewards
discount = 0

if is_local_resident:
    discount += 0.10  # Supporting our neighbors with 10% off

if bike_commuter:
    discount += 0.05  # Encouraging sustainable transport

if brought_mug:
    discount += 0.05  # Reducing waste

if purchase_total >= 25:
    discount += 0.05  # Bulk order appreciation

# Calculate and display final discount
final_discount = discount * 100
print("Your community rewards discount: " + str(final_discount) + "%")

# Our complete menu organized by category
donut_menu = {
    'Small Batch': [
        'Wild Rice & Honey',  
        'Maple Bacon',  
        'Swedish Cardamom'  
    ],
    'Seasonal': [
        'Apple Cider',  
        'Jucy Lucy', 
        'Lake of the Woods'  
    ],
    'Local Collabs': [
        'Spyhouse Coffee Cake',
        'Fulton Beer & Pretzel',
        'Sweet Science Ice Cream'
    ]
}

# Locally-sourced toppings
toppings = [
    'House-made Sprinkles',
    'Candied Hazelnuts',  # From MN growers
    'Bee Pollen',  
    'Cookie Butter Drizzle'
]

# Track our morning sales
morning_sales = []

# Record our first sale
morning_sales.append({
    'item': 'Wild Rice & Honey',
    'quantity': 2,
    'toppings': ['Bee Pollen'],
    'time': '7:30 AM'
})

# Display our current menu
print("Today's Morning Menu:")
for category, items in donut_menu.items():
    print(category + ":")
    for item in items:
        print(" - " + item)

