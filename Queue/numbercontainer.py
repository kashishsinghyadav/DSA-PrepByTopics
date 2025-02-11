class NumberContainers:

    def __init__(self):
        self.d={}
        
        self.d1=defaultdict(list)
        
        

    def change(self, index: int, number: int) -> None:
        
        self.d[index] = number 
        heappush(self.d1[number], index)

        

        

    def find(self, number: int) -> int:
        while self.d1[number] and self.d[self.d1[number][0]] != number:
            heappop(self.d1[number])
        return self.d1[number][0] if self.d1[number] else -1
