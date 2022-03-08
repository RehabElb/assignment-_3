hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#calc_total= 
total_price = 0 #creating a variable to take all prices (like a box to keep all values added)


for x in prices: # x = 30, 25...35 every iteration of the loop will take a value and add it to the total_price variable
  total_price += x  #adding each element from price list to the existing value

average_price = total_price/len(prices)

print('Average Haircut Price:', average_price)
  
new_prices = [x - 5 for x in prices] # every value/element of the list prices should be $5 less and create new_prices list
print(new_prices)

# new_prices2 = []
# for x in prices:
#   x -= 5
#   new_prices2.append(x)

# print(new_prices2)
  
# print(total_price)



total_revenue = 0

for i in range(len(hairstyles)): # range(0, 5) --> (0,1,2,3,4) - range(5)--> (0,1,2,3,4)
  total_revenue += (prices[i] * last_week[i])
  
print('Total Revenue:', total_revenue)

average_daily_revenue = total_revenue / 7

print('Average Daily Revenue: $', average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
# i takes its value from range 0 to 8 (a number every iteration of the loop) and is used as index number for the 2 lists (hairstyles and new_prices).
# if new_prices[i] is less than 30 then I will insert the same index in hairstyles in my new list(cuts_under_30)
# if the element at the index i in new_prices list is greater than 30 then the correspondant element in hairstyles list will be skipped
print(cuts_under_30)



