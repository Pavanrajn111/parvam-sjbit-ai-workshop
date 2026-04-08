print("Hello World!")
print("Akshay Rao")

# Data types in Python
# Primitive Datatypes
name = "Akshay Rao"
age = 24
height = 160.5
is_trainer = True # is_student = True

# string
print(name, type(name))
# integer
print(age, type(age))
# float
print(height, type(height))
# boolean
print(is_trainer, type(is_trainer))

# Non Primitive Datatypes
# List - [] - Ordered, Mutable (changeable), Can have duplicate values
hobbies = ["Learning", "Gaming", "Coding", "Teaching"]

print(hobbies, type(hobbies))

# Tuple - () - Ordered, Immutable (cannot change), allow duplicate values
languages = ("Kannada", "English", "Hindi", "Tamil")

print(languages, type(languages))

# Set - {} - Unordered, Immutable, Doesn't allow duplicate values
even_numbers = {2, 8, 12, 14, 6, 20}

print(even_numbers, type(even_numbers))

# Dictionary - Key-value pairs
profile = {
    "name" : "Akshay Rao",
    "age" : 24,
    "company" : "ParvaM",
    "technologies" : ["Python", "Java", "HTML", "CSS", "JS"],
    "frameworks" : ("Laravel", "Spring", "Django", "React")
}

print(profile, type(profile))