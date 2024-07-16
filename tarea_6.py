def is_eligible_purchase(age, items_purchased):

  return age > 18 and items_purchased > 1

age = int(input("tu edad: "))
items_purchased = int(input("cosas compradas: "))

eligible = is_eligible_purchase(age, items_purchased)
print(eligible)