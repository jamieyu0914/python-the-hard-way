cars = 100 # 車子有100輛
space_in_a_car = 4.0 # 每輛車有4個空位
drivers = 30 # 現在有30名駕駛
passengers = 90 # 現在有90名乘客
cars_not_driven = cars - drivers # 有70輛車沒有駕駛開
cars_driven = drivers # 有30輛車有駕駛開
carpool_capacity = cars_driven * space_in_a_car # 現在一共可以乘載120名乘客
average_passengers_per_car = passengers / cars_driven # 平均每台車要乘載3名乘客

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers acailable.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

# _ 是 underscore, 中文名稱為"下橫線", "下劃線", "下標線", "底線"字符
