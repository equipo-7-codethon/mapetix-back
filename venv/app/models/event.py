# events/model.py
class Event:
    def __init__(self, id, price, status, latitude, longitude, name, description, start_at, end_at, created_by, created_at, updated_at, score, categories, gallery):
        self.id = id
        self.price = price
        self.status = status
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.description = description
        self.start_at = start_at
        self.end_at = end_at
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at
        self.score = score
        self.categories = categories
        self.gallery = gallery
