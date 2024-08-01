# Making Animal Class

class Animal:
    def __init__(self):
        self.num_eyes =2

    def breathe(self):
        print("Inhale, exhale")


# Making Fish class child class of Animal

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this under underwater")

    def swim(self):
        print("Moving in water.")


#Making object from fish
nemo = Fish()
nemo.breathe()
