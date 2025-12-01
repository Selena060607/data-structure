"""
Text editor buffer

It is adapted from 1.3.44, Algorithms, 4th Edition, by Robert Sedgewick and Kevin Wayne.
"""
class EditorBuffer:
    def __init__(self):
        self.left_stack=[]
        self.right_stack=[]
        self.cursor=0
    def insert(self, c: str):
        """insert c at the cursor position"""
        assert len(c) == 1
        self.left_stack.insert(self.cursor, c)
        self.cursor += 1
    def delete(self):
        """delete and return the character at the cursor"""
        return self.left_stack.pop(self.cursor-1)
        self.cursor -= 1
    def move_left(self, k: int):
        """move the cursor k positions to the left"""
        if self.cursor - k < 0:
            for i in range(self.cursor):
                self.right_stack.insert(0, self.left_stack.pop())
            self.cursor = 0
        else:
            for i in range(k):
                self.right_stack.insert(0, self.left_stack.pop())
                self.cursor -= 1

    def move_right(self, k: int):
        """move the cursor k positions to the right"""
        if self.cursor + k > len(self.left_stack + self.right_stack):
            for i in range(len(self.left_stack + self.right_stack) - self.cursor):
                self.left_stack.append(self.right_stack.pop(0))
            self.cursor = len(self.left_stack + self.right_stack)
        else:
            for i in range(k):
                self.left_stack.append(self.right_stack.pop(0))
                self.cursor += 1

    def __len__(self):
        """number of characters in the buffer"""
        return len(self.left_stack+self.right_stack)

    def __str__(self):
        """string representation of the buffer"""
        return ''.join(self.left_stack) + '|' + ''.join(self.right_stack)

if __name__ == "__main__":
    """a demo usage of EditorBuffer"""
    buffer = EditorBuffer()
    buffer.insert("a")
    print(buffer)  # Print buffer state after inserting 'a'
    buffer.insert("b")
    print(buffer)  # Print buffer state after inserting 'b'
    buffer.insert("c")
    print(buffer)  # Print buffer state after inserting 'c'
    assert len(buffer) == 3
    buffer.move_left(1)
    print(buffer)  # Print buffer state after moving left by 1 position
    assert buffer.delete() == "b"
    print(buffer)  # Print buffer state after deleting 'b'