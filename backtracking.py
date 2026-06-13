def maze(grid,path,i,j,n):
    if i==n and j==n:
        print(path)
        return
    if i+1<=n and grid[i+1][j]==1:
        maze(grid,path+'D',i+1,j,n)
    if j+1<=n and grid[i][j+1]==1:
        maze(grid,path+'R',i,j+1,n)
grid=[[1,1,0,1],
      [1,1,0,1],
      [0,1,0,0],
      [1,1,1,1]]
n=len(grid)
maze(grid,"",0,0,n-1)

#here a matrix is given here we travel from one point to end direction is only horizontal or vertical 
#and print all the possible path , D means down R means right