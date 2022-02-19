from collections import defaultdict


# Function to find who covered a song
# Params: (artists: List, songs: List, artist_songs: List, target_song: String)
def who_covered(artists, songs, artist_songs, target_song):
    # Get the target song
    target = 0
    for song in songs:
        if song['name'] == target_song:
            target = song['id']

    # Return list of artists who covered a song
    returnList = []
    for pair in artist_songs:
        if pair[1] is target:
            returnList.append(artists[pair[0]]['name'])

    return returnList


# Function to find which artists share a song
# Params: (artists: List, songs: List, artist_songs: List, target_artist: String)
def shared_songs(artists, songs, artist_songs, target_artist):
    # Get the target artist
    target = 0
    for artist in artists:
        if artist['name'] == target_artist:
            target = artist['id']

    # Populate to_compare list with id = target
    comp = []
    for pair in artist_songs:
        if pair[0] is target:
            comp.append(pair[1])

    # Return list of songs shared by artist
    returnList = []
    for pair in artist_songs:
        if songs[pair[1]].get('id') in comp and songs[pair[0]].get('id') != target:
            returnList.append(songs[pair[1]].get('name'))

    return returnList


# Function find the popularity of a song by assigning a 'rank'
# Params: (songs: List, artist_songs: List)
def song_popularity(songs, artist_songs):
    # Initialize ranks dictionary
    ranks = {}

    # Iterate through songs
    for i in range(len(songs)):
        # Assign rank of song to 0
        ranks[songs[i]['name']] = 0

    # Iterate through artist_songs
    for pair in artist_songs:
        # Increment rank if pair
        ranks[songs[pair[1]].get('name')] += 1

    # Sort the ranks to have the highest at the top
    ranks = {name: count for name, count in sorted(
        ranks.items(), key=lambda item: item[1], reverse=True)}

    # Pretty print
    print('Song Name | # Of Covers  ', end='\n------------------------\n')
    for name, count in ranks.items():
        print(name, count, sep=' | ')


# Function to find artists that are similar by keywords describing their songs
# Params: (artists: List, keywords: List, target_artist: String)
def similar_artists(artists, keywords, target_artist):
    # Get id of target_artists
    target_id = next(artist['id']
                     for artist in artists if artist['name'] == target_artist)

    group = defaultdict(list)
    # Create dict of id and keywords
    for id, keyword in keywords:
        group[id].append(keyword)

    # Target is tuple containing target_id and the keyword(s) for that target_id
    target = (target_id, group[target_id])
    group.pop(target_id, None)

    # Initialize scores dictionary
    scores = {key: {key: 0} for key, _ in group.items()}

    # Iterate through target_id, keyword grouping dict
    for id, tags in group.items():
        for tag in tags:
            # If tags match
            if tag in target[1]:
                scores[id][id] += 1

    new_scores = [dic for _, dic in scores.items()]

    # Initialize new list of scores to be sorted
    newList = []
    for score in new_scores:
        newList += (score.items())

    # Sort new list of scores
    newList.sort(key=lambda item: item[1], reverse=True)

    # Pop from back of list to get the most covered songs first
    while len(newList) > 3:
        newList.pop(-1)

    # Return list of similar artists, in order of most covered songs to least covered songs
    return [artists[id]['name'] for id, _ in newList]


def main():
    artists = [
        {"id": 0, "name": "Juice WRLD"},
        {"id": 1, "name": "Drake"},
        {"id": 2, "name": "Post Malone"},
        {"id": 3, "name": "Lil Uzi"},
        {"id": 4, "name": "Lil Baby"},
        {"id": 5, "name": "Playboi Carti"},
        {"id": 6, "name": "The Kid Laroi"},
        {"id": 7, "name": "Dro Kenji"},
        {"id": 8, "name": "Iann Dior"},
        {"id": 9, "name": "NLE Choppa"},
        {"id": 10, "name": "Gunna"},
    ]
    songs = [
        {"id": 0, "name": "Picture Me Grapin'"},  # NLE
        {"id": 1, "name": "Rider"},  # Juice
        {"id": 2, "name": "Tightrope"},  # Dro
        {"id": 3, "name": "I might"},  # Iann Dior
        {"id": 4, "name": "Shoota"},  # Playboi Carti & Lil Uzi
        {"id": 5, "name": "Stay"},  # TKL
        {"id": 6, "name": "Wants and Needs"},  # Drake & Lil Baby
        {"id": 7, "name": "Hollywood's Burning"},  # Post
        {"id": 8, "name": "Commercials"},  # Lil Baby
        {"id": 9, "name": "Demon High"},  # Lil Uzi
        {"id": 10, "name": "Drip Too Hard"},  # Gunna & Juice WRLD
        {"id": 11, "name": "P Power"},  # Gunna & Drake
        {"id": 12, "name": "The Motto"},  # Drake
        {"id": 13, "name": "Magnolia"}  # Playboi Carti
    ]
    artist_songs = [
        (0, 1), (0, 10),
        (1, 6), (1, 11), (1, 12),
        (2, 7),
        (3, 4), (3, 9),
        (4, 6), (4, 8),
        (5, 4), (5, 13),
        (6, 5),
        (7, 2),
        (8, 3),
        (9, 0),
        (10, 10), (10, 11)
    ]
    keywords = [
        (0, 'sad'), (0, 'rnb'), (0, 'melodic'), (0, 'piano'),
        (1, 'hiphop'), (1, 'rap'),
        (2, 'rock'), (2, 'pop'), (2, 'guitar'), (2, 'acoustic'),
        (3, 'trap'), (3, 'fast'), (3, 'rnb'),
        (4, 'sad'), (4, 'rnb'), (4, 'melodic'), (4, 'pop'),
        (5, 'pop'), (5, 'acoustic'), (5, 'piano'),
        (6, 'sad'), (6, 'rnb'), (6, 'melodic'),
        (7, 'trap'), (7, 'piano'), (7, 'melodic'), (7, 'dark'),
        (8, 'trap'), (8, 'dark'), (8, 'melodic'),
        (9, 'trap'), (9, 'tenor'), (9, 'fast'),
        (10, 'trap'), (10, 'fast'), (10, 'rap'),
    ]

    # Should print Playboi Carti & Lil Uzi
    print(who_covered(artists, songs, artist_songs, 'Shoota'))
    print("==================================\n")

    # Should print: 'Wants and Needs' and 'P Power'
    print(shared_songs(artists, songs, artist_songs, 'Drake'))
    print("==================================\n")

    # Will print list of popular songs by rank
    song_popularity(songs, artist_songs)

    print("==================================\n")
    # Should print Lil Baby, The Kid Laroi, Dro Kenji
    print(similar_artists(artists, keywords, 'Juice WRLD'))


if __name__ == "__main__":
    main()
