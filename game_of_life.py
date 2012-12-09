import Tkinter
import csv

universe = set()

#####################################################################
###  Input Logic
#####################################################################

def pattern_input(filename):
    with open(filename, 'rb') as csvfile:
        points = csv.reader(csvfile,delimiter=',')
        for row in points:
            universe.add((row[0],row[1]))


#####################################################################
###  Game Logic
#####################################################################

universe = set()

def get_moore_neighbourhood(x,y):
    # get the moore neighbourhood of a given cell
    moore_neighbourhood = set([(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)])
    return moore_neighbourhood

def count_neighbours(cell,universe):
    # count the number of living cells in the moore Neighbourhood of a cell.
    neighbourhood = get_moore_neighbourhood(cell[0],cell[1])
    return len(neighbourhood.intersection(universe))

def will_survive(count):
    # Check if a cell will survive
    if count == 2 or count == 3:
        return True
    else:
        return False

def will_be_born(count):
    # Check if an empty cell comes to life
    if count == 3:
        return True
    else:
        return False

def get_survivors(universe):
    survivors = set()
    for cell in universe:
        if will_survive(count_neighbours(cell,universe)) == True:
            survivors.add(cell)
    return survivors

def get_new_cells(universe):
    new_cells = set()
    for cell in universe:
        for position in get_moore_neighbourhood(cell[0],cell[1]):
            if position not in universe and will_be_born(count_neighbours(position,universe)) == True:
                new_cells.add(position)
    return new_cells

def tick(universe):
    new_universe = set()
    new_universe = get_new_cells(universe).union(get_survivors(universe))
    # prepares a new generation.
    return new_universe

####################################################################
####  Tkinter
####################################################################

def run(universe):
    universe = tick(universe)
    update()

   
def load():
    global cell
    for y in range(-1,61):
        for x in range(-1,81):
            cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline=None, fill="black")

def update():
    global canvas
    for position in universe:
        if position.x in range(-1,61) and position.y in range(-1,81):
            x,y = position.x,position.y
            canvas.itemconfig(cell[x][y], fill = "green")
        else:
            continue
    for y in range(-1,61):
        for x in range(-1,81):
            if canvas.itemcget(cell[x][y],'fill') == "green" and (x,y) not in universe:
                canvas.itemconfig(cell[x][y], fill = "black")
                canvas.itemconfig(cell[x][y], outline = "black")
    

def main():
    pattern_input(filename)
    run()
    root.after(50, main)



root = Tk()    
canvas = Canvas(root, width=800, height=600,highlightthickness=0, bd=0, bg='black')
canvas.pack()
load()
update()
main()
root.mainloop()
