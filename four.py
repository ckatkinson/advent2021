def read_file(file):
    with open(file) as f:
        data = [x for x in f.read().splitlines() if x != '']
        callSeq = [int(x) for x in data[0].split(',')]
        boardData = [x.split() for x in data[1:]]
        return (callSeq, boardData)

def readBoardData(bD):
    boards = []
    while len(bD) > 0:
        boardInfo = bD[:5]
        board = [ [Square(int(x)) for x in line] for line in boardInfo]
        boards.append(board)
        bD = bD[5:]
    return [Board(b) for b in boards]

class Square():
    """
    Holds info about a bingo square
    """
    def __init__(self, number, marked=False):
        self.number = number
        self.marked = marked
    def __repr__(self):
        return "Square " + str(self.number) + ' ' + str(self.marked)

def transpose(matrix):
    """
    Compute matrix transpose
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

class Board():
    """
    It's a bingo board.
    """
    def __init__(self, board, last_called=-1):
        self.board = board
        self.last_called = last_called
       
    
    def __repr__(self):
        return "Board " + str(self.board)
        
    def call(self, n):
        """
        Update board as result of BINGO caller calling n
        """
        self.last_called = n
        for row in self.board:
            for square in row:
                if square.number == n:
                    square.marked = True

    def winner(self):
        """
        Did this board win BINGO? If so, return True, row/column
        """
        for row in self.board:
            if all([square.marked for square in row]):
                return (True, self.board)
        boardT = transpose(self.board)
        for row in boardT:
            if all([square.marked for square in row]):
                return (True, self.board)
        return (False, None)    

def play_BINGO( boards, callSeq ):
    """
    Call sequence of numbers and play bingo until someone wins. When that happens, return the winning row/column.
    """
    for n in callSeq:
        [board.call(n) for board in boards]
        wins = [(board.winner()[1], board.last_called) for board in boards if board.winner()[0]]
        if len(wins) > 0:
            return wins[0]

def play_long_BINGO( boards, callSeq ):
    """
    Call sequence of numbers and play bingo until we see the last winner.
    """
    winningBoards = []
    for n in callSeq:
        [board.call(n) for board in boards]
        winningBoards = winningBoards + [board for board in boards if board.winner()[0]]
        boards = [board for board in boards if not board.winner()[0]]
    lastWin = winningBoards[-1]
    return (lastWin.winner()[1], lastWin.last_called)



def winStateToAnswer( state ):
    call = state[1]
    board = state[0]
    nums = (s.number for row in board for s in row if s.marked == False)
    return call * sum(nums)

def main():
    input = read_file('./inputs/four.txt')
    seq = input[0]
    boardData = input[1]
    boards = readBoardData(boardData)
    print(f'Part 1: {winStateToAnswer(play_BINGO( boards, seq))}')
    print(f'Part 2: {winStateToAnswer(play_long_BINGO( boards, seq))}')

if __name__ == '__main__':
    main()
    

