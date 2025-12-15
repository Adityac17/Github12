shopping_list = ["milk", "pasta", "eggs", "bread", "spam", "rice"]

# item_to_find = "spam"
item_to_find = "pizza"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index


if item_to_find in shopping_list:
    found_at = shopping_list.index(found_at)  #must simpler way to write than line 7 to 9


print("Item found at position {}".format(found_at))

else:
    print("{} was not found in the list ".format(item_to_find))
