animal = "horse"
item = "fence"
#
print("The {:10} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item))
# print("The {1} jumped over the {1}".format(animal, item))
# print("The {0} jumped over the {0}".format(animal, item))
# print("The {animal} jumped over the {item}".format(animal="horse", item="fence"))

text = "The {:^10} jumped over the {}"
#
print(text.format(animal, item))
#


