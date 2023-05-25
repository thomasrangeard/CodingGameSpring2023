import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
exist_egg_action = False

liste_cells = []

CV_EGGS = 1
CV_CRYSTAL = 2
class Cell:
    def __init__(self, id, type, resource, ants, voisin_1, voisin_2, voisin_3, voisin_4, voisin_5, voisin_6):
        self.type = type
        self.id = id
        self.resource = resource
        self.ants = 0
        self.voisins = []
        self.voisin_1 = voisin_1
        self.voisins.append(voisin_1)
        self.voisin_2 = voisin_2
        self.voisins.append(voisin_2)
        self.voisin_3 = voisin_3
        self.voisins.append(voisin_3)
        self.voisin_4 = voisin_4
        self.voisins.append(voisin_4)
        self.voisin_5 = voisin_5
        self.voisins.append(voisin_5)
        self.voisin_6 = voisin_6
        self.voisins.append(voisin_6)
        print(f"voisins {self.voisins}", file=sys.stderr, flush=True)
        

def getCell(index):
    if(index < len(liste_cells)):
        return liste_cells[index]
    else :
        return None


number_of_cells = int(input())  # amount of hexagonal cells in this map

MatDistance = []
for i in range (number_of_cells) :
    MatDistance.append([])
    for j in range (number_of_cells) :
         MatDistance[i].append(0)

def AddNeigh(index_i, neigh, poids_neigh) :
    if neigh != None and neigh >= 0 :
        if(MatDistance[index_i][neigh] == 0) :
            MatDistance[index_i][neigh]+=poids_neigh
        if(MatDistance[neigh][index_i] == 0): 
            MatDistance[neigh][index_i]+=poids_neigh 

for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    cell = Cell(i, _type, initial_resources,0,neigh_0, neigh_1, neigh_2,neigh_3,neigh_4, neigh_5)
    AddNeigh(i, neigh_0,1)
    AddNeigh(i, neigh_1,1)
    AddNeigh(i, neigh_2,1)
    AddNeigh(i, neigh_3,1)
    AddNeigh(i, neigh_4,1)
    AddNeigh(i, neigh_5,1)
    liste_cells.append(cell)
number_of_bases = int(input())
for i in input().split():
  my_base_index = int(i)
for i in input().split():
  opp_base_index = int(i)


action = []


def GoTo(from_p, to_p):

    print(f"egg {to_p}", file=sys.stderr, flush=True)
    action.append(f"LINE {from_p} {to_p} {nb_crystal*2}")


def GoEggsClosest(from_point, niv_actuel, limit_search):
    if niv_actuel == limit_search :
        return False
    if getCell(from_point).type == CV_EGGS :
        GoTo(my_base_index, from_point)
        if(getCell(from_point).resource < niv_actuel * 5) :
            for voisin in getCell(from_point).voisins:
                if voisin != -1:
                    if GoEggsClosest(voisin,1, 3) :
                        return True
        return True
    else : 
        for voisin in getCell(from_point).voisins:
            if voisin != -1:
                if GoEggsClosest(voisin,niv_actuel+1, limit_search) :
                    return True

    return False

# game loop
while True:
    action = []
    nb_eggs = 0
    nb_crystal = 0
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = [int(j) for j in input().split()]

        liste_cells[i].ants = my_ants
        liste_cells[i].resource = resources
        if liste_cells[i].type == CV_EGGS and liste_cells[i].resource > 0:
            nb_eggs = nb_eggs +1
        if liste_cells[i].type == CV_CRYSTAL and liste_cells[i].resource > 0:
            nb_crystal = nb_crystal +1
    GoEggsClosest(my_base_index, 1, 5)
    for i in range (number_of_cells):
        if getCell(i).type == CV_CRYSTAL  and getCell(i).resource > 0:
            action.append(f"LINE {my_base_index} {i} {nb_crystal}")
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(";".join(action))
