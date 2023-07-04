my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"


def problem1():
    class p1:
        def __init__(self,x):
          self.sayi=x
          if type( self.sayi) != int :
            self.sayi=0
        def get_value(self):
          return self.sayi
        def set_value(self,x):
          if type(x) == int:
            self.sayi=x
          else :
            None
    return p1

def problem2():
  class p1:
    def __init__(self, x , y):
      self.x=x
      self.y=y
    def get_area(self):
      return self.x*self.y
    def get_perimeter(self):
      return self.x*2 + self.y*2
  return p1


def problem3():
  class Grades:
    def __init__(self):
      self.grades=[]
    def add_grade(self, x):
      self.grades.append(x)
    def remove_grade(self, x):
       if x in self.grades: 
        self.grades.remove(x)  
    def get_min(self):
       y = sorted(self.grades)  
       if len(y)>0:           
          return y[0]
       else :
          return 0.0
    def get_max(self):
      y = sorted(self.grades)  
      if len(y)>0:          
        return y[len(y)-1]
      else :
          return 0.0
    def get_mean(self):
       y = sorted(self.grades)
       if len(y)>0:            
         s=0
         for i in self.grades : 
             s += i
         return s/len(y)
       else :
          return 0.0
    def get_median(self):
      y = sorted(self.grades)
      if len(y)== 0 :
          return 0.0
      if (len(y) % 2) != 0:
          return y[(int(len(y)/2))]
      if (len(y) % 2) == 0:
          return (y[int((len(y)/2))-1]+y[int((len(y)/2))])/2

  return Grades


def problem4():
  class Movie:
    def __init__(self):
      self.movie_name = ""
      self.director = ""
      self.year = ""
      self.rating=0.0
      self.length=0.0
    def set_rating(self , x):
      self.rating=x
    def set_length(self , x):
      self.length=x
    def get_rating(self):
      return self.rating
    def get_movie_name(self):
      return self.movie_name
    def get_director(self):
      return self.director
    def get_year(self):
      return self.year
    def get_length(self):
      return self.length
  
  return Movie




class Movie:
    def __init__(self, movie_name="", director="", year="", rating=0.0, length=0.0):
        self.movie_name = movie_name
        self.director = director
        self.year = year
        self.rating = rating
        self.length = length

    def set_rating(self, rating):
        self.rating = rating

    def set_length(self, length):
        self.length = length

    def set_name(self, movie_name):
        self.movie_name = movie_name

    def set_director(self, director):
        self.director = director

    def set_year(self, year):
        self.year = year

    def get_rating(self):
        return self.rating

    def get_movie_name(self):
        return self.movie_name

    def get_director(self):
        return self.director

    def get_year(self):
        return self.year

    def get_length(self):
        return self.length


class MovieCatalog:
    def __init__(self):
        self.movies = []
       

    def add_movie(self, movie_name, director, year, rating=0.0, length=0):
        for movie in self.movies:
            if movie.get_movie_name() == movie_name and movie.get_director() == director and movie.get_year() == year:
                return
        movie = Movie(movie_name, director, year, rating, length)
        self.movies.append(movie)

    def remove_movie(self, movie_name):
        for movie in self.movies:
            if movie.get_movie_name() == movie_name:
                self.movies.remove(movie)

    def get_oldest(self):
        oldest_movie = min(self.movies, key=lambda x: x.get_year())
        return oldest_movie.get_movie_name()

    def get_lowest_ranking(self):
        lowest_ranked_movie = min(self.movies, key=lambda x: x.get_rating())
        return lowest_ranked_movie.get_movie_name()

    def get_highest_ranking(self):
        highest_ranked_movie = max(self.movies, key=lambda x: x.get_rating())
        return highest_ranked_movie.get_movie_name()

    def get_by_director(self, director):
        movies_by_director = [movie for movie in self.movies if movie.get_director() == director]
        return [movie.get_movie_name() for movie in movies_by_director]

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        