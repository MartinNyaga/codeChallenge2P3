from Review import Review
class Customer:
    all_of_them = []
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all_of_them.append(self)

    @property
    def given_name(self):
        return (self._first_name)
    
    @property
    def family_name(self):
        return (self._last_name)
    
    @family_name.setter
    def family_name(self, value):
        self._last_name = value

    def full_name(self):
        return(f'{self._first_name} {self._last_name}')
    
    @classmethod
    def all(cls):
        return (cls.all_of_them)
    
    def restaurants(self):
        return({review for review in Review.all if review.customer.full_name == self.full_name})
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.review.append(review)
        restaurant.add_review(review)

    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_of_them:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        customers = []
        for customer in cls.all_of_them:
            if customer.given_name == name:
                customers.append(customer)
        return customers