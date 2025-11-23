# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class Car:
# Constructor (Initialization) - __init__ method
    def __init__(self, make, model):
        self.make = make  # Encapsulation: Attribute 'make' is encapsulated within the class.
        self.model = model


# Method - start_engine
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")


# Creating instances (objects) of the Car class

# Inheritance: Car is a class that can be used to create objects (instances).
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(f"I have a {car1.make} {car1.model}.")  # Accessing attributes
print(f"I have a {car2.make} {car2.model}.")  # Accessing attributes
# Abstraction: We create objects without worrying about the internal details of the Car class.

# Creating the first car (object)
car1.start_engine()
# Creating the second car (object)
car2.start_engine()


# Accessing object attributes

# Encapsulation: Accessing object attributes (make and model) using dot notation.


# Calling object methods

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).


# Method Call - start_engine

# Git push 403 helper: concise commands to fix "permission denied / 403" errors.
GIT_PUSH_403_HELP = """\
1) Check current remotes:
   git remote -v

2) If you don't have write access, fork the repo on GitHub then:
   git remote set-url origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main

3) HTTPS (use PAT instead of password):
   # create a PAT with 'repo' scope, then:
   git remote set-url origin https://<your-username>:<PAT>@github.com/<your-username>/<repo-name>.git

4) Preferred: SSH
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # add ~/.ssh/id_ed25519.pub to GitHub > Settings > SSH and GPG keys
   git remote set-url origin git@github.com:<your-username>/<repo-name>.git
   git push -u origin main

5) If contributing to upstream: push to your fork and open a Pull Request against the original repo.
Replace <your-username>, <repo-name>, and <PAT> accordingly.
"""

def print_git_push_help():
    """Prints concise steps and exact commands to resolve git push 403 errors."""
    print(GIT_PUSH_403_HELP)

# Optional: call print_git_push_help() when running this file directly.
# if __name__ == "__main__":
#     print_git_push_help()
