# Rated Places (Django | Postgresql)

## Description 

  When you travel to a new city, it takes time till you find your new favorite place or visit what's best here. You will want to visit the best places there are, but it is so difficult to find them. The most reviewed and top rated places are ones that you can trust. But take everything with a grain of salt.Enter the city name and see the the best reviewed places on Google Maps. You may also wish to view the most reviewed or worst reviewed on Google Maps in the world.

[Clone Project From here!](https://github.com/Spidy-crypto/Rated-places.git)

## Configure your api Apis

* Places APi 
* Geocoding API

### Make key.py file with manage.py and put below code snippet in it.

```
def getkey():
    return "Here is your api key"
```

### Change database credential in settings.py 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spidy',
        'USER' : 'postgres',
        'PASSWORD': '1234',
        'HOST' : 'localhost'
    }
}
```
