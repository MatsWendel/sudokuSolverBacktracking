#Abgewandelt von: https://www.geeksforgeeks.org/sudoku-backtracking-7/


import sys
from prettytable import PrettyTable

#ausgabe der Matrix auf die Konsole
def printMatrix(_matrix):
    p = PrettyTable()
    for row in _matrix:
        p.add_row(row)

    print(p.get_string(header=False, border=True))

#Funktion zum Finden der naechsten leeren Stelle im Sudoku
def findNextEmpty(_matrix, position):
    for x in range(9):
        for y in range(9):
            if (_matrix[x][y] == 0):
                position[0] = x
                position[1] = y
                return True
    return False

#Funktion, die kontrolliert, ob die uebergebene Zahl bereits in der Spalte vorkommt.
def isInRow(_matrix, _row, _value):
    for x in range(9):
        if (_matrix[_row][x] == _value):
            return True
    return False

#funktion, die kontrolliert, ob die uebergebene Zahl bereits in der Zeile vorkommt.
def isInColumn( _matrix, _col, _value):
    for x in range(9):
        if (_matrix[x][_col] == _value):
            return True
    return False

#funktion, die kontrolliert, ob die uebergebene Zahl bereits in der Box vorkommt.

def isInBox(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False
#funktion, die kontrolliert, ob die uebergebene Zahl valide fuer das aktuelle Fald ist,
#das Heisst, ob die Zahl in der Spalte, in der Zeile und in der Box noch nicht vorkommt.

def isValid(num, arr, col, row):
    return not isInRow(arr, row, num) and not isInColumn(arr, col, num) and not isInBox(arr, row - row % 3,
                                                                                                 col - col % 3, num)


#Funktion zum loesen des Sudokus.
def solve(_matrix):
    #Definieren einer Liste zum uebertragen der aktuellen leeren Stelle.
    position = [0, 0]


    #Aufruf der Funktion zum finden der naechsten leeren Stelle.(Wenn sie false zurueck gibt ist das Sudoku geloest.)
    if not findNextEmpty(_matrix, position):
        return True

    row = position[0]
    col = position[1]
    #Eine Schleife mit 9 durchlaeufen, fuer jede moegliche Zahl einer.
    for x in range(1, 10):
        #gucken, ob die Zahl valide fuer das Feld ist. Wenn ja:
        if isValid(x, _matrix, col, row):
            #Zahl vorlaeufig in das Array einsetzen und diese Funktion rekursiv fuer das neue Array aufrufen.
            print(str(x) + ' =>' + str(col) + ' : ' + str(row))
            _matrix[row][col] = x
            if (solve(_matrix)):
                # wenn true zurueck kommt ist das Sudoku geloest.
                return True
            #wenn false zurueck kommt:
            #wieder auf 0 setzen und die naechste Zahl aus der For schleife einsetzen.
            _matrix[row][col] = 0
    #return false (loest das Backtracking beim rekursiven Aufruf aus.)
    return False

#Main

if __name__ == "__main__":
    sudoku = [[0 for x in range(9)] for y in range(9)]
        #erstellen des Sudokus
    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    #Wenn die funktion zum loesen des Sudokus True Zurueck gibt
    printMatrix(sudoku)
    if solve(sudoku):
        printMatrix(sudoku)
    else:
        print("keine Lösung")



