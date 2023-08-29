class Review:
    REVIEWS = []
    def __init__(self, customer, restaurant, rating = 0):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    
    def rating(self):
        return(self._rating)
    
    @classmethod
    def all(cls):
        return (cls.REVIEWS)
    
    def customer(self):
        return(self._customer)
        
    def restaurant(self):
        return(self._restaurant)