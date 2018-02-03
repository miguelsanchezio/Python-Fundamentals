playlist = {
    'title': '10X Playlist',
    'author': 'Miguel',
    'songs': [
        {
            'title': 'Hustle!',
            'artist': ['Grant'],
            'duration': 2.5
        },
        {
            'title': 'Success!',
            'artist': ['John'],
            'duration': 3.1
        },
        {
            'title': 'Keys Keys!',
            'artist': ['Grant', 'DJ Khaled'],
            'duration': 2.6
        }
    ]
}

total_length = 0

for song in playlist['songs']:
    print(song['title'] + ' duration: ' + str(song['duration']))
    total_length += song['duration']

print(total_length)