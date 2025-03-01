# 1. We are helping out a popular grocery store called Jiho’s Produce.
# Every week the store has to choose the order in which it displays some of its popular items on sale in the front window to attract customers.
# Jiho, the store owner, likes to store the items for the display in a list. Check out the current display list in our code editor. 
# Click Run to print out the list.
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# 2. Jiho found out some great news! "Pineapple" is back in stock.
# Jiho would like to put "Pineapple" in the front of the list so it is the first item customers see in the display window.
# Use .insert() to add "Pineapple" to the front of the list. Print the resulting list to see the change.
# Note: For this list, the front will be the element at index 0
front_display_list.insert(0, "Pineapple")
print(front_display_list)