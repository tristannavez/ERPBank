try:
    import common, ui, data_manager
except:
    from includes import *


def start_module(table_list, name_file):
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
            show_table(table, table_title, name_file)
        elif option[0] == "2":
            add(table, table_list, name_file)
        elif option[0] == "3":
            id_ = ui.get_inputs(["ID: "], "Quel est l'ID du produit a supprimer ? ")[0]
            table = remove(table, id_, name_file)
        elif option[0] == "4":
            show_table(table, table_title, name_file)
            id_ = ui.get_inputs(["ID: "], "Quel est l'ID du produit a mettre à jour ? ")[0]
            table = update(table, id_, name_file, table_title)
        elif option[0] == "0":
            exit()
        else:
            ui.print_error_message("Cette option n'existe pas !")


def show_table(table, table_title, name_file):
    table_title = ['id'] + table_title
    table = data_manager.get_table_from_file(name_file + ".csv")
    ui.print_table(table, table_title)


def add(table, table_list='', name_file='', test=''):
    wanna_stay = True
    while wanna_stay:

        if test == '':
            new_entry = ui.get_inputs(table_list, "Renseigner les informations : ")
            new_entry.insert(0, common.generate_random(table))
            next_step = ui.get_inputs([""], "Appuyez sur 0 pour enregistrer & sortir ou sur 1 pour ajouter")[0]
            table.append(new_entry)
            if next_step == "0":
                data_manager.write_table_to_file(name_file + ".csv", table)
        else:
            new_entry = test
            next_step = "0"
            table.append(new_entry)

        wanna_stay = False
    return table


'Fonction de suppression de données dans la table'


def remove(table, id_, name_file='', test=''):
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

        if test == '':
            next_step = ui.get_inputs([""], "Appuyez sur 0 pour sortir ou sur 1 pour supprimer")[0]
            if next_step == '0':
                data_manager.write_table_to_file(name_file + ".csv", table)
                wanna_stay = False
            else:
                id_ = ui.get_inputs(["Veuillez taper l'ID à supprimer : "], "\n")[0]
                continue
        else:
            next_step = 0
            wanna_stay = False
    return table


'Fonction de mise à jour des données dans la table'


def update(table, id_, name_file='', table_title='', test=''):
    wanna_stay = True
    current_iterates = 0
    compteur = 1
    'longeur verticale'
    max_iterates = len(table)
    while wanna_stay:
        for i, v in enumerate(table):
            if v[0] == id_:
                if test == '':
                    for y in table_title:
                        value_read = []
                        value_read = ui.get_inputs([""], "Veuillez donner une valeur pour -> " + y + " :")
                        v[compteur] = value_read[0]
                        compteur = compteur + 1

                else:
                    while compteur < len(test):
                        v[compteur] = test[compteur]
                        compteur = compteur + 1

            elif v[0] != id_ and current_iterates < max_iterates:
                current_iterates += 1

        if test == '':
            last_step = ui.get_inputs([""], "Pressez 0 pour quitter ou 1 pour en ajouter un revenir")[0]
            id_ = ui.get_inputs(["Veuillez renseigner l'ID du client à mettre à jour: "], "\n")[0]
            continue
            if last_step == '0':
                data_manager.write_table_to_file(name_file + ".csv", table)
                wanna_stay = False
        else:
            wanna_stay = False
    return table
