# Fantasy_Music
This is a passion project I will work on, likely during the winter season December 2026-February 2027.
The goal is to make a version of fantasy football, but based around music instead.
This will mainly work with the billboard and polars python libraries.
The current rough sketch I have starts with get_artists.py, which is a one-time script to scrape all relevant artists to be stored somewhere. Participants will draft from this list of artists to make their teams. Once artists are drafted into teams, every week, generate_scores.py will be run and each artist will be assigned a score for the week, which are summed up to get the team scores. The structure for the remaining processes should be trivial from there.
Teams will have 2 pop artists, 2 hip hop/RnB artists, 1 country artist, 1 latin artist, 1 rock artist, 1 dance artist, 1 flex artist, and 7 bench artists.