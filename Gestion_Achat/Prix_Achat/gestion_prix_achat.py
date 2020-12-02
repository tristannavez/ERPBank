""" MODULE GESTION PRIX ACHAT

Structure des données:
    * id (string)
    * produit (string): Produit acheté
    * prix (number): Prix du produit
    * acheteur (string): Acheteur du produit
"""


def start_module():
    """
    Commencement du module avec le choix des foncitons.

    Returns:
        None
    """

    table = data_manager.get_table_from_file("Prix_Achat/Gestion_prix_achat.csv")
    table_title = ["id", "produit", "prix", "acheteur"]

    list_options = ["Afficher les données",
                    "Ajouter un produit",
                    "Supprimer un produit",
                    "Mettre à jour les données"]

    ui.print_menu("Menu prix achat", list_options, "Sortir ->")
    while True:
        option = ui.get_inputs(["Merci de renseigner le n° correspondant"], "")
        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            id_ = ui.get_inputs(["ID: "], "Quel est l'ID du produit a supprimer ? ")[0]
            table = remove(table, id_)
        elif option[0] == "4":
            id_ = ui.get_inputs(["ID: "], "Quel est l'ID du produit a mettre à jour ? ")[0]
            table = update(table, id_)
        elif option[0] == "0":
            exit()
        else:
            ui.print_error_message("Cette option n'existe pas !")
