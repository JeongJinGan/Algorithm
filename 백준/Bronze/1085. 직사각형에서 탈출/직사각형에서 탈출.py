x, y, w, h = map(int,input().split())


list_ = []
list_.append(abs(0-x))
list_.append(abs(0-y))
list_.append(abs(w-x))
list_.append(abs(h-y))
list_.sort()
print(list_[0])