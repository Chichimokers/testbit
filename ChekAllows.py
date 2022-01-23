import os 
from cleanname import CleanName
from config import arroba
paths = os.path.dirname(os.path.abspath(__file__))

def EstasPermitiado(update):

    if("@"+update.message.chat.username == arroba):
        return True

    else:
        
      return False   

    pass
