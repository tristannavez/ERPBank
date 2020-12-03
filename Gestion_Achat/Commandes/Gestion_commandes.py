""" Sales module

Data table structure:
    * id (string): Identifiant unique généré aléatoirement
    * produit (string): nom des produits
    * Date de commande (number): Date démission de la commande
    * Date de réception (number): Date à laquelle il a été reçu
    * Quantité (number): nombre d'unité par produit

"""


# Interface utilisateur
from Gestion_Achat.Commandes import ui
# gestion des données
import data_manager
# module commun
import common


def getMax(list):
    maxElement = list[0]
    for elements in list:
        if elements > maxElement:
            maxElement = elements
    return maxElement


def start_module():
    """
     Lance ce module et affiche son menu.

     """
    table = data_manager.get_table_from_file("Gestion_commandes.csv.csv")
    table_title = ["id", "produit", "date de commande", "date de reception", "quantité"]

    list_options = ["Afficher",
                    "Ajouter",
                    "Supprimer"]

    ui.print_menu("Module Menu Commande:", list_options, "Sortir ")
    while True:
        option = ui.get_inputs(["Veuillez rentrez un nombre"], "")
        if option[0] == "1":
            display_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            id_ = ui.get_inputs(["ID: "], "Veuillez saisir l'ID du produit à retirer: ")[0]
            table = remove(table, id_)
        elif option[0] == "0":
            exit()
        else:
            ui.print_error_message("Cette option n'existe pas!")


def display_table(table):
    """
    Afficher toute  la table
    """

    title_list = ["id", "produit", "date de commande", "date de reception", "quantité"]
    table = data_manager.get_table_from_file("Gestion_commandes.csv")
    ui.print_table(table, title_list)

def add(table):
    """
    Demander à l'utilisateur d'ajouter une commande

    """

    list_labels = ["id", "produit", "date de commande", "date de reception", "quantité"]
    wanna_stay = True
    while wanna_stay:
        new_product = ui.get_inputs(list_labels, "Fournissez l'information de la commande")
        new_product.insert(0, common.generate_random(table))
        table.append(new_product)
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour sauvegarder & exit ou 1 to ajouter une autre commande.")[0]
        if next_step == "0":
            data_manager.write_table_to_file("Gestion_commandes.csv", table)
            wanna_stay = False
    return table

def remove(table, id_):
    """
   Supprime un enregistrement

    """

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
                ui.print_error_message("Aucune donnée avec cet ID!")
        next_step = ui.get_inputs([""], "Appuyez sur 0 pour sauvegarder & exit ou 1 to ajouter une autre commande.")[0]
        if next_step == '0':
            data_manager.write_table_to_file("Gestion_commandes.csv", table)
            wanna_stay = False
        else:
            id_ = ui.get_inputs(["Veuillez saisir l'ID de la commande à retirer: "], "\n")[0]
            continue
    return table

