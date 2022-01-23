from config import Config
from datetime import time

import urllib

import telegram

from telegram.bot import Bot

from TareaFinalizable import StoppableThread

import threading

from typing import ContextManager, List, Text

from telegram import update

from FuncionesBot import CancelarTarea

from telegram.files.document import Document

import os

import todus3

from urllib import parse

from telegram.ext import CommandHandler,Updater , MessageHandler

from telegram.ext.conversationhandler import ConversationHandler

from telegram.ext.filters import Filters, MessageFilter

from telegram import ChatAction, chat, message

from telegram.update import Update

from todus3.client import ToDusClient

import shutil

from tokenmanage import searchToken

import requests

import time

import re 

import bs4

from os.path import basename

from ChekAllows import EstasPermitiado

from FuncionesBot import DisallowUser ,ProcesartxtdeYoutube,DescargarVideodeYoutube,Agregarusuario,ProcesarDescargadeunFichero,DowlandFromTxt

Entrada_de_la_Descaraga = 0 

ChangeToken = 1

Dowlandtxt = 100

Dowland_Trance = 5

youtubetxt = 6


paths = os.path.dirname(os.path.abspath(__file__))

def ProcessYutubetxt(update,context):
 

 ProcesartxtdeYoutube(update=update,context=context)

 return ConversationHandler.END

 pass

def ProccesYoutubeDowland(update,context):

    DescargarVideodeYoutube(update=update,context=context)

    return ConversationHandler.END

    pass

def Dowland(update,context):

    #Downland entry point

    print("/dowland  fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):


     update.message.reply_text("Envie el enlace")

     return Entrada_de_la_Descaraga

    else :

        update.message.reply_text("No estas autorizado para utilizar este bot")
  
    pass

def start(update,context):
    #init Handler

    print("/start fue utilizado por @"+str(update.message.chat.username))

    print(update)

    print(context)

    if(EstasPermitiado(update=update)):

        update.message.reply_text("Utilize /dowland y luego instrodusca un url valido")

    else:

        update.message.reply_text("No estas autorizado para usar este bot")


    pass
    #Downland action
    
def ChangeTokens(update,context):

    print("/token fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

      update.message.reply_text("Introdusca el nuevo token")

      return ChangeToken

    else:

      update.message.reply_text("No estas autorizado para usar este bot")

    pass

def processtoken(update,token):

    print("Cambio el token @"+str(update.message.chat.username))

    _tokenfinal = update.message.text

    return ConversationHandler.END

    pass

#Dowland youtube videos from txt list
def Youtubetxt(update,context):
    
    print("/youtubetxt fue utilizado por @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

      update.message.reply_text("Envie un txt con los enlaces")

      return youtubetxt

    else:

         update.message.reply_text("No estas autorizado para usar este bot")
       
    pass


def AddUser(update,context):

    Agregarusuario(update=update,context=context)
   
    return ConversationHandler.END
    
    pass

def downloadTxt(update,conext):

    print("/dowlandtxt fue utilizado por  @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el archivo con los enlaces")

     return Dowlandtxt

    else:

     update.message.reply_text("No estas autorizado para usar este bot")

    pass

CancelTrace = 56

def Cancelartareas(update,context):

    print("/cancel fue utilizado por  @"+str(update.message.chat.username))

    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el ID de su descarga")

     return CancelTrace

    else:

     update.message.reply_text("No estas autorizado para usar este bot")
    pass

def DowlandYoutubeVideo(update,context):
#Youtube dowland entry point
    
    print("/youtube fue utilizado por  @"+str(update.message.chat.username))
    
    if(EstasPermitiado(update=update)):

     update.message.reply_text("Envie el enlace del video de youtube")

     return Dowland_Trance

    else:

     update.message.reply_text("No estas autorizado para usar este bot")

    pass

def main():


        configuracion = Config()
        print("Cargando Configuracion")

        print("Listening.....")  

   
        update = Updater(token=configuracion.apibot,use_context=True)

        despachador =  update.dispatcher
        

        despachador.add_handler(CommandHandler('start',start))
        
        despachador.add_handler(ConversationHandler(

        entry_points=
        [
    
            CommandHandler('dowland',Dowland),
            CommandHandler('token',ChangeTokens),
            CommandHandler('youtube',DowlandYoutubeVideo),
            CommandHandler('youtubetxt',Youtubetxt),
            CommandHandler('Dowlandtxt',downloadTxt),
            CommandHandler('cancel',Cancelartareas),

        ],
        states=
        {
            ChangeToken: [MessageHandler(Filters.text,processtoken)],
            Entrada_de_la_Descaraga: [MessageHandler(Filters.text,proccesrequest)],
            Dowland_Trance :[MessageHandler(Filters.text,ProccesYoutubeDowland)],
            youtubetxt:[MessageHandler(Filters.document,ProcessYutubetxt)],
            Dowlandtxt:[MessageHandler(Filters.document,DowlandFromTxt)],
            CancelTrace:[MessageHandler(Filters.text,CancelarTarea)]
        },
        
        fallbacks=[]

    ))
       
        print("Listo para descargar")

        update.start_polling()
      
        update.idle() 
     
        pass  
        
def proccesrequest(update,context):

    ProcesarDescargadeunFichero(update=update,context=context)
    
    return ConversationHandler.END

if __name__ == "__main__":
      main()