import os,sys

# recursion  is kinda while loop or for loop, poka num ==0, num -1 

def num_test (num):
    if num == 0:
        print ("end of nums")
    else:
        print(num)
        num_test (num - 1)  
     
num_test(3)


list_1 = ['ES31-CTS', 'functional', 'synchronization', 'inter_call',
 'without_memory_barrier', 'ssbo_atomic_counter_mixed_dispatch_100_calls_1k_invocations']

# list_1="mirlan"
# print(list_1) 

def recursive_repw(list_1):
        
        if len(list_1) <= 1:
                return " 0 eken"
                  
        recursive_repw(list_1[1:])
        print(  list_1[0]    )

recursive_repw(list_1)                

# ===================================================
l = ["bir", "eki", "uch", "tort"]

def recur(l):
    if len(l) == 1:
        return("it is done")
    recur(l[1:])
    print(l[0])
     
recur(l)

