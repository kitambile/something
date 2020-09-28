
















def add_up(lst):
    total=0
    for num in lst:
        total+=num
    return total

def is_balanced(num_list):
    C = [2, 5, 1, 3, 3, 2]
    
    
    
    
    if num_list=="C":
        num=len(C)
        print(C)
        print(num)
        num_div=(num//2)
        print(num_div)
        if (num % 2)==0:
            print("number is even")
            print(C[:num_div], C[num_div:])
            halfC_1=C[:num_div]
            print(halfC_1)
            halfC_2=C[num_div:]
            print(halfC_2)
            print(sum(halfC_1))
            print(sum(halfC_2))
            if add_up(halfC_1)==add_up(halfC_2):
                return "true"
            else:
                return "false"
            
        else:
            print("number is odd")
            del C[num_div]
            print(C)
            num=len(C)
            print(num)
            halfC_1=C[:num_div]
            print(halfC_1)
            halfC_2=C[num_div:]
            print(halfC_2)
            print(sum(halfC_1))
            print(sum(halfC_2))
            if add_up(halfC_1)==add_up(halfC_2):
                return "true"
            else:
                return "false"
            
            
                  
    
    
    


















print(is_balanced("C"))
