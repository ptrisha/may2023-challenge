
GRID_DIM=5

# generate the adjacent neighbours
def generate_neighbours(grid):
    
    for cell in grid:
        neighbours=[]
        row, col = cell
        north = (row-1, col)
        south = (row+1, col)
        east = (row, col+1)
        west = (row, col-1)
        if north[0] >= 0:
           neighbours.append(north)
        if south[0] < GRID_DIM:
           neighbours.append(south)
        if east[1] < GRID_DIM:
           neighbours.append(east)
        if west[1] >= 0:
           neighbours.append(west)
        neighbours1 = [ row*GRID_DIM + col for row, col in neighbours]
        grid[cell]['neighbours'] = sorted(neighbours1)
    return grid

def transition(state, nb_states ):
    sum_nb = sum(nb_states)
    if state:
        if sum_nb==1:
            next_state=1
        else:
            next_state=0
    else:
        if sum_nb >= 1 and sum_nb <=2:
            next_state=1
        else:
            next_state=0
    return next_state  
        

# returns state of next time step
def step_grid(grid, current_state):

    nb_list =  [ dd['neighbours'] for dd in list(grid.values()) ]
    print("nb_list:", nb_list)
    nb_states = []
    for nb in nb_list:
        state_list = []
        for id in nb:
            state_list.append(current_state[id])
        nb_states.append(state_list)
    

    next_state=[ transition(current_state[i], nb_states[i]) for i in range(len(current_state)) ]
    return next_state



if __name__ == '__main__':
   
    # generate dictionary with cell as key
    grid = {}

    for r in range(GRID_DIM):
        for c in range(GRID_DIM):
            tup = (r, c)
            grid[tup] = { 'id' : (r*GRID_DIM+c), 'neighbours': [] }

    grid = generate_neighbours(grid)

    print("Grid")
    print("Grid size:", len(grid))
    for k in grid:
        print(grid[k])

    # '{0:b}'.format(2)  convert integer to binary string
    # '{0:025b}'.format(1)
    # int('111', 2) # convert a binary string to integer

    # set state at t=0
    #start_state = [ 0,0,0,0,1, 1,0,0,1,0, 1,0,0,1,1, 0,0,1,0,0, 1,0,0,0,0]
    start_state = [1,1,1,1,0, 1,0,0,0,0, 1,0,0,1,0, 0,1,0,1,0, 1,1,0,1,1]

    current_state = start_state[:len(start_state)]


    run = True
    store = []
    t=0
    curr_state = start_state[:len(start_state)]
    print("t=", t)
    b_str = "".join( [str(b) for b in curr_state] )
    print("start_state", curr_state, int(b_str, 2) )
    store.append(b_str)
    while run:
       t+=1
       print("t=", t)
       state = step_grid(grid, current_state) 
       b_str = "".join( [str(b) for b in state] )
       b_int = int(b_str, 2)
       print("next_state", state, b_int )
       current_state=state
       if b_int in store:
           run = False
           print("Found at t=", store.index(b_int))
       store.append(b_int)

    life_score = sum( [ current_state[i]*(2**i) for i in range(len(current_state))] )
    print("Lifeform score:", life_score)
