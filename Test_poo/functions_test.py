import ui
import data_manager
import common

def start_module(table_list,name_file):
    """
    Commencement du module avec le choix des foncitons.

    Returns:
        None
    """

    table = data_manager.get_table_from_file(name_file + ".csv")
    table_title = table_list

    list_options = ["Afficher",
                    "Ajouter",
                    "Supprimer",
                    "Mettre à jour"]

    ui.print_menu("Menu test", list_options, "Sortir ->")
    while True:
        option = ui.get_inputs(["Merci de renseigner le n° correspondant"], "")
        if option[0] == "1":
            show_table(table,table_title,name_file)
        elif option[0] == "2":
            add(table,table_list,name_file)
        elif option[0] == "3":
            id_ = ui.get_inputs(["ID: "], "Quel est l'ID du produit a supprimer ? ")[0]
            table = remove(table, id_, name_file)
        elif option[0] == "4":
            show_table(table,table_title,name_file)
            id_ = ui.get_inputs(["ID: "], "Quel est l'ID du produit a mettre à jour ? ")[0]
            table = update(table, id_,name_file, table_title)
        elif option[0] == "0":
            exit()
        else:
            ui.print_error_message("Cette option n'existe pas !")




def show_table(table,table_title,name_file):
    table_title = ['id'] + table_title
    table = data_manager.get_table_from_file(name_file + ".csv")
    ui.print_table(table, table_title)


def add(table,table_list,name_file):
    wanna_stay = True
    while wanna_stay:
        new_entry = ui.get_inputs(table_list, "Renseigner les informations : ")
        new_entry.insert(0, common.generate_random(table))
        table.append(new_entry)
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour enregistrer & sortir ou sur 1 pour ajouter")[0]
        if next_step == "0":
            data_manager.write_table_to_file(name_file + ".csv", table)
            wanna_stay = False
    return table




'Fonction de suppression de données dans la table'
def remove(table,id_,name_file):
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
            data_manager.write_table_to_file(name_file + ".csv", table)
            wanna_stay = False
        else:
            id_ = ui.get_inputs(["Veuillez taper l'ID à supprimer : "], "\n")[0]
            continue
    return table


'Fonction de mise à jour des données dans la table'
def update(table, id_,name_file, table_title):
    table_title = ['id'] + table_title
    wanna_stay = True
    current_iterates = 0
    'longeur verticale'
    max_iterates = len(table)
    'longeur horizontale'
    max_values = len(table_title)
    while wanna_stay:
        for i, v  in enumerate(table):
            id_ = int(id_)
            print(table[id_])
            for i in table_title:
                values = ui.get_inputs([""], "Veuillez donner une valeur pour -> " + i + " :")

            last_step = ui.get_inputs([""], "Appuyez sur 0 pour sortir ou sur 1 pour mettre à jour un autre client .")[0]
            if last_step == '0':
                data_manager.write_table_to_file(name_file + ".csv", table)
                wanna_stay = False
            else:
                id_ = ui.get_inputs(["Veuillez renseigner l'ID du client à mettre à jour: "], "\n")[0]
                continue
    return table


