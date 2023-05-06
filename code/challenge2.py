names = ["John", "James", "Jenna", "Josh", "Jacob", "Jerry"]
run = [6, 8, 5, 7, 4, 9]
rest = [20, 25, 16, 23, 32, 18]
speed = [10, 8, 12, 7, 9, 5]

run_rest = [ run[i]+rest[i] for i in range(len(names)) ]

time = 1234

for i in range(len(names)):
    print(names[i], speed[i]*( run[i]*(time//(run_rest[i])) + 
                  min( run[i], time%(run_rest[i]) ) 
                )
         )

# results
# John 2880
# James 2432
# Jenna 3540
# Josh 2037
# Jacob 1260
# Jerry 2070





