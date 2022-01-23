import os 
from cleanname import CleanName
from config import Config
paths = os.path.dirname(os.path.abspath(__file__))

def EstasPermitiado(update):
    
    configuracion = Config()

    if("@"+update.message.chat.username == configuracion.arroba):

        return True

    else:
        
      return False   

    pass
