import json


from telegram.update import Update

from todus3.client import ToDusClient

from todus3.main import split_upload

import os 

from nubapi import NubApi

from telegram import ChatAction, bot, chat, message

def UploadFile(final,name,update,multiple :bool,nube :NubApi,context):
    
       #split_upload(clienteTodus,token,final,10000006,100)

        # if os.path.isfile(listo):
        #     with open(listo,'rb') as txtorigen:
        #         with open(paths+"//"+nombre+".txt",'wb')as desiton:
        #             shutil.copyfileobj(txtorigen,desiton)    
        # 
       filepath = name+".json" 

       respuesta = ""

       respuesta = nube.UploadFile(final,update=update)

       if(multiple==False):

              if(respuesta != "error"):

                 fichero = open(filepath,"w")

                 fichero.write(str(respuesta))  
     
                 fichero.close()

                 er = json.loads(respuesta)

                 update.message.reply_text(str(er["url"]))

                 print("Archivo Copiado")
 
                 update.message.chat.send_action(action=ChatAction.UPLOAD_DOCUMENT,timeout = 5)
 
                 print("Se a enviado " + filepath)

                 update.message.chat.send_document(document = open(filepath,"rb"))

                 #context.bot.send_message(chat_id='-647544571',text=)
                 
            
                 if(os.path.exists(final)):

                     os.remove(final)

                 if(os.path.exists(filepath)):

                     os.remove(filepath)

                 print(os.listdir("//"))
                 
               
                 update.message.reply_text("✅Operacion Finalizada✅")
               
              else:
                     print(os.listdir("//"))

                     nubea = NubApi()

                     update.message.reply_text("😭Fallo la subida de el archivo " +name+ " y se subira de nuevo😭")
                     
                     UploadFile(final,name,update,False,nubea,context=context)



       else:
              if(respuesta != "error"):

                  if(os.path.exists(final)):
                         
                       print("Existe y se removera")

                       print(os.listdir("//"))

                       os.remove(final)
                  else:
                      print("ya el archivo no existe")   

                      print(os.listdir("//"))


                  return respuesta

              else:


                  update.message.reply_text("Fallo la subida de el archivo " +name)

                  if(os.path.exists(final)):
                         
                       print("Existe")

                       print(os.listdir("//"))

                  else:
                      print("No existe")   

                      print(os.listdir("//"))

                  return respuesta

       pass