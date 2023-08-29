from Review import Review
class Restaurant:
    RESTAURANTS = []
    def __init__(self, name=""):
        self.name = name

    @classmethod
    def name(self):
        return(self._name)
    
    @classmethod
    def all(cls):
        return(cls.RESTAURANTS)
    
    def reviews(self):
        return [review for review in Review.all if review.restaurant.name == self._name]
    
    def customers(self):
        return list({review.customer for review in Review.all if review.restaurant.name == self._name})
    
    def average_star_rating(self):
        sum = 0
        for item in Review.all:
            sum = sum(item.rating)
        average = sum / len(Review.all)
        return average