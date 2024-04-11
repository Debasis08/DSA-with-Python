# The below code will show Error cause concatenation
# between string and int is not supported

age = 36
#txt = "My name is Debasis, I am " + age
#print(txt)  #Error



# Combine strings and numbers by using the "format()" method
txt = "My name is Debasis and I am {}"
print(txt.format(age))


# For many values
quantity = 8
item = "milk"
price = 25
myOrder = "I want total of {} packets of {} for each of {} rupees."
print(myOrder.format(quantity, item, price))

# Can be given with index nos. For example:-
myOrder = "I am willing to pay {2} rupees for total of {0} packets of {1}."
print(myOrder.format(quantity, item, price))