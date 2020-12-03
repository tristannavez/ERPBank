""" MODULE GESTION CLIENTS

Structure des données:
    * id (string)
    * n° compte (string): Numero du compte
    * montant (float): Solde du compte
    * dépense du mois (int) : dépense mois en cours
    * credit (bool) : crédit en cours ou non
    * remboursement credit (float) : montant du remboursement
"""

import ui
import data_manager
import common


def start_module():

    table = data_manager.get_table_from_file("gestion_comptes.csv")
    table_title = ["id", "n° compte", "montant", "dépense/mois", "crédit", "remboursement crédit"]

    list_options = ["Afficher les données",
                    "Ajouter un client",
                    "Supprimer un client",
                    "Mettre à jour les données"]

    ui.print_menu("Menu Gestion Comptes", list_options, "Sortir ->")

    while True:
        option = ui.get_inputs(["Merci de renseigner le n° correspondant : "], "")
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
    title_list = ["id", "n° compte", "montant", "dépense/mois", "crédit", "remboursement crédit"]
    table = data_manager.get_table_from_file("gestion_comptes.csv")
    ui.print_table(table, title_list)

'Fonction ajout de données dans la table'
def add(table):
    list_labels = ["N° compte : ", "Montant : ", "Dépense/mois : ", "Crédit : ", "Remboursement :"]
    wanna_stay = True
    while wanna_stay:
        new_product = ui.get_inputs(list_labels, "Renseigner les informations : ")
        new_product.insert(0, common.generate_random(table))
        table.append(new_product)
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour enregistrer & sortir ou sur 1 pour ajouter un nouveau client")[0]
        if next_step == "0":
            data_manager.write_table_to_file("gestion_comptes.csv", table)
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
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour sortir ou sur 1 pour supprimer un autre client")[0]
        if next_step == '0':
            data_manager.write_table_to_file("gestion_comptes.csv", table)
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
                first_step = ui.get_inputs([""], "Veuillez préciser ce que vous souhaitez modifier à l'indice donné. (N° compte,Montant,Dépense/mois,Crédit,Remboursement)")[0]
                if first_step == "n° compte":
                    new_number = ui.get_inputs([""], "Veuillez renseigner un nouveau n° compte!")
                    v[1] = new_number[0]
                elif first_step == "montant":
                    new_montant = ui.get_inputs([""], "Veuillez renseigner un nouveau montant!")
                    v[2] = new_montant[0]
                elif first_step == "depense":
                    new_depense = ui.get_inputs([""], "Veuillez donner une nouvelle depense (0 par défaut)!")
                    v[3] = new_depense[0]
                elif first_step == "credit":
                    new_credit = ui.get_inputs([""], "Veuillez renseigner si il y a un crédit en cours ( 0 | 1 )!")
                    v[4] = new_credit[0]
                elif first_step == "remboursement":
                    new_remb = ui.get_inputs([""], "Veuillez renseigner la somme rembourser s'il y en a une ( sinon mettre 0 )!")
                    v[5] = new_remb[0]
                else:
                    ui.print_error_message("Cette option n'existe pas !")
            elif v[0] != id_ and current_iterates < max_iterates:
                current_iterates += 1
            else:
                ui.print_error_message("Vous ne pouvez pas renseigner cette information !")
        last_step = ui.get_inputs([""], "Appuyez sur 0 pour sortir ou sur 1 pour mettre à jour un autre client .")[0]
        if last_step == '0':
            data_manager.write_table_to_file("gestion_comptes.csv", table)
            wanna_stay = False
        else:
            id_ = ui.get_inputs(["Veuillez renseigner l'ID du client à mettre à jour: "], "\n")[0]
            continue

    return table

