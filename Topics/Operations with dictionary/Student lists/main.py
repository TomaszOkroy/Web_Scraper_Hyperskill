import operator
# student_list = {
#     "English": ['Tim', 'Carl', 'Dean', 'Jane'],
#     "Maths": ['Jane', 'Mike', 'Ann', 'Kate', 'Nick', 'Jenny'],
#     "Chemistry": ['Tim', 'Carl', 'Dean']
# }
# write your code here
student_popular = {key: len(value) for key, value in student_list.items()}
print(max(student_popular, key=student_popular.get))