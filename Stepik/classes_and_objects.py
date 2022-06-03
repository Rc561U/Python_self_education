class TravelBlog:
    total_blogs = 0

    @classmethod
    def count_blog(cls):
        cls.total_blogs += 1

    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.count_blog()

tb1 = TravelBlog('France', 6)
tb2 = TravelBlog('Italy', 5)
print(TravelBlog.total_blogs)