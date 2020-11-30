# This ode is made by Musab Schluck, it's simple and very readable
# hope it helps someone someday.
#values		1,1,2,3,5,8,13
# index		1,2,3,4,5,6,7

def feb(n, memo, result = None):
        if memo[n] != None:
                return memo[n]
        if n == 1 or n == 2:
                result = 1
        else:
                result = feb(n-1, memo) + feb(n-2, memo)
        memo[n] = result
        return result

n = 100
memo = [None for x in range(n+1)]
print(feb(n, memo))
