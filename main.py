import sys
import CRUD.crud_functions
import CRUD.ui


def choose():
    list_test = ["name", "budget_donne", "budget_restant"]
    list_test2 = ["produit", "prix", "acheteur"]
    inputs = CRUD.ui.get_inputs(["Merci d'entrer le chiffre correspondant a ce que vous chercher: "], "")
    option = inputs[0]
    if option == "1":
        CRUD.crud_functions.start_module(list_test, "Gestion_Achat/Budget/Gestion_budgetaire")
    elif option == "2":
        CRUD.crud_functions.start_module(list_test2, "Gestion_Achat/Prix_Achat/Gestion_prix_achat")
    elif option == "0":

        sys.exit(0)
    else:
        raise KeyError("Ce n'est pas une option valable")


def handle_menu():
    options = ["Gestion budget",
               "Gestion des prix d'achat"]

    CRUD.ui.print_menu("Menu principal", options, "Sortir")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            CRUD.ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
