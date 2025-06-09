from fnmatch import fnmatch

for i in range(0, 10**9 + 1, 23):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i // 23)

# 113456759 6673927
# 133456749 7850397
# 153456739 9026867
# 173456729 10203337
# 193456719 11379807