class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.bucket = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size
    
    def _resize(self):
        new_size = self.size * 2
        new_bucket = [[] for _ in range(new_size)]

        for bucket in self.bucket:
            for key, value in bucket:
                index = hash(key) % new_size
                new_bucket[index].append((key, value))

        self.size = new_size
        self.bucket = new_bucket

    def put(self, key, value):
        load_factor = self.count / self.size
        if load_factor > 0.7:
            self._resize()

        index = self._hash(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.bucket[index]

        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def contains_key(self, key):
        index = self._hash(key)
        bucket = self.bucket[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    def remove(self, key):
        index = self._hash(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

