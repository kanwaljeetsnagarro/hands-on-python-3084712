greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {} and {}"

formatted = greet_format.format("TestUser", "AnotherUser")  + " " + intrupution

print(intrupution.lower(), formatted.upper())
print(formatted.replace("Hello", "Hi"))
print(formatted)
