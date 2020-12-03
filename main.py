# Do not modify this file
# run this program (the ERP software) from the terminal from thd root directory of this project


import sys
import ui  # User Interface

from Gestion_Achat import Commandes
# Customer Relationship Management (CRM) module
from CRM import Clients
from Gestion_Achat import Commandes
# Data Analyser module



def choose():
    inputs = ui.get_inputs(["Veuillez saisir un nombre: "], "")
    option = inputs[0]
    if option == "1":
        store.start_module()
    elif option == "2":
        hr.start_module()
    elif option == "3":
        inventory.start_module()
    elif option == "4":
        accounting.start_module()
    elif option == "5":
        Gestion_commandes.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "7":
        data_analyser.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Data Analyser Module"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
