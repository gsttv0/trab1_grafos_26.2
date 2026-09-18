class Aresta:

    def __init__(self, id, orig, dest, val):
        self.id = id
        self.orig = orig
        self.dest = dest
        self.val = val

    def __str__(self):
        return (
            f"{self.id}: "
            f"{self.orig} -> {self.dest} "
            f"(peso={self.val})"
        )