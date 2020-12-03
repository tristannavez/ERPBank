import ui
import gestion_comptes
import common

def choose():
    inputs = ui.get_inputs(["Merci d'entrer le chiffre correspondant a ce que vous chercher : "], "")
    option = inputs[0]
    if option == "1":
        gestion_comptes.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("Ce n'est pas une option valable")


def handle_menu():
    options = ["Gestion des clients"]

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
