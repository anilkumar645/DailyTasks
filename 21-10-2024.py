def count_char(d):
        l = len(d)
        d1 = {}
        for i in d:
                if i in d1:
                        d1[i] = d1[i] + 1 
                else:
                        d1[i] = 1 
        return d1 
d = "skywavessoftwares"
print(count_char(d))

