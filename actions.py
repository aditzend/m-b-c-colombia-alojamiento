# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.slots import Slot

import requests
import json

WS_URL_BASE = "https://preesb.compensarsalud.com/esb.preproduccion.consorcio/WSCOMEPS_rst_serviceagent/"
WS_TOKEN = "?sApl=SWPR136&sXml="
WS_METHOD_NAME ="Afiliado"
_HEADERS = {'Accept':'application/json'}




class custAction_Afiliaciones_ConsultarCategoriaXIdentificacion(Action):

    def name(self):
        return "custAction_Afiliaciones_ConsultarCategoriaXIdentificacion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,domain):
        identificacion = '84088570'#tracker.latest_message.get('text')

        STRING_XML = "<Afiliado>"
        STRING_XML = STRING_XML + "<IDAfiliado>"+identificacion+"</IDAfiliado>"
        STRING_XML = STRING_XML + "<TIDAfiliado>1</TIDAfiliado>"
        STRING_XML = STRING_XML + "<Opcion>22</Opcion>"
        STRING_XML = STRING_XML + "</Afiliado>" 
        response = requests.get(WS_URL_BASE + WS_METHOD_NAME + WS_TOKEN + STRING_XML , headers=_HEADERS)
        json_person = response.json()     

        return [SlotSet("nombreCompleto", json_person['DsAfiliado']['Afiliado']['Nombre'] + " " + json_person['DsAfiliado']['Afiliado']['PrimerApellido']),
                SlotSet("identificacion", json_person['DsAfiliado']['Afiliado']['IdAfiliado']),
                SlotSet("celular", json_person['DsAfiliado']['Afiliado']['Celular']),
                SlotSet("direccion", json_person['DsAfiliado']['Afiliado']['Direccion'])]
