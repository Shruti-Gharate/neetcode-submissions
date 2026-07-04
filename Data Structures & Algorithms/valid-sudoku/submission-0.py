from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                key = (i // 3, j // 3)

                if value in rows[i] or value in columns[j] or value in boxes[key]:
                    return False
                
                rows[i].add(value)
                columns[j].add(value)
                boxes[key].add(value)

        return True