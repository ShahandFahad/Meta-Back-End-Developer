# Self coded solution for tower of hanoi

def tower_of_hanoi(disks, source, helper, destination):
    if (disks == 1):
        print("Tower -> {}: {} -> {}.".format(disks, source, destination))
        return
    
    tower_of_hanoi(disks - 1, source, destination, helper)
    print("Tower -> {}: {} -> {}.".format(disks, source, destination))
    tower_of_hanoi(disks - 1, helper, source, destination)
    
    
    
    



# Asks for number of disks
disks = 3
print("Number of Moves for the {} disks problem: {} is: ".format(disks, 2**disks - 1))
tower_of_hanoi(disks, 'A', 'B', 'C')