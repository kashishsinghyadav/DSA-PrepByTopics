
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                s += str(board[i][j])

        dirt = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [4, 2]
        }

        lvl = 0
        q = deque()
        q.append(s)
        vis = set()
        vis.add(s)

        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if curr == '123450':
                    return lvl
                stid = curr.find('0')
                for num in dirt[stid]:
                    temp = list(curr)
                    temp[num], temp[stid] = temp[stid], temp[num]
                    new_state = ''.join(temp)
                    if new_state not in vis:
                        q.append(new_state)
                        vis.add(new_state)
            lvl += 1
        return -1
