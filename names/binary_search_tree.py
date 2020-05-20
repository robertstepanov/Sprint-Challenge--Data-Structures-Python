class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right != None:
                return self.right.contains(target)
        elif target < self.value:
            if self.left != None:
                return self.left.contains(target)
        else:
            return False

    def get_max(self):
        if self.right == None:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
