import argparse
import sys
from cache import Cache

CACHE = 20 #change according to desired cache size: 2^20=1MB
BLOCK = 6  #change according to desired cache block size 2^6=64bytes
WAYS = 4   #change accordin to desired number of ways 2^4=16 ways

cache_size = 2 ** CACHE
block_size = 2 ** BLOCK
ways = 2 ** WAYS
#Initialize cache
cache = Cache(cache_size, block_size, ways)

f= open(sys.argv[1],"r+")
f1 = f.readlines()      #Process file line by line

hits = 0
misses = 0

for x in f1:
    line = x.split()
    try:
        instr = line[1] #get instruction W or R
        virtual_addr = line[2]  #get virtual address
        
        #verify if address has x or not:eg 0xA2 OR A2
        if "x" in virtual_addr:             
            address = int(virtual_addr,0)
        else:          
            address = int(virtual_addr,16)
        
        if instr == "R":
            #check if address in cache
            cache_block = cache.read(address)
            if cache_block:
                hits += 1
            else:
                #implement LRU
                cache.load(address)
                cache.read(address)
                misses += 1  
        elif instr == "W":
            #check if address in cache
            written = cache.write(address)
            if written:
                hits += 1
            else:
                #implement write-back
                misses += 1
                cache.load(address)
                cache.write(address)
    except IndexError:
        """ERROR: Invalid address"""
    except:
        """ERROR: Invalid address"""
"""Print stats"""
miss_rate = 100 * (float(misses)/float(hits + misses) if misses else 1) 
#print("\nHits: "+ str(hits)+"\nMisses: "+ str(misses)+"\nTotal: "+str(misses+hits))
print("Cache Miss Rate: {0:.2f}%".format(miss_rate))
