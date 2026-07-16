class Solution:

    def check_lines(self, board: List[List[str]]) -> bool:
        for line in board:
            cleanLine = list(filter(lambda x: x != '.', line))
            if len(set(cleanLine)) != len(cleanLine):
                return False
        return True

    def check_squares(self, board: List[List[str]]) -> bool:
        boxes = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + (j // 3)
                boxes[box_index].append(board[i][j])
        return self.check_lines(boxes)

    def check_h_lines(self, board: List[List[str]]) -> bool:
        boxes = [[] for _ in range(9)]
        for j in range(9):
            for i in range(9):
                boxes[j].append(board[i][j])
        return self.check_lines(boxes)
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_lines(board) and self.check_h_lines(board) and self.check_squares(board)