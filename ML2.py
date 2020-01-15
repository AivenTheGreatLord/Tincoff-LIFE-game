import random as rd

def area_counter(world, i, j, sign):
    fish_counter = 0
    if world[i-1][j-1] == sign:
        fish_counter += 1
    if world[i-1][j] == sign:
        fish_counter += 1
    if world[i-1][j+1] == sign:
        fish_counter += 1
    if world[i][j-1] == sign:
        fish_counter += 1
    if world[i][j+1] == sign:
        fish_counter += 1
    if world[i+1][j-1] == sign:
        fish_counter += 1
    if world[i+1][j] == sign:
        fish_counter += 1
    if world[i+1][j+1] == sign:
        fish_counter += 1
    return fish_counter

def next_era(world): 
    new_world = [["//" for i in range(18)] for j in range(18)] #насколько я понимаю, все клетки эвалюционируют одновременно, то есть нужно создавать новый список
    for i in range(1,17):
        for j in range(1,17):
            if world[i][j] == "->":
                fish_count = area_counter(world, i, j, "->")
                if fish_count <= 1 or fish_count >=4:
                    new_world[i][j] = ".."
                else:
                    new_world[i][j] = "->"

            elif world[i][j] == ";":
                fish_count = area_counter(world, i, j, ";") 
                if fish_count == 1 or fish_count >=4:
                    new_world[i][j] = ".."
                else:
                    new_world[i][j] = ";"

            elif world[i][j] == "..":
                fish_count = area_counter(world, i, j, ";")
                if fish_count == 3:
                    new_world[i][j] = ";"
                else:
                    new_world[i][j] = ".."
                
                fish_count = area_counter(world, i, j, "->")
                if fish_count == 3:
                    new_world[i][j] = "->"

            elif world[i][j] == "O":
                new_world[i][j] = "O"

            else:
                new_world[i][j] = "//"
    return new_world
                

def clear():
    border = ["//" for i in range(18)]
    world = [border] + [ ( ["//"]  +  [".." for i in range(16)]  +  ["//"] ) for j in range(16)] + [border]
    return world

def fill(world):
    material = ["O","->","->", ";",";"]
    for i in range(1,17):
        for j in range(1,17):
            world[i][j] = material[rd.randint(0,4)]
    return world

def create(world):
    print("Введите кооманду создания?")
    print("Например: -> 3 3 означает, что мы размещаем рыбу на клетке три три (начало отсчета из верхнего левого угла, измерение начинается с еденицы)")
    command = input()
    try:
        command = command.split()
        world[int(command[1])][int(command[2])] = command[0]
        if world[int(command[1])][int(command[2])] not in ["->",";","..","O"]:
               command = 1/0
    except BaseException:
        print("Вы ввели некорректную команду!") 
    return world

def visualization(world):
    for i in range(len(world)):
        print(*[str(world[i][j]).rjust(3) for j in range(len(world[i]))])


print('''Привет! Это моя реализация игры "Жизнь" от Тинкофф Банка.''')
print("Поле представляет собой карту 16x16 клеток. Условные обозначения: O - скала, -> - рыба, ; - креветка, // - граница карты")
print("Управление следующее:")
print("fill - заполнить поле случайными объектами (старые стираются)")
print("next - один ход эволюции")
print("create - создать один из объектов: скалу (O), рыбу(->), креветку(;) и пустоту(..)")
print("clear - очистить поле")
print('''EXIT - выйти''')
print("Нажмите Enter чтообы продолжить")
command = input()

world = clear()

while True:
    visualization(world)
    print("Введите комманду:")
    command = input()
    if command == "EXIT":
        break
    elif command == "fill":
        world = fill(world)
    elif command == "clear":
        world = clear()
    elif command == "next":
        world = next_era(world)
    elif command == "create":
        world = create(world)
    else:
        print("Вы ввели некорректную команду!")
         