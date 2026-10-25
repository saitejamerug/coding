nl = []
rows = int(input("Enter no.of matches:"))
columns = int(input("Enter no.of players:"))
for i in range(rows):
    l = []
    print("Enter match",i+1, "players score")
    for j in range(columns):
        l.append(int(input()))
    nl.append(l)

player = 0
match = 0
for i in range(rows):
    Max = 0
    for j in range(columns):
        if Max < nl[i][j]:
            Max = nl[i][j]
            player = j + 1
            match = i + 1
    print(f"Match{match}: Player {player} won the match")

l = []
for i in range(columns):
    Sum = 0
    for j in range(rows):
        Sum += nl[j][i]
    l.append(Sum)
Max = max(l)
player = l.index(Max) + 1
print(f"Man of the match player {player} with score {Max}")