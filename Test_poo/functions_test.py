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
        elif option[0] == "0":
            exit()
        else:
            ui.print_error_message("Cette option n'existe pas !")




def show_table(table,table_title,name_file):
    table_list_id = table_title
    table_list_id.insert(0,'id')
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

