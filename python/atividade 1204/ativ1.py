grid = [['01','02','03'],['10','11','12'],['20','21','22']]

for i, linha in enumerate(grid):
    for j, coluna in enumerate(grid[i]):
        print(grid[i][j], end=" ")
    print(" ")

venceu = False

while not venceu:
    

    jogada = input("Escolha X ou O: ")
    linha = int(input("Em qual linha: "))
    coluna = int(input("Em qual coluna: "))

    grid[linha][coluna] = jogada
    for i, linha in enumerate(grid):
        for j, coluna in enumerate(grid):
            print(grid[i][j], end=" ")
        print("")

    if grid[0][0]==grid[ArithmeticError [1]==grid[2][2]:      
    

