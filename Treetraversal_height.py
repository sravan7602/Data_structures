class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if data<self.data:
            if self.left==None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        elif data>self.data:
            if self.right==None:
                self.right=Node(data)
            else:
                self.right.insert(data)
    def infix(self,root):
        if root!=None:
            self.infix(root.left)
            print(root.data)
            self.infix(root.right)
def height(root):
    if root==None:
        return 0
    else:
        lh=height(root.left)
        rh=height(root.right)
    if lh>rh:
        return lh+1
    else:
        return rh+1
a=list(map(int,input().split()))
for i in range(len(a)):
    if i==0:
        o=Node(a[i])
    else:
        o.insert(a[i])
o.infix(o)
print(height(o))
