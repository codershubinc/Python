# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.


size = 'Large'
coffee = 'Cappuccino'
Extra_shot = True

if Extra_shot :
    coffee =  size + ' coffee with extra shot of espresso'
else:
        coffee = size + 'coffee '
    

print("Order",coffee)