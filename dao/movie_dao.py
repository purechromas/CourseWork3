from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Movie).get(pk)

    def get_all(self, page=None, status=None):
        if status:
            return self.session.query(Movie).order_by(Movie.year.desc()).paginate(per_page=12)
        elif page is not None:
            return self.session.query(Movie).paginate(per_page=12)
        else:
            return self.session.query(Movie).all()

    def create(self, movie):
        new_movie = Movie(**movie)

        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, pk):
        movie = self.get_one(pk)

        self.session.delete(movie)
        self.session.commit()
