items = ["pen","whitener","notebook","glue","textbook"]
stock_counts = [5,0,36,1,10]

inventory = {item: count for item,count in zip(items,stock_counts)}
print("Full inventory:",inventory)

in_stock_items = [item for item in items if inventory[item]>0]
print("Items in stock are:",in_stock_items)

chosen_item = input("Which item would you like to buy from here?!")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item," This item is out of stock")
    exit()

prices = [10,40,999,10,9999]
markup = int(input("Enter the markup"))

marked_up_prices = list(map(lambda p: p + markup,prices))
print(marked_up_prices)

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("The price of",chosen_item,"is",chosen_price)

inventory[chosen_item] = inventory[chosen_item]- 1
print(inventory[chosen_item])

print("")
print("============== SCHOOL ITEM SHOPPING LIST ==================")
print("item(s) bought:",chosen_item)
print("Price paid:",chosen_price)
print ("Updated inventory:",inventory)
