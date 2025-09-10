
def squares(integer: int) -> int:
    if integer <= 0:
        print("That number is not a positive integer")
    else:
        sum = 0
    for i in range(1, integer):
        print("integer: ", i, "square root: ", i * i)
        sum += i * i
    print("sum of all square roots: ", sum)
    return sum
        
    
    