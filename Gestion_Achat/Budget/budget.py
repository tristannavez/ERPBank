""" GESTION BUDGET

Structure des données:
    * id (string)
    * name (string)
    * budget_donne (number)
    * budget_restant (string)
"""

import ui
import data_manager
import common

def start_module():
    """
    Commencement du module avec le choix des foncitons.

    Returns:
        None
    """

    table = data_manager.get_table_from_file("Gestion_budgetaire.csv")
    table_title = ["id", "name", "budget_donne", "budget_restant"]

    list_options = ["Afficher",
                    "Ajouter",
                    "Supprimer",
                    "Mettre à jour"]

    ui.print_menu("Menu gestion budget", list_options, "Sortir ->")
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
    title_list = ["id", "name", "budget_donne", "budget_restant"]
    table = data_manager.get_table_from_file("Gestion_prix_achat.csv")
    ui.print_table(table, title_list)

'Fonction ajout de données dans la table'
def add(table):
    list_labels = ["name : ", "budget_donne : ", "budget_restant : "]
    wanna_stay = True
    while wanna_stay:
        new_entry = ui.get_inputs(list_labels, "Renseigner les informations : ")
        new_entry.insert(0, common.generate_random(table))
        table.append(new_entry)
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour enregistrer & sortir ou sur 1 pour ajouter")[0]
        if next_step == "0":
            data_manager.write_table_to_file("Gestion_budgetaire.csv", table)
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
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour sortir ou sur 1 pour supprimer")[0]
        if next_step == '0':
            data_manager.write_table_to_file("Gestion_budgetaire.csv", table)
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
                first_step = ui.get_inputs([""], "Veuillez préciser ce que vous souhaitez modifier à l'indice donné. (name, budget_donne, budget_restant)")[0]
                if first_step == "produit":
                    new_name = ui.get_inputs([""], "Saisir name")
                    v[1] = new_name[0]
                elif first_step == "prix":
                    new_budgetd = ui.get_inputs([""], "Saisir budget_donne")
                    v[2] = new_budgetd[0]
                    new_budgetr = ui.get_inputs([""], "Saisir budget_restant")
                    v[3] = new_budgetr[0]
                else:
                    ui.print_error_message("Cette option n'existe pas !")
            elif v[0] != id_ and current_iterates < max_iterates:
                current_iterates += 1
            else:
                ui.print_error_message("Vous ne pouvez pas ajouter l'item pour plusieurs raisons !")
        last_step = ui.get_inputs([""], "Pressez 0 pour quitter ou 1 pour en ajouter un revenir")[0]
        if last_step == '0':
            data_manager.write_table_to_file("Gestion_budgetaire.csv", table)
            wanna_stay = False
        else:
            id_ = ui.get_inputs(["Saisir un ID "], "\n")[0]
            continue

    return table
