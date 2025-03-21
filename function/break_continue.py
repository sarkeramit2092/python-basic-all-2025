# break = Break out of a loop (STOP)
# continue = Skip current cycle of a loop (SKIP)

num = 0  
while num < 10:  
    num += 1  
    
    if num == 3:  
        print("Skipping", num)  
        continue  # Skip 3 and move to the next iteration  
    
    if num == 5:  
        print("Stopping at", num)  
        break  # Stop when num is 5  
    
    print(num)  
