songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

good_songs = {(song[0], song[1]) for song in songs if song[0] != 'Nickelback'}

print(good_songs)