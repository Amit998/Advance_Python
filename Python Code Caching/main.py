from functools import cache,lru_cache
import time

# @cache
@lru_cache(maxsize=10)
def fibbo(n):
    if n== 1 or n==2:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)


start=time.time()

print(fibbo(500))
end=time.time()

print(end-start)