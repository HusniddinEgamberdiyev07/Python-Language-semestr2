# Incorrect inheritence but works

class hyder:
    def __init__(self,m,h):
        self.m=m
        self.h=h
        
    def hello(self):
        print(self.m)

    def bye(self):
        print(self.h)

class zafar(hyder):
    def __init__(self,m, h, zm,zh):
        self.zm=zm
        self.zh=zh
        self.m = m
        self.h = h

    def zjob(self):
        print(self.zm)
        print(self.zh)

x=zafar("1000$","Gagarin", "100$", "somehwere")
print(x.zm)
x.bye()

# Correct inheritence

class hyder2:
    def __init__(self,m,h):
        self.m=m
        self.h=h
        
    def hello(self):
        print(self.m)

    def bye(self):
        print(self.h)

class zafar2(hyder):
    def __init__(self,m, h, zm,zh):
        super().__init__(m, h)
        self.zm=zm
        self.zh=zh

    def zjob(self):
        print(self.zm)
        print(self.zh)

x2=zafar2("1000$","Gagarin", "100$", "somehwere")
print(x2.zm)
x2.bye()