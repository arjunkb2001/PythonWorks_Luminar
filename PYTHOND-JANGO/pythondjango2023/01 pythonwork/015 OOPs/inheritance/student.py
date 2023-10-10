
# create a function display student  and  print student name  and course


# display_student(name="ravi",course="django",rol=1000,gender="male")

def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))

display_student(name="ravi",course="django",rol=1000,gender="male")
