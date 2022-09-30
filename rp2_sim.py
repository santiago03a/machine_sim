
pins='pins'

class PIO():
    OUT_LOW=0
    

class StateMachine:
  def __init__(self, smnum, prog, freq=125000000, **kwargs):
      pass
      
  def active(self, x=None):
       pass

class nop:
    def __init__(self,*args, **kwargs):
        print('nop.__init__',args,kwargs)
        pass
     
    def __getitem__(self,name):
        print('nop.__getattr__',name)
        pass
        
class set(nop):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
  
class wrap(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
         
def asm_pio(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        print("Inside inner function")
        print("I like", kwargs['set_init']) 
        func()
    return inner
#@decorator(like = "geeksforgeeks")
#def my_func():
    #print("Inside actual function")
         
