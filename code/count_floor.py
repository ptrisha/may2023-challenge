p1="<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<"
p2="<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><"
p3="<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>"
p4="<>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>"
p5="<><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><"
p6="><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<"
p7="><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><"
p8="<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>"
p9="<><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><"
p10="<>><<>><<>><"

pattern = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10

floor = 0
for ch in pattern:
    if ch=="<":
        floor += 1
    else:
        floor -= 1
print(len(pattern))  # 642
print(floor)  # result is: 56

# Use list comprehension
print( sum([ 1 if ch=="<" else -1 for ch in pattern  ]) )  # sum is 56






