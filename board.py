class Board():
    def __init__(self):
        self.matrix = []
        for i in range(5):
            linha = []
            for j in range(5):
                linha.append(0)
            self.matrix.append(linha)

    def create_board1(self):
        for i in range(0,5):
            for j in range(0,5):
                if i == 0:
                    if j == 0 or j == 1 or j == 2:
                        self.matrix[i][j] = 2
                    else:
                        self.matrix[i][j] = 0
                elif i == 1:
                    if j in [1,2,3,4]:
                        self.matrix[i][j] = 2
                    else:
                        self.matrix[i][j] = 0
                elif i == 2:
                    if j in [1,2,3,4]:
                        self.matrix[i][j] = 2
                    else:
                        self.matrix[i][j] = 0      
                elif i == 3:
                    if j in [3,4]:
                        self.matrix[i][j] = 2
                    else:
                        self.matrix[i][j] = 0     
                elif i == 4:
                    if j == 3:
                        self.matrix[i][j] = 2
                    elif j == 4:
                        self.matrix[i][j] = 3
                    else:
                        self.matrix[i][j] = 0                  

    def create_board2(self):
        for i in range(0,5):
            for j in range(0,5):
                if i == 0:
                    if j in [2,3]:
                        self.matrix[i][j] = 2
                    elif j == 4:
                        self.matrix[i][j] = 3  
                elif i == 1:
                    if j in [1,2,3,4,5]:
                        self.matrix[i][j] = 2
                elif i == 2:
                    if j in [1,2,3,4,5]:
                        self.matrix[i][j] = 2      
                elif i == 3:
                    if j in [2,3,4]:
                        self.matrix[i][j] = 2     
                elif i == 4:
                    if j == 4:
                        self.matrix[i][j] = 2
     

        '''0 [[0,2, 2, 3, 0], 
           1 [2, 2, 2, 2, 2], 
           2 [2, 2, 2, 2, 2], 
           3 [0, 2, 2, 2, 0], 
           4 [0, 0, 0, 2, 0]] '''






'''
for i in range(len(self.matrix)):
    for j in range(len(self.matrix[i])):
        if self.matrix[i][j] == 3:
            return True   

            [[0, 1, 2, 6, 7], [9, 5, 4, 8, 2], [7, 5, 9, 0, 2], [7, 5, 9, 0, 2], [7, 5, 9, 0, 2]]
            
            
            [[0, 0, 0, 0, 0]]
            

            [[0, 1, 2, 3, 7], [9, 5, 4, 8, 2], [7, 5, 9, 0, 2], [7, 5, 9, 0, 2], [7, 5, 9, 0, 2]]

           0 [[0,2, 2, 3, 0], 
           1 [2, 2, 2, 2, 2], 
           2 [2, 2, 2, 2, 2], 
           3 [0, 2, 2, 2, 0], 
           4 [0, 0, 0, 2, 0]]
            '''