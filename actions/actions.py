# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
f = open('data.json')
data = json.load(f)
f.close()


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
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict) -> Dict[Text, Any]:

        if slot_value.lower() not in data['prato'].keys():
            dispatcher.utter_message(text='Não temos pizza de ' + str(slot_value) + ' no cardápio')
            return {'pizzasabor': None}
        return {'pizzasabor': slot_value}

    def validate_tamanhopizza(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict) -> Dict[Text, Any]:

        if slot_value.lower() not in data['tamanhopizza']:
             dispatcher.utter_message(text='Não temos o tamanho ' + str(slot_value) + ' no cardápio')
             return {'tamanhopizza': None}
        return {'tamanhopizza': slot_value}

    def validate_bebida(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict) -> Dict[Text, Any]:

        if slot_value.lower() not in data['bebida']:
            dispatcher.utter_message(text='Não temos a bebida ' + str(slot_value) + ' no cardápio')
            return {'bebida': None}
        return {'bebida': slot_value}