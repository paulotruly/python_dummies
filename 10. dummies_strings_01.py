MyString = "Hello world!"
print(MyString[0])

String1 = "Hello world!"
String2 = "Python is fun!"

print(String1[0])
print(String1[0:5])
print(String1[:5])
print(String1[6:])

String3 = String1[:6] + String2[:6]
print(String3 + "!")

print(String2[:7]*5)

String4 = "   Hello world!   "

print(String4.upper())
print(String4.strip())
print(String4.center(21, " "))
print(String4.strip().center(21, " "))
print(String4.isdigit())
print(String4.istitle())
print(max(String4))
print(String4.split())
print(String4.split()[0])

SearchMe = "The apple is red and the berry is blue"
print(SearchMe.find("is"))
print(SearchMe.rfind("is"))
print(SearchMe.count("is"))
print(SearchMe.startswith("The"))
print(SearchMe.endswith("The"))
print(SearchMe.replace("apple","car"))

Formatted = "{:d}"
print(Formatted.format(7000))
Formatted = "{:,d}"
print(Formatted.format(7000))
Formatted = "{:^15,d}"
print(Formatted.format(7000))
Formatted = "{:-^15,d}"
print(Formatted.format(7000))
Formatted = "{:-^15.2f}"
print(Formatted.format(7000))
Formatted = "{:*>15X}"
print(Formatted.format(7000))
Formatted = "{:*<#15x}"
print(Formatted.format(7000))
Formatted = "A {0} {1} and a {0} {2}"
print(Formatted.format("blue", "car", "truck"))
