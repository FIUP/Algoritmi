
class cluster:
    def __init(self, P):
        self.P = P
        self.center = self.calcCenter()
    
    def calcCenter(self):
        sum_x, sum_y = 0, 0
        for (x,y) in self.P:
            sum_x = sum_x + x
            sum_y = sum_y + y
        
        n = len(self.P)
        return (sum_x/n , sum_y/n)
