import requests as que

# tipe data list
keranjang_buah = ['mangga','apel','nanas']
print(keranjang_buah[1])
# tipe data dictionary
murid_codero = {
    'nama': 'Rafael',
    'kelas': '6',
    'umur': '12',
    'hobi': 'main game'
}
print(murid_codero['nama'])
print(murid_codero['hobi'])


# Buatlah 3 tipe data dictinary yaitu teman sekolah, game, film
teman_sekolah = {
    'nama':'Juvent',
    'kelas': '6',
    'umur': '12',
    'hobi': 'main pokemon go',
    'jenis kelamin': 'Laki-laki'
} 

game = {
    'genre': 'MOBA',
    'rating': '4,5',
    'nama game': 'Mobile Legend'
}

film ={
    'nama film': 'Avenger',
    'rating': '4,9',
    'genre': 'sci-fi',
    'pemeran utama': 'captain america'
}
print('Teman sekolah : ')
print(teman_sekolah['nama'])
print(teman_sekolah['hobi'])
print('Game : ')
print(game['nama game'])
print(game['genre'])
print('Film : ')
print(film['nama film'])
print(film['genre'])