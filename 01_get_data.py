import pandas as pd
import pylyrics3


def get_lyrics(artist):
    artist_lower = artist.lower()
    albums = pylyrics3.get_artist_lyrics(artist_lower, albums=True)

    data = []
    print('Finished downloading {}'.format(artist))
    for album_title, value in albums.items():
        for song_title in albums[album_title].keys():
            chunk = {}

            chunk['artist'] = artist
            chunk['album'] = album_title
            chunk['title'] = song_title
            chunk['lyrics'] = albums[album_title][song_title]

            # print(song_title)

            data.append(chunk)

        #     break
        # break

    return data

########### params
artists = [
    'Nightwish',
    'Delain',
    'Epica',
    'Within Temptation',
    'Lacuna Coil',
    'Amaranthe',
    'After Forever',
    'Beyond the Black',
    'Evanescence',
    'Hands Like Houses',
    'Linkin Park',
    'Myrath',
    'Paramore',
    'Powerwolf',
    'Serenity',
    'Sirenia',
    'Van Canto',
    'Visions of Atlantis',
]
###########
lyrics = []
for artist in artists:
    data = get_lyrics(artist)
    lyrics.extend(data)

df = pd.DataFrame(lyrics)
df['year'] = df.album.str.split('(').str[1].str.strip(')')
df['album'] = df.album.str.split('(').str[0].str.strip()
df.to_csv('lyrics.csv', index=False)
