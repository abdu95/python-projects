# list of coordinates
# (x, y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)

# for x in range(4):
#     print(x)

# how nested loop works
# x 0
#   y 0
#   y 1
#   y 2
# x 1
#   y 0
#   y 1
#   y 2

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")