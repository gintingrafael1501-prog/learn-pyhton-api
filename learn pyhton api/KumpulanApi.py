import  requests as est

while True:
    print('\n=== Menu ===')
    print('1. Joke')
    print('2. Quote')
    print('3. Fakta Kucing')
    print('4. Fakta Random')
    print('5. Gambar Anjing Random')
    print('6. Keluar')

    pilih = input('Pilih : ')

    if pilih == '1':
        req = est.get('https://official-joke-api.appspot.com/random_joke')
        data = req.json()

        print('\nJoke : ')
        print(data['setup'])
        input('Enter the line....')
        print(data['punchline'])
        
    elif pilih == '2':
        req = est.get('https://zenquotes.io/api/random')
        data = req.json()

        print('\n QOUTE : ')
        print(data[0]['q'])
        print('- '+ data[0]['a'])

    elif pilih == '3':
        print(3)
    
    elif pilih == '4':
        print(4)

    elif pilih == '5':
        print(5)

    elif pilih == '6':
        print('Terimakasih Sudah Bermain')
        break

    else:
        print('Pilihan tidak ada')