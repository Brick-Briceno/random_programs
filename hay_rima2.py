import pyphen
def separar_silabas(word):
    dic = pyphen.Pyphen(lang="en")
    syllables = dic.inserted(word).split('-')
    return syllables

palabra = "So it's gonna be forever"

#Ejemplo de uso
print(separar_silabas(palabra), len(separar_silabas(palabra)))

"""
Nice to meet you, where you been?
I could show you incredible things
Magic, madness, heaven, sin
Saw you there and I thought
"Oh, my God, look at that face
You look like my next mistake
Love's a game, wanna play?" Ay
New money, suit and tie
I can read you like a magazine
Ain't it funny? Rumors fly
And I know you heard about me
So hey, let's be friends
I'm dying to see how this one ends
Grab your passport and my hand
I can make the bad guys good for a weekend
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless
We'll take this way too far
It'll leave you breathless, mm
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
Cherry lips, crystal skies
I could show you incredible things
Stolen kisses, pretty lies
You're the King, baby, I'm your Queen
Find out what you want
Be that girl for a month
Wait, the worst is yet to come, oh, no
Screaming, crying, perfect storms
I can make all the tables turn
Rose garden filled with thorns
Keep you second guessing like
"Oh, my God, who is she?"
I get drunk on jealousy
But you'll come back each time you leave
'Cause, darling, I'm a nightmare dressed like a daydream
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless (oh)
We'll take this way too far
It'll leave you breathless, mm (oh)
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane (insane)
But I've got a blank space, baby
And I'll write your name
Boys only want love if it's torture
Don't say I didn't, say I didn't warn ya
Boys only want love if it's torture
Don't say I didn't, say I didn't warn ya
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over (over)
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane (I'm insane)
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless
We'll take this way too far (ooh)
It'll leave you breathless, mm
Or with a nasty scar (leave a nasty scar)
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
"""
