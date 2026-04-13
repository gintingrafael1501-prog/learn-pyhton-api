import requests as res

while input('Do You want a joke : ').lower()== 'y':
    req = res.get('https://official-joke-api.appspot.com/random_joke')
    respond = req.json()
    if 'setup' in respond:
        joke = respond['setup']
        print(joke)

        var = input('Click Enter fo Punchline : ')
        punchline = respond['punchline']
        print(punchline)
