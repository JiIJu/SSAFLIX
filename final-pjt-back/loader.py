import json

with open('manymovies.json','r') as f:
    movies = json.load(f)

print(movies)
new_list = []

for movie in movies:
    new_data = {'model' : 'movies.movie'}
    new_data['fields'] = movie
    new_list.append(new_data)

with open('manymovies.json','w',encoding='UTF-8') as f:
    json.dump(new_list,f,ensure_ascii=False,indent=2)