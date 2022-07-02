my_set = {"Jan", "Feb", "Mar"}
for element in my_set:
    print(element)

my_set.add("Apr")
print(my_set)
my_set.remove("Jan")
print(my_set)

my_list = ["Jan", "Feb", "Mar", "Feb"]
my_list.remove("Feb")
print(my_list)