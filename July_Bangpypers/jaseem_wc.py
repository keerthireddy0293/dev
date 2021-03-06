"""
Find winners of world cup group stage 2014 from match results.
 
Input is a dictionary consisting of group results keyed by group-name
and further keyed by a string with the teams which played a match. The value
of the inner key is a tuple of the score of the match.
 
For example: If the key is 'A-B' and value is (x,y) it means team A scored
x goals and team B scored y goals.
 
Use this as input to find,
 
1. The top 2 teams per group and their points.
 
The rules are:
 
1. Each win - 3 points
2. Each draw - 1 point.
3. Loss - 0 point.
4. If two teams has same number of points, the winner is the one
who has a better goal difference (GD), where,
 
GD = GF (goals for) - GR (goals received)
 
This is an open problem.
 
"""
 
results = {'A': {'brazil-croatia': (3, 1),
                 'brazil-mexico': (0,0),
                 'cameroon-brazil': (1,4),
                 'croatia-mexico': (1,3),
                 'cameroon-croatia': (0,4),
                 'mexico-cameroon': (1,0)},
 
           'B': {'holland-spain': (5,1),
                 'holland-australia': (3,2),
                 'holland-chile': (2,0),
                 'chile-australia': (3,1),
                 'chile-spain': (2,0),
                 'spain-australia': (3,0)},
 
           'C': {'colombia-greece': (3,0),
                 'colombia-ivorycoast': (2,1),
                 'colombia-japan': (4,1),
                 'greece-japan': (0,0),
                 'greece-ivorycoast': (2,1),
                 'ivorycoast-japan': (2,1)},
 
           'D': {'costarica-uruguay': (3,1),
                 'costarica-italy': (1,0),
                 'costarica-england': (0,0),
                 'uruguay-england': (2,0),
                 'uruguay-italy': (1,0),
                 'italy-england': (2,1)},
 
           'E': {'france-switzerland': (5,2),
                 'france-honduras': (3,0),
                 'france-ecuador': (0,0),
                 'switzerland-ecuador': (2,1),
                 'switzerland-honduras': (3,0),
                 'ecuador-honduras': (2,1)},
 
           'F': {'argentina-nigeria': (3,2),
                 'argentina-iran': (1,0),
                 'argentina-bosnia': (2,1),
                 'iran-bosnia': (1,3),
                 'iran-nigeria': (0,0),
                 'nigeria-bosnia': (1,0)},
 
           'G': {'germany-portugal': (4,0),
                 'germany-ghana': (2,2),
                 'germany-usa': (1,0),
                 'usa-ghana': (2,1),
                 'usa-portugal': (2,2),
                 'portugal-ghana': (2,1)},
 
           'H': {'belgium-algeria': (2,1),
                 'belgium-russia': (1,0),
                 'belgium-korea': (1,0),
                 'algeria-korea': (4,2),
                 'algeria-russia': (1,1),
                 'russia-korea': (1,1)}}

from collections import defaultdict
 
def val_of_team(group):
    """Return a dict of team's performance metrics.
 
    Sample:
    {
        'brazil': (points, scored - recived)
    }
    """
 
    cache = defaultdict(lambda : tuple([0,0]))
 
    for match, score in group.iteritems():
        t1, t2 = match.split('-')
 
        points, diff = cache[t1]
        result = score[0] - score[1]
        point = 3 if result > 0 else 1 if result == 0 else 0
        cache[t1] = (points + point, diff  + result)
 
        points, diff = cache[t2]
        result = score[1] - score[0]
        point = 3 if result > 0 else 1 if result == 0 else 0
        cache[t2] = (points + point, diff  + result)
 
    return dict(cache)
 
def two_winners(group):
    """Return an array of names of top 2 winners."""
 
    # Sample: [((7, 5), 'brazil'), ((7, 3), 'mexico') .. ]
    vals = sorted([(val, key) for key, val in group.iteritems()], reverse=True)
    return [i[1] for i in vals[0:2]]
 
for n, group in results.iteritems():
    print n , two_winners(val_of_team( group))