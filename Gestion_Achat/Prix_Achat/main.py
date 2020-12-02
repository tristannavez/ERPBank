import ui
import gestion_prix_achat
import common

def choose():
    inputs = ui.get_inputs(["Merci d'entrer le chiffre correspondant a ce que vous chercher: "], "")
    option = inputs[0]
    if option == "1":
        gestion_prix_achat.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("Ce n'est pas une option valable")


def handle_menu():
    options = ["Gestion des prix d'achat"]

    ui.print_menu("Menu principal", options, "Sortir")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
