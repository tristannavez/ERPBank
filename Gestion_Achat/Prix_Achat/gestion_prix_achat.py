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


'Fonction afficher les données de la table'
def show_table(table):
    title_list = ["id", "produit", "prix", "acheteur"]
    table = data_manager.get_table_from_file("Prix_Achat/Gestion_prix_achat.csv")
    ui.print_table(table, title_list)

'Fonction ajout de données dans la table'
def add(table):
    list_labels = ["produit : ", "prix : ", "acheteur : "]
    wanna_stay = True
    while wanna_stay:
        new_product = ui.get_inputs(list_labels, "Renseigner les informations : ")
        new_product.insert(0, common.generate_random(table))
        table.append(new_product)
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour enregistrer & sortir ou sur 1 pour ajouter un nouveau produit")[0]
        if next_step == "0":
            data_manager.write_table_to_file("Prix_Achat/Gestion_prix_achat.csv", table)
            wanna_stay = False
    return table


'Fonction de suppression de données dans la table'
def remove(table, id_):
    wanna_stay = True
    current_iterates = 0
    max_iterates = len(table)
    while wanna_stay:
        for i, v in enumerate(table):
            if v[0] == id_:
                table.remove(table[i])
            elif v[0] != id_ and current_iterates < max_iterates:
                current_iterates += 1
            else:
                ui.print_error_message("Il y a pas d'ID correspondant !")
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour sortir ou sur 1 pour supprimer un autre produit")[0]
        if next_step == '0':
            data_manager.write_table_to_file("Prix_Achat/Gestion_prix_achat.csv", table)
            wanna_stay = False
        else:
            id_ = ui.get_inputs(["Veuillez taper l'ID à supprimer : "], "\n")[0]
            continue
    return table


'Fonction de mise à jour des données dans la table'
def update(table, id_):
    wanna_stay = True
    current_iterates = 0
    max_iterates = len(table)
    while wanna_stay:
        for i, v in enumerate(table):
            if v[0] == id_:
                first_step = ui.get_inputs([""], "Veuillez préciser ce que vous souhaitez modifier à l'indice donné. (produit, prix, acheteur)")[0]
                if first_step == "produit":
                    new_product = ui.get_inputs([""], "Veuillez donner un nouveau produit!")
                    v[1] = new_product[0]
                elif first_step == "prix":
                    new_price = ui.get_inputs([""], "Veuillez donner un nouveau prix!")
                    v[2] = new_price[0]
                elif first_step == "acheteur":
                    new_buyer = ui.get_inputs([""], "Veuillez donner un nouvel acheteur!")
                    v[3] = new_buyer[0]
                else:
                    ui.print_error_message("Cette option n'existe pas !")
            elif v[0] != id_ and current_iterates < max_iterates:
                current_iterates += 1
            else:
                ui.print_error_message("You can't add an item because of some reasons!")
        last_step = ui.get_inputs([""], "Press 0 to exit or 1 to update another item.")[0]
        if last_step == '0':
            data_manager.write_table_to_file("sales/sales.csv", table)
            wanna_stay = False
        else:
            id_ = ui.get_inputs(["Please type an ID to update the item at the given ID: "], "\n")[0]
            continue

    return table

