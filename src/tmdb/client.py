import requests

url = "https://api.themoviedb.org/3/search/movie?query=Barbie&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZWFmMTlmY2JmNjY3OTBjYjgxYWQzYzRjNTdjOWFjOCIsIm5iZiI6MTc2NzI0MzI3NS4wNTc5OTk4LCJzdWIiOiI2OTU1ZmUwYjEzODliNTM1YmE3YzZiYmQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.KCrIVpeus8Xwm48-2T9W_5abpUuuBWZxNRNWiCu-OR4"
}

response = requests.get(url, headers=headers)

print(response.text)


def search_movie(query:str, page:int=1, raw=False):
    url=f"https://api.themoviedb.org/3/search/movie"
    params={
        "query":query,
        "page":page,
        "include_adult":False,
        "language":"en-US"
    }
    response=requests.get(url,headers=headers,params=params)
    if raw:
        return response
    return response.json()

def movie_detail(movie_id:int , raw=False):
    url="https://api.themoviedb.org/3/movie/{movie_id}"
    params={
        "include_adult":False,
        "language":"en-US"
    }
    response=requests.get(url,headers=headers,params=params)
    if raw:
        return response
    return response.json()