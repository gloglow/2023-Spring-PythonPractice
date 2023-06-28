def generate(n, prefix):
    if n==len(prefix):
        print(prefix)
    else:
        generate(n, prefix+'a')
        generate(n, prefix+'b')

generate(3, '')