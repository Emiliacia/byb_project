# Create a list of items sold in cafe under the name menu.
menu = ["tea", "water", "sandwiches", "croissants"]
# Create a dictionarie with stock value for each item called stock
int_Keys_stockDict = {"tea": 6,
                      "water" : 1,
                      "sandwiches": 4,
                      "croissants": 1
                      }
# Create a dictionarie with price value for each item called price
int_Keys_priceDict = {"tea": 2,
                      "water" : 3 ,
                      "sandwiches": 5,
                      "croissants": 4
                      }

#Calculate the total_stock worth in the cafe.
total_stock_worth = 0
for item in menu:
    total_stock_worth += int_Keys_stockDict[item] * int_Keys_priceDict[item]
print( total_stock_worth)
