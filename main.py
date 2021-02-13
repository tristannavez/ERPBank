import sys
import CRUD.crud_functions
import includes.ui


def choose():
    ga_budget = ["name", "budget_donne", "budget_restant"]
    ga_commandes = ["Produit", "Date de commande", "Date de reception", "Quantite"]
    ga_prixachat = ["produit", "prix", "acheteur"]
    gf_comptagene = ["Agences", "M�nages", "Biens & services", "Societe", "Operations", "Ressources"]
    gf_comptes = ["name", "price", "old_sold", "new_sold"]
    gf_couts = ["Libelle", "Prix", "Quantite", "Montant"]
    gf_tva = ["Libelle", "TVA", "Pourcentage", "Categories"]
    crm_clients = ["name", "surname", "society", "country"]

    inputs = includes.ui.get_inputs(["Merci d'entrer le chiffre correspondant a ce que vous chercher: "], "")
    option = inputs[0]
    if option == "1":
        CRUD.crud_functions.start_module(ga_budget, "Gestion_Achat/Budget/Gestion_budgetaire")
    elif option == "2":
        CRUD.crud_functions.start_module(ga_commandes, "Gestion_Achat/Commandes/Gestion_commandes")
    elif option == "3":
        CRUD.crud_functions.start_module(ga_prixachat, "Gestion_Achat/Prix_Achat/Gestion_prix_achat")
    elif option == "4":
        CRUD.crud_functions.start_module(gf_comptagene, "Gestion_Finance/Comptabilite_generale/comptabilite_generale")
    elif option == "5":
        CRUD.crud_functions.start_module(gf_comptes, "Gestion_Finance/Comptes/gestion_comptes")
    elif option == "6":
        CRUD.crud_functions.start_module(gf_couts, "Gestion_Finance/Couts/gestion_couts")
    elif option == "7":
        CRUD.crud_functions.start_module(gf_tva, "Gestion_Finance/TVA/tva")
    elif option == "8":
        CRUD.crud_functions.start_module(crm_clients, "CRM/Clients/Gestion_client")

    elif option == "0":

        sys.exit(0)
    else:
        raise KeyError("Ce n'est pas une option valable")


def handle_menu():
    options = ["Gestion achat - Budget",
               "Gestion achat - Commandes",
               "Gestion achat - Prix d'achat",
               "Gestion finance - Comptabilite generale",
               "Gestion finance - Comptes",
               "Gestion finance - Couts",
               "Gestion finance - TVA",
               "CRM - Gestion client"]

    includes.ui.print_menu("Menu principal", options, "Sortir")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            includes.ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
