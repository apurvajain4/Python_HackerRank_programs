_ = int(input())
set_n = set(map(int, input().split()))
_ = int(input())
set_b = set(map(int, input().split()))
new_set = set_n.difference(set_b)
print(len(new_set))
