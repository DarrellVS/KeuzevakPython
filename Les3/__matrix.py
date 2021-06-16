class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [ [ 0 for i in range(width) ] for j in range(height) ]

    def add(self, matrix):
        if(not isinstance(matrix, Matrix)):
            raise Exception("Argument must be a Matrix class")

        # Create a new matrix with identical width and height
        result = Matrix(self.width, self.height)

        # iterate through rows
        for i in range(self.height):
            # iterate through columns
            for j in range(self.width):
                result.setAtIndex(i, j, self.matrix[i][j] + matrix.getValueAt(i, j))

        return result

    def setFromArray(self, matrixArray):
        self.matrix = matrixArray

    def setAtIndex(self, x, y, value):
        self.matrix[x][y] = value

    def getMatrix(self):
        return self.matrix

    def getValueAt(self, x, y):
        return self.matrix[x][y]

    def print(self):
        # iterate through rows
        for i in range(self.height):
            # iterate through columns
            for j in range(self.width):
                print(self.matrix[i][j], end=" ")
        
            print()
        print()