#Matrix Multiplication
def accept_matrix(matrix_num):
   rows = int(input("Enter the number of rows: "))
   cols = int(input("Enter the number of columns: "))
   matrix = []

   print(f"enter the numbers for the rows in the matrix: ")
   for i in range(rows):
      row = list(map(int, input(f"ROw {i+1}: ").split()))
      matrix.append(row)
      return matrix, rows, cols
   
