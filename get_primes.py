def get_primes(n):
    """
    get primes less than n using sieve algorithm.
    """
    is_p = [False,False]+[True]*(n-2)
    end = n**0.5
    for i in range(2,int(end)+1):
        if is_p[i]:
            is_p[i*i:n:i] = [False]*len(is_p[i*i:n:i])
    primes = [i for i,ip in enumerate(is_p) if ip]
    return primes
    
