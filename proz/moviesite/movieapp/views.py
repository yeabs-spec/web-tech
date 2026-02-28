from django.shortcuts import render

movies_list = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "genres": ["Sci-Fi", "Action"],
        "rating": 8.8,
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "duration_min": 148
    },
    {
        "id": 2,
        "title": "The Matrix",
        "year": 1999,
        "genres": ["Sci-Fi", "Action"],
        "rating": 8.7,
        "director": "Lana Wachowski, Lilly Wachowski",
        "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "duration_min": 136
    },
    {
        "id": 3,
        "title": "Interstellar",
        "year": 2014,
        "genres": ["Sci-Fi", "Adventure", "Drama"],
        "rating": 8.6,
        "director": "Christopher Nolan",
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "duration_min": 169
    },
    {
        "id": 4,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama"],
        "rating": 9.3,
        "director": "Frank Darabont",
        "cast": ["Tim Robbins", "Morgan Freeman"],
        "duration_min": 142
    },
    {
        "id": 5,
        "title": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "genres": ["Animation", "Action", "Adventure"],
        "rating": 8.4,
        "director": "Peter Ramsey, Rodney Rothman, Bob Persichetti",
        "cast": ["Shameik Moore", "Jake Johnson", "Hailee Steinfeld"],
        "duration_min": 117
    }
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movies_view(request):
    return render(request, 'movies.html', {'list': movies_list})

