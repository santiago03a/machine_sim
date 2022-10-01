def asm_pio(*args, **kwargs):
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador
'''asm_pio es una funcion en la cual entran dos parametros, args y kwargs, los cuales permiten pasar un número variable de argumentos a una
funcion, pero al especificar arg viene de argumentos y son parámetros de entrada de una función, en el caso de kwargs permite pasar argumentos
de longitud variable asociados con un nombre o key a una función, en esta funcion se define el decorador, en el cual entra el programa, y posteriormente
se define el compilador en el cual se imprime el programa y retornan las funciones'''
def decorador_instr(fun_inst):
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'
'''decorador_instr es una funcion decorador en la cual esta entrando la funcion fun_inst, dentro de la cual
esta un decorador de esa funcion de entrada con otros parametros de la funcion que entro al decorador, dentro de
la cual se llama al self que permite ejecutar las variables y las funciones, para posteriormente ser ejcutada y retornada'''
class PIO():
    OUT_LOW='PIO.OUT_LOW'
    
'''clase en la cual se definen los pines y su valor de entrada'''
class StateMachine:
'''clase dentro la cual tienen unas funciones'''
  def __init__(self, id_, program, freq=125000000, **kwargs):
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
'''____init__ es una funcion a la cual la cual tienen ciertos parametros de entradas, algunos definidos con un valor,
se definen dos varibles '''
        
  def active(self, x=None):
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def __getitem__(self,name):
        #print('nop.__getattr__',name)
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
         
         
