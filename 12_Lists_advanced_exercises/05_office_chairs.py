n = int(input())
free_chairs = 0
are_chairs_enough = True

for room in range(1, n+1):
    chairs, visitors = input().split()
    visitors = int(visitors)
    difference = abs(len(chairs) - visitors)
    if len(chairs) < visitors:
        print(f"{abs(len(chairs) - visitors)} more chairs needed in room {room}")
        are_chairs_enough = False
    else:
        free_chairs += difference

if are_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")

