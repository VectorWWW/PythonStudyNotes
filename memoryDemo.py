a = 1
b = 1

# print(id(a))
# print(id(b))
print(a is b)

a = 'good'
b = 'good'
print(a is b)

a = 'very good morning'
b = 'very good morning'
print(a is b)

a = "very   good    morning"
b = 'very   good    morning'
print(a is b)

a = []
b = []
print(a is b)