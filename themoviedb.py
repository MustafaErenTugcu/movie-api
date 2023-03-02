import requests

class Movie():
    def __init__(self):
        self.url = "https://api.themoviedb.org/3/"
        self.api_key = "8f9ddcd2a729165000994178b759b43b" 
       

    def getPopularMovie(self):
        response = requests.get(f"{self.url}movie/popular?api_key={self.api_key}&language=en-US&page=1 ")
        return response.json()

    def getmoviesTheaters(self):
        response = requests.get(f"{self.url}movie/now_playing?api_key={self.api_key}&language=en-US&page=1 ")
        return response.json()





movie = Movie()

while True : 
    
    choice = input('1- Get Popular Movies Lists\n2- Get Movies in Theaters\n3- Exit\nYour Choice : ')
    if choice == "3":
        break
    else : 
        if choice == "1":
            result = movie.getPopularMovie()
            print("Popular Movies".center(50,"*"))
            for movie in result["results"]:
                print(movie["original_title"])
        
        elif choice == "2":
           movies = movie.getmoviesTheaters()
           print("Movies In Theaters".center(50,"*")) 
           for movie in movies["results"]:
               print(movie["original_title"])
        
        else : 
            print("Entered wrong value")











