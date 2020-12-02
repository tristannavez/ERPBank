""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    col_width = list()

    for i, title in enumerate(title_list):
        col_width.append(len(title))

    for items in table:
        for i, item in enumerate(items):
            try:
                if col_width[i] < len(str(item)):
                    col_width[i] = len(str(item))
            except:
                col_width.append(len(item))

    table_size = 1
    for dash in col_width:
        table_size += (dash + 3)
    print("|", end="")
    for i, title in enumerate(title_list):
        
        print('{:{width}} |'.format(title, width=col_width[i]), end="")

    print('\n' + '|' + ('-' * (table_size-7)) + '|')
    
    for items in table:
        for i, item in enumerate(items):
            if i == 0: 
                print('|', end="")
            print('{:{width}} |'.format(item, width=col_width[i]), end="")
        print()


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result
    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(label, ":\n", result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    number = 1
    print("\t", title)
    for i in list_options:
        print("\t\t ({})".format(number), i)
        number += 1
    print("\t\t (0)", exit_message)
    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)
    for element in list_labels:
        x = input(element)
        inputs.append(x)

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(message)
