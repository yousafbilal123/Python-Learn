class User:
    def __init__(self, id=None, name=None, age=None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age})"
