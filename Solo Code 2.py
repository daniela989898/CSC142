import random
class Review:
    def __init__(self, rating, text):
        self.rating = rating
        self.text = text
    def pretty_print(self):
        print(f"Rating: {self.rating}/5")
        print(f"Review: {self.text}")
class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []
    def add_review(self, review):
        self.reviews.append(review)
    def average_rating(self):
        if len(self.reviews) == 0:
            return 0
        total = 0
        for review in self.reviews:
            total += review.rating
        return total / len(self.reviews)
    def display_reviews(self):
        for review in self.reviews:
            review.pretty_print()
            print()
    def best_review(self):
        max_rating = max(review.rating for review in self.reviews)
        best = [r for r in self.reviews if r.rating == max_rating]
        return random.choice(best)
    def worst_review(self):
        min_rating = min(review.rating for review in self.reviews)
        worst = [r for r in self.reviews if r.rating == min_rating]
        return random.choice(worst)
movie = Movie("El Retorno Del Jedi")
movie.add_review(Review(5, "Excelente película, la recomiendo mucho"))
movie.add_review(Review(4, "Muy buena, pero larga"))
movie.add_review(Review(1, "mala, no la recomiendo"))
movie.add_review(Review(2, "No me gustó mucho"))
movie.add_review(Review(0, "Horrible, una pérdida de tiempo"))
movie.add_review(Review(5, "Increíble, la volvería a ver"))
movie.add_review(Review(3, "Buena, pero esperaba más"))
movie.add_review(Review(4, "Entretenida y bien hecha"))
movie.add_review(Review(2, "No es mi tipo de película"))
print("Movie:", movie.title)
print("Average rating:", movie.average_rating())
print("\nAll reviews:")
movie.display_reviews()
print("Best review:")
movie.best_review().pretty_print()
print("\nWorst review:")
movie.worst_review().pretty_print()