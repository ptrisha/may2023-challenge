# Challenge 4 - 10 May 2023

def make_sublists(l):
    '''
    Create a list of sublists of l where the value of the elements 
    in each sublist is the same
    '''
    new_list = []
    curr_sublist= []
    i=0
    prev_val=-1
    while i < len(l):
        curr_val = l[i][1]
        if curr_val != prev_val:
           if len(curr_sublist)>=1:
               new_list.append(curr_sublist)
           curr_sublist=[]   # start a new sublist
           curr_sublist.append(l[i])
           prev_val= curr_val
        else: 
           curr_sublist.append(l[i])
        i+=1
    if len(curr_sublist):
        new_list.append(curr_sublist)
    print("Result of making sublists:", new_list)
    return new_list

def compute_loss(item, cost_dict):
    '''
    Computes total cost of the item adding costs of items which 
    share any of the workers in item.  Adds the total loss/cost
    to item. 
    '''
    loss=0
    worker1, worker2= item[0]
    for k in cost_dict:
        if (worker1 in k) or (worker2 in k):
            loss += cost_dict[k]
    return loss

def order_sublists(l, cost_dict):
    """
    Order each sublist in list l according to ascending order of
    total loss/cost.  Note that all items in the sublist have the
    same (individual) cost.
    """
    new_list=[]
    for sublist in l:
        subdict = {}
        for it in sublist:
            loss = compute_loss(it, cost_dict)
            subdict[it[0]] = (it[1], loss)
        ordered_sublist = sorted(subdict.items(), key=lambda x:x[1][1], reverse=True)
        new_list.append(ordered_sublist)
    return new_list


    
effs = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

#effs =[4, 2, 8, 1, 9]

print("Number of workers:", len(effs))

cost_dict = {}

# generate a dictionary of the cost of each possible pair
num_workers = len(effs)
num_pairs = 0
for i in range(num_workers):
    for j in range(i+1, num_workers):
        num_pairs += 1
        cost_dict[(i,j)] = abs(effs[i]-effs[j])
        #print("{}. ({},{})={}".format(num_pairs, i, j, cost_dict[(i,j)]))

print("Number of pairs generated: ", num_pairs)

# sort the cost dictionary in ascending order of the cost i.e. the value of the dictionary
sorted_cost = sorted(cost_dict.items(), key=lambda x:x[1])

print(sorted_cost)

print("Make sublists from sorted_cost")
subbed = make_sublists(sorted_cost)
print(subbed)

print("Oder the sublists according to total loss")
sorted_subbed = order_sublists(subbed, cost_dict)
print(sorted_subbed)

#flatten sorted_subbed
sorted_loss = [item for sublist in sorted_subbed for item in sublist]
print("Flattened list")
print(sorted_loss)
print("Number of elements in flattened list:", len(sorted_loss))


min_pairs = []

while len(sorted_loss)>1:
    min_pairs.append( sorted_loss[0] )
    sorted_loss.pop(0)
    print("Next selection of min pair", min_pairs)
    print("Sorted cost:", sorted_loss)
    worker1, worker2 = min_pairs[-1][0]
    print("Worker1: {},  Worker2: {}".format(worker1, worker2))
    # remove items from sorted list if either worker1 or worker2 is in the pair
    sorted_loss=[ elem for elem in sorted_loss if ((worker1 not in elem[0]) and (worker2 not in elem[0])) ]


if len(sorted_loss)==1:
    min_pairs.append(sorted_loss[0])

print(min_pairs)
print("Minimum cost: {}".format( sum( [ x[1][0] for x in min_pairs] ) ) )

workerpr_list = [ list(item[0]) for item in min_pairs ]
sorted_worker_list = sorted([item for sublist in workerpr_list for item in sublist])
print("List of sorted workers in min pairs:", sorted_worker_list)

# which worker is excluded?
for idx in range(len(sorted_worker_list)):
   if idx != sorted_worker_list[idx]:
       break
print("Excluded worker:", idx)


# Partial Output
# List of worker pairs (a,b) and individual-pair cost c and total cost d: ( (a, b), (c, d) )
# This is the configuration with minimum cost of 539
# [  ((15, 21), (0, 14446)), 
# ((0, 22), (1, 16440)), 
# ((7, 38), (1, 15730)), 
# ((12, 24), (1, 15170)), 
# ((9, 10), (1, 14834)), 
# ((11, 25), (1, 14202)), 
# ((2, 4), (2, 14252)), 
# ((6, 20), (2, 14206)), 
# ((19, 26), (2, 14054)), 
# ((27, 29), (3, 14462)), 
# ((1, 23), (4, 16198)), 
# ((8, 31), (6, 14722)), 
# ((16, 28), (11, 39044)), 
# ((30, 37), (11, 14054)), 
# ((35, 36), (20, 15134)), 
# ((5, 34), (28, 53320)), 
# ((14, 32), (57, 34284)), 
# ((17, 33), (103, 20576)), 
# ((3, 18), (285, 51092))  ]
#
# Minimum cost: 539
# List of sorted workers in min pairs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
# Excluded worker: 13
# Note that worker index starts with 0.

