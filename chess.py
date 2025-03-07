# Tип документации Google
class Board(object):
    """Класс, представляющий шахматную доску и методы для работы с ней."""

    def start_board(self):
        """Создаёт начальное состояние шахматной доски.

        Returns:
            list: Двумерный список, представляющий начальное состояние доски.
        """
        first_row = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' ']
        third_row = ['8', 'Rook', 'Night', 'Bishop', 'Queen', 'King', 'Bishop', 'Night', 'Rook', '8']
        fourth_row = ['7', 'Pawn','Pawn','Pawn','q','Pawn','Pawn','Pawn','Pawn', '7']
        fifth_row = ['6', '.', '.', '.', '.', '.', '.', '.', '.', '6']
        sixth_row = ['5', '.', '.', '.', '.', '.', '.', '.', '.', '5']
        seventh_row = ['4', '.', '.', '.', '.', '.', '.', '.', '.', '4']
        eighth_row = ['3', '.', '.', '.', '.', '.', '.', '.', '.', '3']
        nineth_row = ['2', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn', '2']
        tenth_row = ['1', 'rook', 'night', 'bishop', 'queen', 'king', 'bishop', 'night', 'rook', '1']
        start_field = [first_row, third_row, fourth_row, fifth_row, sixth_row, seventh_row, eighth_row, nineth_row, tenth_row, first_row]
        visible_field = [[i[0] for i in row] for row in start_field]
        
        return visible_field
    
    def print_board(self, field: list):
        """Выводит текущее состояние доски на экран.

        Args:
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        for row in field:
            print(*row)
    
    def point_position(self, column: str, row: int, field):
        """Возвращает фигуру, находящуюся на указанной позиции.

        Args:
            column (str): Буква столбца (A-H).
            row (int): Номер строки (1-8).
            field (list): Двумерный список, представляющий текущее состояние доски.

        Returns:
            str: Фигура, находящаяся на указанной позиции.
        """
        try:
            column = field[0].index(column.upper())
        except:
            pass
        return field[8 - int(row) + 1][column]
        
    def rewriter(self, column1: str, row1: int, column2: str, row2: int, field: list):
        """Перемещает фигуру с одной позиции на другую.

        Args:
            column1 (str): Буква столбца начальной позиции.
            row1 (int): Номер строки начальной позиции.
            column2 (str): Буква столбца конечной позиции.
            row2 (int): Номер строки конечной позиции.
            field (list): Двумерный список, представляющий текущее состояние доски.

        Returns:
            list: Обновлённое состояние доски.
        """
        fig1 = Board().point_position(column1, row1, field)
        column1 = field[0].index(column1.upper())
        column2 = field[0].index(column2.upper())
        field[8 - row1 + 1][column1] = '.'
        field[8 - row2 + 1][column2] = fig1
        return field
    
    def change_fig(self, c: str, r: int, fig: str, field: list):
        """Изменяет фигуру на указанной позиции.

        Args:
            c (str): Буква столбца.
            r (int): Номер строки.
            fig (str): Новая фигура.
            field (list): Двумерный список, представляющий текущее состояние доски.

        Returns:
            list: Обновлённое состояние доски.
        """
        field[8 - r + 1][field[0].index(c.upper())] = fig
        return field
    
    def can_hit_or_step(self, fig1, fig2):
        """Проверяет, может ли фигура fig1 атаковать или занять позицию фигуры fig2.

        Args:
            fig1 (str): Фигура, которая пытается сделать ход.
            fig2 (str): Фигура на целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        if fig2 == '.' or (fig2[0].isupper() and fig1[0].islower()) or (fig1[0].isupper() and fig2[0].islower()):
                return True
        return False
    
    def fing_fig(self, fig: str, field: list):
        """Находит все позиции указанной фигуры на доске.

        Args:
            fig (str): Фигура, которую нужно найти.
            field (list): Двумерный список, представляющий текущее состояние доски.

        Returns:
            list: Список координат фигуры в формате ['A1', 'B2', ...].
        """
        all_fig = []
        xy = [0, 0]
        r = 8
        for row in field[1:-1]:
            c = 1
            if row.count(fig) >= 1:
                xy[1] = r
                for el in row[1:-1]:
                    if el == fig:
                        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                        c1 = convert_column[c - 1]
                        xy[0] = c1
                        all_fig.append(xy[0] + str(xy[1]))
                    c += 1
            
            r -= 1
        return all_fig
    
    def check_mat(self, color: str, field: list):
        """Проверяет, находится ли король под шахом.

        Args:
            color (str): Цвет короля ('w' для белого, 'b' для чёрного).
            field (list): Двумерный список, представляющий текущее состояние доски.

        Returns:
            str: 'Mat', если король под шахом, иначе 'all good'.
        """
        fig = 'K' if color == 'w' else 'k'
        cr = Board().fing_fig(fig, field)[0]
        c, r = cr[0], cr[1]
        fig = 'R' if color == 'b' else 'r'
        allfig = Board().fing_fig(fig, field)
        for f in allfig:
            if Rook(f[0], int(f[1]), field).can_step(c, r):
                return 'Mat'
        fig = 'B' if color == 'b' else 'b'
        allfig = Board().fing_fig(fig, field)
        for f in allfig:
            if Bishop(f[0], int(f[1]), field).can_step(c, r):
                return 'Mat'
        fig = 'Q' if color == 'b' else 'q'
        allfig = Board().fing_fig(fig, field)
        for f in allfig:
            if Queen(f[0], int(f[1]), field).can_step(c, r):
                return 'Mat'
        fig = 'N' if color == 'b' else 'n'
        allfig = Board().fing_fig(fig, field)
        for f in allfig:
            if Knight(f[0], int(f[1]), field).can_step(c, r):
                return 'Mat'
        fig = 'P' if color == 'b' else 'p'
        allfig = Board().fing_fig(fig, field)
        for f in allfig:
            if Pawn(f[0], int(f[1]), field).can_step(c, r):
                return 'Mat'
        
        return 'all good'

    def rewrite_castling(self, c1: str, r1: int, c2: str, r2: int, field: list):
        """Выполняет рокировку.

        Args:
            c1 (str): Буква столбца начальной позиции короля.
            r1 (int): Номер строки начальной позиции короля.
            c2 (str): Буква столбца конечной позиции короля.
            r2 (int): Номер строки конечной позиции короля.
            field (list): Двумерный список, представляющий текущее состояние доски.

        Returns:
            list: Обновлённое состояние доски.
        """
        fig1 = Board().point_position(c1, int(r1), field)
        fig2 = 'r' if fig1.islower() else 'R'
        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if c2 == 'C':
            c1 = convert_column.index(c1) + 1
            c2 = convert_column.index(c2) + 1
            avg_c = (c2 + c1) // 2
            field[8 - int(r1) + 1][c2] = fig1
            field[8 - int(r1) + 1][c1] = '.'
            field[8 - int(r1) + 1][avg_c] = fig2
            field[8 - int(r1) + 1][1] = '.'
        
        if c2 == 'G':
            c1 = convert_column.index(c1) + 1
            c2 = convert_column.index(c2) + 1
            avg_c = (c2 + c1) // 2
            field[8 - int(r1) + 1][c2] = fig1
            field[8 - int(r1) + 1][c1] = '.'
            field[8 - int(r1) + 1][avg_c] = fig2
            field[8 - int(r1) + 1][-2] = '.'
        return field
             

class Figures(object):
    """Базовый класс для всех фигур."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует фигуру.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        self.column = column
        self.row = row
        self.field = field
    
    def can_hit_or_step(self, fig1, fig2):
        """Проверяет, может ли фигура fig1 атаковать или занять позицию фигуры fig2.

        Args:
            fig1 (str): Фигура, которая пытается сделать ход.
            fig2 (str): Фигура на целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        if fig2 == '.' or (fig2[0].isupper() and fig1[0].islower()) or (fig1[0].isupper() and fig2[0].islower()):
                return True
        return False
    
    def auto_step(self, c: str, r: int):
        """Автоматически определяет, может ли фигура сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        now_fig = Board().point_position(self.column, self.row, self.field).lower()
        if now_fig == 'r':
            return Rook(self.column, self.row, self.field).can_step(c, r)
        elif now_fig == 'p':
            return Pawn(self.column, self.row, self.field).can_step(c, r)
        elif now_fig == 'q':
            return Queen(self.column, self.row, self.field).can_step(c, r)
        elif now_fig == 'k':
            return King(self.column, self.row, self.field).may_step(c, r)
        elif now_fig == 'n':
            return Knight(self.column, self.row, self.field).can_step(c, r)
        elif now_fig == 'b':
            return Bishop(self.column, self.row, self.field).can_step(c, r)
        elif now_fig == '.':
            return False
        

class Rook(Figures):
    """Класс, представляющий ладью."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует ладью.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        Figures.__init__(self, column, row, field)
    
    def can_step(self, c: str, r: int):
        """Проверяет, может ли ладья сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        move = [c, r]
        if (self.column != move[0] and self.row == move[1]) or (self.column == move[0] and self.row != move[1]):
            pass
        else:
            return False
        all_step_may = []
        buk = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        buk = buk[buk.index(self.column):buk.index(move[0]) + 1] if buk[buk.index(self.column):buk.index(move[0]) + 1] else buk[buk.index(move[0]):buk.index(self.column) + 1]
        num = ['1', '2', '3', '4', '5', '6', '7', '8']
        num = num[num.index(str(self.row)):num.index(str(move[1])) + 1] if num[num.index(str(self.row)):num.index(str(move[1])) + 1] else num[num.index(str(move[1])):num.index(str(self.row)) + 1]
        for c in buk:
            for r in num:
                if (self.column == c or self.row == r) and (move[0] == c or move[1] == r):
                    all_step_may.append(c + r)
        all_step_may = all_step_may[1:]
        all_step_may = all_step_may[:-1]
        if not all_step_may:
            pass
        else:
            for step in all_step_may:
                if Board().point_position(step[0], int(step[1]), self.field) != '.':
                    return False
        fig1 = Board().point_position(self.column, int(self.row), self.field)
        fig2 = Board().point_position(move[0], int(move[1]), self.field)
        if Figures(self.column, self.row, self.field).can_hit_or_step(fig1, fig2):
            pass
        else:
            return False
        return True
        

class King(Figures):
    """Класс, представляющий короля."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует короля.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        Figures.__init__(self, column, row, field)
    
    def can_step(self, c: str, r: int):
        """Проверяет, может ли король сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        move = [c, r]
        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        move[0] = convert_column.index(c) + 1
        self_column = convert_column.index(self.column) + 1
        if abs(self_column - move[0]) <= 1 and abs(self.row - move[1]) <= 1: 
            pass
        else:
            return False
        fig1 = Board().point_position(self.column, int(self.row), self.field)
        fig2 = Board().point_position(move[0], int(move[1]), self.field)
        if Figures(self.column, self.row, self.field).can_hit_or_step(fig1, fig2):
            return True
        else:
            return False

    def castling(self, c: str, r: int, count_step_king: int):
        """Проверяет, возможна ли рокировка.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.
            count_step_king (int): Количество ходов, сделанных королём.

        Returns:
            bool: True, если рокировка возможна, иначе False.
        """
        move = [c, r]
        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        move[0] = convert_column.index(c) + 1
        self_column = convert_column.index(self.column) + 1
        if (count_step_king == 0) and (self.column == 'E') and (self.row == 1) and (Board().point_position(self.column, self.row, self.field).islower()) and (   (self_column - move[0] == 2 and self.row == move[1] == 1 and Board().point_position('A', 1, self.field) == 'r' and all([True if Board().point_position(i, self.row, self.field) == '.' else False for i in range(4, 1, -1)])) or  (move[0] - self_column == 2 and self.row == move[1] == 1 and Board().point_position('H', 1, self.field) == 'r' and all([True if Board().point_position(i, self.row, self.field) == '.' else False for i in range(6, 7 + 1)])) ):
            return True
        elif (count_step_king == 0) and (self.column == 'E') and (self.row == 8) and (Board().point_position(self.column, self.row, self.field).isupper()) and (   (self_column - move[0] == 2 and self.row == move[1] == 8 and Board().point_position('A', 8, self.field) == 'R' and all([True if Board().point_position(i, self.row, self.field) == '.' else False for i in range(4, 1, -1)])) or  (move[0] - self_column == 2 and self.row == move[1] == 8 and Board().point_position('H', 8, self.field) == 'R' and all([True if Board().point_position(i, self.row, self.field) == '.' else False for i in range(6, 7 + 1)])) ):
            return True
        else: return False

    def may_step(self, c: str, r: int):
        """Проверяет, может ли король сделать ход без попадания под шах.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        if King(self.column, self.row, self.field).can_step(c, r):
            color = 'b' if Board().point_position(self.column, self.row, self.field).islower() else 'w'
            field2 = self.field
            Board().rewriter(self.column, self.row, c, r, field2)# проверить
            if Board().check_mat(color, field2) == 'all good':
                return True
        return False


class Knight(Figures):
    """Класс, представляющий коня."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует коня.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        Figures.__init__(self, column, row, field)
    
    def can_step(self, c: str, r: int):
        """Проверяет, может ли конь сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        move = [c, int(r)]
        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        move[0] = convert_column.index(c) + 1
        self_column = convert_column.index(self.column) + 1
        if (abs(self_column - move[0]) == 2 and abs(self.row - move[1]) == 1) or  (abs(self_column - move[0]) == 1 and abs(self.row - move[1]) == 2):
            pass
        else:
            return False
        fig1 = Board().point_position(self.column, int(self.row), self.field)
        fig2 = Board().point_position(move[0], int(move[1]), self.field)
        if Figures(self.column, self.row, self.field).can_hit_or_step(fig1, fig2):
            return True
        else:
            return False


class Bishop(Figures):
    """Класс, представляющий слона."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует слона.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        Figures.__init__(self, column, row, field)
    
    def can_step(self, c: str, r: int):
        """Проверяет, может ли слон сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        move = [c, int(r)]
        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        move[0] = convert_column.index(c) + 1
        self_column = convert_column.index(self.column) + 1
        if abs(self_column - move[0]) == abs(self.row - int(move[1])):
            pass
        else:
            return False
        n = abs(self_column - move[0])
        all_step = []
        op = ()
        if self_column >= move[0] and self.row >= move[1]:
            op = ('-','-')
        elif move[0] >= self_column and self.row >= move[1]: 
            op = ('+','-')
        elif move[0] >= self_column and move[1] >= self.row:
            op = ('+','+')
        elif self_column >= move[0] and move[1] >= self.row:
            op = ('-','+')
        
        for i in range(1, n):
            first = convert_column[eval(f'{self_column - 1} {op[0]} {i}')]
            second = eval(f'{self.row} {op[1]} {i}')
            all_step.append(f'{first}{second}')
        for fig in all_step:
            if Board().point_position(fig[0], int(fig[1]), self.field) != '.':
                return False
        fig1 = Board().point_position(self.column, self.row, self.field)
        fig2 = Board().point_position(move[0], move[1], self.field)
        if Figures(self.column, self.row, self.field).can_hit_or_step(fig1, fig2):
            pass
        else:
            return False
        return True
    

class Pawn(Figures):
    """Класс, представляющий пешку."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует пешку.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        Figures.__init__(self, column, row, field)
    
    def can_step(self, c: str, r: int):
        """Проверяет, может ли пешка сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        move = [c, int(r)]
        color = 'b' if Board().point_position(self.column, int(self.row), self.field).islower() else 'w'
        convert_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        move[0] = convert_column.index(c) + 1
        self_column = convert_column.index(self.column) + 1
        if (((self.row - move[1]) == 1 and color == 'w') or ((move[1] - self.row) == 1 and color == 'b')) and (self_column == move[0]):
            return True
        if (abs(self.row - move[1]) == 2) and ((self.row == 2 and Board().point_position(self.column, self.row, self.field) == 'p') or (self.row == 7 and Board().point_position(self.column, self.row, self.field) == 'P')):
            print(False and False)
            return True
        elif abs(self.row - move[1]) == 1 and abs(self_column - move[0]) == 1 and Board().point_position(c, r, self.field) != '.':
            fig1 = Board().point_position(self.column, self.row, self.field)
            fig2 = Board().point_position(c, r, self.field)
            if Figures(self.column, self.row, self.field).can_hit_or_step(fig1, fig2):
                return True
            else: return False
        else: return False
    
    def can_transform(self):
        """Проверяет, может ли пешка превратиться в другую фигуру.

        Returns:
            bool: True, если пешка может превратиться, иначе False.
        """
        fig = Board().point_position(self.column, self.row, self.field)
        if fig.islower() and self.row == 8:
            return True
        elif fig.isupper() and self.row == 1:
            return True
        return False


class Queen(Figures):
    """Класс, представляющий ферзя."""

    def __init__(self, column: str, row: int, field: list):
        """Инициализирует ферзя.

        Args:
            column (str): Буква столбца.
            row (int): Номер строки.
            field (list): Двумерный список, представляющий текущее состояние доски.
        """
        Figures.__init__(self, column, row, field)
    
    def can_step(self, c: str, r: int):
        """Проверяет, может ли ферзь сделать ход.

        Args:
            c (str): Буква столбца целевой позиции.
            r (int): Номер строки целевой позиции.

        Returns:
            bool: True, если ход возможен, иначе False.
        """
        return Rook(self.column, self.row, self.field).can_step(c, r) or Bishop(self.column, self.row, self.field).can_step(c, r)

field = Board().start_board()
Board().print_board(field)
print(Figures('E', 8, field).auto_step('D', 7))

'''
def main():
    """Основная функция для запуска шахматной игры."""
    count_step = 0
    count_step_king_b = 0
    count_step_king_w = 0
    field = Board().start_board()
    colot_c = 1
    while True:
        color_new = 'white' if colot_c == 1 else 'black'
        color = color_new[0]
        Board().print_board(field)
        try:
            my_coord = (input(f"Введите координаты фигуры через пробел, ход {color_new} (Например: А2 A3), ходов было - {count_step}:"))
            c, r, c1, r1 = my_coord[0].upper(), my_coord[1], my_coord[3].upper(), my_coord[4] 
        except:
            print("Неправильный ввод координат")
            continue
        coord = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if c in coord and 1 <= int(r) <= 8 and c1 in coord and 1 <= int(r1) <= 8:
            r, r1 = int(r), int(r1)
        else:
            print("Неправильный ввод координат")
            continue
        if (Board().point_position(c, r, field).isupper() and colot_c == 0) or (Board().point_position(c, r, field).islower() and colot_c == 1):
            print(f"Сейчас ход {color_new}, выберете {color_new} фигуру")
            continue
        fig = Board().point_position(c, r, field)
        now_step_king = count_step_king_w if fig == 'K' else count_step_king_b
        if King(c, r, field).castling(c1, r1, now_step_king) and fig.upper() == 'K':
            field = Board().rewrite_castling(c, r, c1, r1, field)
            count_step_king_b += 1 if fig.islower() else 0
            count_step_king_w += 1 if fig.isupper() else 0
            count_step += 1
            colot_c = 1 if colot_c == 0 else 0
            continue
        elif King(c, r, field).castling(c, r, 0) and fig.upper() == 'K':
            print('Нельзя сделать ракировку')
        if Board().check_mat(color, field) == 'Mat':
            field2 = field
            if Figures(c, r, field).auto_step(c1, r1):
                field2 = Board().rewriter(c, r, c1, r1, field2)
                if Board().check_mat(color, field2) == 'Mat':
                    print('Вы не можете так сходить, вым обьявлен мат')
                    continue
                else:
                    field = field2
                    if field[1].count('p') or field[-2].count('P'):
                        f = ['b', 'n', 'q', 'r', 'p']
                        fig = input('Выберите в кого превращаться:')
                        if fig.lower() in  f:
                            Board().change_fig(c1, r1, fig, field)
                        else:
                            print('Неправильная фигура')
                            continue
                    colot_c = 1 if colot_c == 0 else 0
                    count_step += 1
                    continue
            else:
                print('Неправильный ввод хода')
                continue 

        if Figures(c, r, field).auto_step(c1, r1):
            field = Board().rewriter(c, r, c1, r1, field)
            colot_c = 1 if colot_c == 0 else 0
            count_step += 1
            if field[1].count('p') or field[-2].count('P'):
                f = ['b', 'n', 'q', 'r', 'p']
                fig = input('Выберите в кого превращаться:')
                if fig.lower() in  f:
                    Board().change_fig(c1, r1, fig, field)
                else:
                    print('Неправильная фигура')
                    continue
            
            if fig in 'Kk':
                count_step_king_b += 1 if fig.islower() else 0
                count_step_king_w += 1 if fig.isupper() else 0
        else:
            print('Неправильный ход')

        
main()#'''