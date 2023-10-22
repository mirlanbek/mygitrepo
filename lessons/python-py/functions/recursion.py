import os,sys

# recursion  is kinda while loop or for loop, poka num ==0, num -1 

# =====   int Nums ======================================= 
n = 7
def recur(n):
    if n > 0:
        print(n)
        recur(n-1)
    else:
        print("end of num")

recur(n)

# ============ List =======================================
l = ["bir", "eki", "uch", "tort"]

def recur(l):
    if len(l) > 0:
        print(l[0])
        recur(l[1:])
    else:
        print("end of list")

recur(l)

================ real time recursion ==========================================

list_1 = ['ES31-CTS', 'functional', 'synchronization', 'inter_call',
 'without_memory_barrier', 'ssbo_atomic_counter_mixed_dispatch_100_calls_1k_invocations']


def recur(list_1):
    if len(list_1) > 0:
        print(list_1[0])
        recur(list_1[1:])
    else:
        print("end of list")

recur(list_1)
