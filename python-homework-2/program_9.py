# Safe key check

student = {
    "name": "Sumon",
    "age": 25,
    "email": "sumon@google.com"
}
email = student.get("email")
if email:
    print(email)
else:
    print("Email not found")
