class User():
    def __init__(self, first_name, last_name, age, location, bg):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.loc = location
        self.blood_group = bg
        self.login_attempts = 0

    def describe_user(self):
        return f"User Profile:\nName: {self.first_name} {self.last_name}\nAge : {self.age}\nLocation : {self.loc}\nBlood Group : {self.blood_group} "

    def greet_user(self):
        return f"Hello, {self.first_name} {self.last_name}. How are you?"

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Parth", "Khadke", "21", "Amravati", "AB+")

print(user_1.describe_user())

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)