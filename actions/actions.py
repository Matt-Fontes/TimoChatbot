# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# import json
# f = open('data.json')

from typing import Any, Text, Dict, List

from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# class ActionIngredientes(Action):

#     def name(self) -> Text:
#         return "action_ingredientes"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         data = json.load(f)
#         str = ''.join(data['prato'][tracker.get_slot('pedido')]['ingredientes'])

#         dispatcher.utter_message(text=str)

#         return []

class ValidatePizza(FormValidationAction):

    def name(self) -> Text:
        return "validate_order_form"

    def validate_pizzasabor(
        self,
        dispatcher: CollectingDispatcher,
        slot_value: Any,
        tracker: Tracker,
        domain: DomainDict) -> Dict[Text, Any]:

        data = json.loads(f)
        # dispatcher.utter_message(text='passei aqui pizza')
        if slot_value.lower() not in data.pratos.keys():
            dispatcher.utter_message(text='Não temos pizza de {slot_value} no cardápio')
            return {'pizzasabor': None}
        return {'pizzasabor': slot_value}

    def validate_tamanhopizza(
        self,
        dispatcher: CollectingDispatcher,
        slot_value: Any,
        tracker: Tracker,
        domain: DomainDict) -> Dict[Text, Any]:
        dispatcher.utter_message(text='passei aqui tamanho')
        # data = json.loads(f)

        # if slot_value.lower() not in data.tamanhopizza:
        #     dispatcher.utter_message(text='Não temos o tamanho {slot_value} no cardápio')
        #     return {'tamanhopizza': None}
        return {'tamanhopizza': slot_value}

    def validate_bebida(
        self,
        dispatcher: CollectingDispatcher,
        slot_value: Any,
        tracker: Tracker,
        domain: DomainDict) -> Dict[Text, Any]:
        dispatcher.utter_message(text='passei aqui bebida')
        # data = json.loads(f)

        # if slot_value.lower() not in data.bebida:
        #     dispatcher.utter_message(text='Não temos a bebida {slot_value} no cardápio')
        #     return {'bebida': None}
        return {'bebida': slot_value}