class OffsetMap:
    def __init__(self, keyOffset, valueOffset):
        self.keyOffset = 0
        self.valueOffset = 0
        self.offsetMap = {}

    def size(self):
        return len(self.offsetMap)

    def isEmpty(self):
        return not self.offsetMap

    def containsKey(self, key):
        keyNotOffset = key - self.keyOffset
        if keyNotOffset > 0:
            return True
        return False

    def containsValue(self, value):
        valueNotOffset = value - self.valueOffset
        if valueNotOffset > 0:
            return True
        return False
    
    def get(self, key):
        keyNotOffset = key - self.keyOffset
        value = self.offsetMap[keyNotOffset]
        if not value:
            return
        return value + self.valueOffset

    def put(self, key, value):
        keyNotOffset = key - self.keyOffset
        valueNotOffset = value - self.valueOffset
        
    def remove(self, key):
        keyNotOffset = key - self.keyOffset

    def addToValues(self, toAdd):
        self.valueOffset += toAdd

    def addtoKeys(self, toAdd):
        self.keyOffset += toAdd
    