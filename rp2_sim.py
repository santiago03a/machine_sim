def asm_pio(*args, **kwargs):
    def decorador(programa):
        print("Inside decorator")
        def compilador():
            print("Inside inner function")
            print("I like", kwargs) 
            programa()
            return None
        return compilador
    return decorador



#lista_instr=[]
def decorador_instr(fun_inst):
    # global 
    def decoracion_instr(self,*args, **kwargs):
        #global lista_instr
        instr1=fun_inst(self,*args, **kwargs)
        #lista_instr.append(instr1)
        return None #instr1
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
        global sm_iniciandoce,fsms
        sm_iniciandoce=self
        print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('lista_instr',self.lista_instr)
        sm_iniciandoce=None
        fsms[id_]=self
        pass
      
#   def add_instr(self):
#      self.lista_instr
        
  def active(self, x=None):
       pass
fsms=[None]*8

sm_iniciandoce=None

# class Instruc():
#     def __init__(self):
#         pass



# @decorador_instr
# def nop():
#     return'nop'
    
# @decorador_instr
# def set():
#     return'set'
    
# #@decorador_instr
# def wrap_target():
#     return'wrap_target'
    
# @decorador_instr
# def wrap():
#     return'wrap'
    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        global sm_iniciandoce
        print(self.__class__.__name__,'nop.__init__',args,kwargs)
        sm_iniciandoce.lista_instr.append(self)
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
         
#@decorator(like = "geeksforgeeks")
#def my_func():
    #print("Inside actual function")
         
