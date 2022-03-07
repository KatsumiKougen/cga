p,s=lambda n:not True in[n%i==0 for i in range(2,n)],lambda m:p(sum([int(z)for z in str(m)])if p(m)else 4)
