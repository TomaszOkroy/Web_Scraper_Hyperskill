# the list "walks" is already defined
# your code here

distance = 0
for walk in walks:
    distance += walk["distance"]


print(distance // len(walks))