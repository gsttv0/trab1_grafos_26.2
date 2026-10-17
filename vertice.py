class Vertice:

    def __init__(self, id, latitude=None, longitude=None):

        self.id = id
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):

        return str(self.id)