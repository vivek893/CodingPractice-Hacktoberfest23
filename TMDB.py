#Find the vote count and vote average of the movie "3 Idiots" using the TMDb API
# API LINK: "https://api.themoviedb.org//3/search/movie"
API_key="9421b1f4ffc8ce3b10736daa08f9940c"
params={'query':'3 Idiots','api_key':'API_key'}
header={'Accept': 'application/json','Authorization':'bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNzMyZmFlMGM0NjIwMTkwZDBhMTE3NzljZTkzZWZiNCIsInN1YiI6IjY0ZTc4MWIwMDZmOTg0MDEyZDcyMGQ5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HWTRgXZ33ybINQJC9FeCnEfm1Tz5GPg3F46gyBpWb-g'}
a=requests.get('https://api.themoviedb.org//3/search/movie',params=params,headers=header)
print(a.status_code)
print(a.url)
#print(a.text)
python_data=a.json()
#print(python_data)
for i in python_data['results']:
    if i['title']=='3 Idiots':
        print(i['vote_count'],int(i['vote_average']))
