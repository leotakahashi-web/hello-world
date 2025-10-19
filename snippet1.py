# Writes one line to output.txt: "Hello, How do you do?"
with open("output.txt", "a", encoding="utf-8") as db:
    a = "Hello"                 # or: a = "Hello" + str(1) if you really needed the number
    b = "How do you do?"
    db.write(f"{a}, {b}\n")
