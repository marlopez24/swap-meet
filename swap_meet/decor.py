from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "Decor", condition = 0.0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        return f'Something to decorate your space.'