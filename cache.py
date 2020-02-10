from math import log

class Line:
    def __init__(self, size):
        self.use = -1
        self.tag = -1

class Cache:
    def __init__(self, size, block_size, ways):
        self._lines = [Line(block_size) for i in range(size // block_size)]
        self._ways = ways  
        self._size = size 
        self._block_size = block_size 

    def read(self, address):
        tag = address >> int(log(self._size // self._ways, 2))  # tag of cache line
        set = self.get_set(address)  # set of cache line
        line = None
        #search according to tag
        for candidate in set:
            if candidate.tag == tag:
                line = candidate
                break
        if line:
                self.update(line, set)
        #return true if found, otherwise false
        return True if line else False

    #Insert into cache line
    def load(self, address):
        tag = address >> int(log(self._size // self._ways, 2))  # tag of cache line
        set = self.get_set(address)  # set of cache line
        victim = set[0]
        for index in range(len(set)):
            if set[index].use < victim.use:
                victim = set[index]
        victim.use = 0
        victim.tag = tag

    def write(self, address):
        tag = address >> int(log(self._size // self._ways, 2)) # tag of cache line
        set = self.get_set(address)  # set of cache lines
        line = None
        #search according to tag
        for candidate in set:
            if candidate.tag == tag:
                line = candidate
                break
        if line:
            self.update(line, set)
        #return true if found, otherwise false
        return True if line else False

    def update(self, line, set):
        use = line.use
        if line.use < self._ways:
            line.use = self._ways
            for other in set:
                if other is not line and other.use > use:
                    other.use -= 1

    def get_set(self, address):
        setmask = (self._size // (self._block_size * self._ways)) - 1
        setno = (address >> int(log(self._block_size, 2))) & setmask
        idx = setno * self._ways
        sets = self._lines[idx:idx + self._ways]
        return sets