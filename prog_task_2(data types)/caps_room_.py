n = input()
room_list = input().split()
room_set= set(room_list)
for ele in list(room_set):
    room_list.remove(ele)
cap_room_num = room_set.difference(set(room_list)).pop()
print(cap_room_num)