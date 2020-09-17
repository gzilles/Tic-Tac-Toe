# Variables
counter = 0
counterX = 0
counterO = 0
choose = 0
flag = 0
result = "new"
Numbers = ["1", "2", "3"]
Pieces = ["X", "O"]
Moves = []
Field = []
Input = "_________"
# Get field input
# while flag == 0:
#     Input = str(input("Enter cells: "))
#     if Input != "" and len(Input) >= 7:
#         flag = 1
# flag = 0
# Create field
for i in Input:
    Field.append(i)
# Print input
#    print(Input)
# Print field
while flag == 0:
    print("---------")
    print("|", Field[0], Field[1], Field[2], "|")
    print("|", Field[3], Field[4], Field[5], "|")
    print("|", Field[6], Field[7], Field[8], "|")
    print("---------")
# Ask to enter the coordinates and analyze user input
    while flag == 0:
        choose = choose % 2
        x = 0
        y = 0
        coord = str(input("Enter the coordinates: "))
        coord = coord.strip()
        if len(coord) != 3 or coord == "" or coord[0] >= "a" or coord[1] >= "a" or coord[2] >= "a":
            print("You should enter numbers!")
        elif 1 <= int(coord[0]) <= 3 and coord[1] == " " and 1 <= int(coord[2]) <= 3:
            # if int(coord) > 3 or int(coord) < 1000:
            Moves = coord.split()
            x = int(Moves[0])
            y = int(Moves[1])
            flag = 1
        else:
            print("Coordinates should be from 1 to 3!")
        if x == 1 and y == 1:
            if Field[6] == "_":
                Field[6] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 1 and y == 2:
            if Field[3] == "_":
                Field[3] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 1 and y == 3:
            if Field[0] == "_":
                Field[0] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 2 and y == 1:
            if Field[7] == "_":
                Field[7] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 2 and y == 2:
            if Field[4] == "_":
                Field[4] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 2 and y == 3:
            if Field[1] == "_":
                Field[1] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 3 and y == 1:
            if Field[8] == "_":
                Field[8] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 3 and y == 2:
            if Field[5] == "_":
                Field[5] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
        if x == 3 and y == 3:
            if Field[2] == "_":
                Field[2] = Pieces[choose]
                flag = 1
                Input = ""
                for i in range(len(Field)):
                    Input += Field[i]
            else:
                flag = 0
                print("This cell is occupied! Choose another one!")
    choose += 1
# Print input
#     print(Input)
# Count1 X's and O's in field
    counterX = 0
    counterO = 0
    for char in Input:
        if char == "X":
            counterX += 1
        elif char == "O":
            counterO += 1
# Determine victory in line
    for i in range(0, 7, 3):
        if Input[i] == Input[i + 1] and Input[i + 1] == Input[i + 2]:
            if Input[i] == "X":
                counter += 1
            if Input[i] == "O":
                counter += 2
# Determine victory in column
    for i in range(0, 3):
        if Input[i] == Input[i + 3] and Input[i + 3] == Input[i + 6]:
            if Input[i] == "X":
                counter += 1
            if Input[i] == "O":
                counter += 2
# Determine victory in diagonal
    if Input[0] == Input[4] and Input[4] == Input[8]:
        if Input[0] == "X":
            counter += 1
        if Input[0] == "O":
            counter += 2
    elif Input[2] == Input[4] and Input[4] == Input[6]:
        if Input[2] == "X":
            counter += 1
        if Input[2] == "O":
            counter += 2
# Impossible
    if counterX - counterO >= 2 or counterO - counterX >= 2 or counter >= 3:
        result = "Impossible"
        flag = 1
# X wins
    elif counter == 1:
        result = "X wins"
        flag = 1
# 0 wins
    elif counter == 2:
        result = "O wins"
        flag = 1
# Game not finished
    elif "_" in Input:
        result = "Game not finished"
        flag = 0
# Draw
    else:
        result = "Draw"
        flag = 1
# Print Result
else:
    print("---------")
    print("|", Field[0], Field[1], Field[2], "|")
    print("|", Field[3], Field[4], Field[5], "|")
    print("|", Field[6], Field[7], Field[8], "|")
    print("---------")
    print(result)
