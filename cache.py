
from __future__ import division
import sys

def main():
    f= open(sys.argv[1],"r+")
    f1 = f.readlines()      #Process file line by line

    hit=0
    miss =0
    write=0
    cache = []

    for x in f1:
        words = x.split()
        if words[0]=="#eof":
            break
        elif words[1]=='W':
            write=write+1
        elif words[1]== 'R':
            if words[2] in cache:
                hit = hit+1
            elif len(cache)<32000:
                miss=miss+1
                cache.append(words[-1])
            else:
                miss=miss+1
                cache.pop()
                cache.append(words[-1])
        else:
            print("Please input read of write")


    f.close()
    # for x in range(len(cache)): 
    #     print cache[x]
    total=miss+hit
    miss_ratio=(miss/total)*100
    print 'Writes: ', write
    print 'Hit: ', hit, 'and Miss: ', miss
    print 'Total number of lines: ', total
    print 'Miss ration: ', miss_ratio
    print 'Cache size',len(cache) 


if __name__ == "__main__":
    main()
