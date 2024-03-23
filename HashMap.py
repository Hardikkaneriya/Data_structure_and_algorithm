# Author : Hardik kaneriya
# type : Simple HashMap implementation
# limitations : this Hashmap implement will not be able to handle Collision 
# when two keys are having the same hash key and try to store the value of that key in the 
# same hash location. In that case we need to handle collision problem

class HashMap:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h += ord(i)
        return h % self.Max

    def __setitem__(self, key, value):
        h= self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h= self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h= self.get_hash(key)
        self.arr[h] = None

if __name__ == "__main__":
    l= HashMap()
    print(l.get_hash("march 6"))
    l['march 10'] = 100
    l['march 6'] = 50
    print(l.arr)
    print(l['march 6'])
    del l['march 6']
    print(l.arr)
