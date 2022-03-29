def tribonacci(signature, n):
    tribonacci = []

    for i in range(1, n+1):
        new_elm = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_elm)
        elm = signature.pop(0)
        tribonacci.append(elm)

    return tribonacci

num = int(input())
sig =[1, 1, 2]
print(*tribonacci(sig, num), sep=" ")
