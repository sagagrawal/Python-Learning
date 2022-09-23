class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class Stack:
    def __init__(self, maxsize):
        self.head = None
        self.size = 0
        self.maxsize = maxsize
    
    def isFull(self) -> bool:
        return self.size == self.maxsize
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def pop(self) -> int:
        if self.isEmpty():
            raise Exception("Trying to pop out of a empty stack")
        else:
            if self.size == 1:
                res = self.head.key
            else:
                    
                tmp = self.head
                while tmp.next.next:
                    tmp = tmp.next
                
                res = tmp.next.key
                tmp.next = None
            self.size -= 1
            
            return res
    
    def push(self, key: int):
        if self.isFull():
            raise Exception("Stack is full, cannot push new element")
        else:
            newNode = Node(key)
            if self.isEmpty():
                self.head = newNode
            else:
                tmp = self.head
            
                while tmp.next:
                    tmp = tmp.next
            
                tmp.next = newNode
            self.size += 1
        
    def peek(self) -> int:
        if self.isEmpty():
            raise Exception("Trying to pop out of a empty stack")
        else:
            tmp = self.head
            
            while tmp.next:
                tmp = tmp.next
            
            return tmp.key
            
if __name__ == "__main__":
    st = Stack(5)
    print(st.isEmpty())
    print(st.isFull())
    for i in range(1, 6):
        st.push(list(range(i,8)))
    
    print(st.isFull())
    print(f"Peek: {st.peek()}")
    
    while not st.isEmpty():
        print(st.pop())
    
    print(st.isEmpty())
            
