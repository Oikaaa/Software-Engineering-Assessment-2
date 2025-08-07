fruit_basket = {'apple', 'banana', 'cherry'}
fruit_basket.add('watermelon')
fruit_basket.update({'green_apple', 'hello'})

lunch = {'pho', 'rau', 'hello'}
dinner = {'mi', 'pho'}
#Whole shit
meals = lunch.union(dinner) # U for union oc
meals = lunch | dinner
#Same shit
same_meals = lunch.intersection(dinner)
same_meals = lunch & dinner
#Toji
diff_meals = lunch.difference(dinner)
diff_meals = lunch - dinner

#Find the whole thing except same
anything_except_same = lunch.union(dinner) - lunch.intersection(dinner)
print(anything_except_same)