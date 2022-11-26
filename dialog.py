def choice_dialog(choices):
    print('Select score: ')
    selection = input()

    for idx, choice in enumerate(iter(choices)):
        print(f'{idx + 1}. {choice}: {choices[choice]}')

    for idx, choice in enumerate(iter(choices)):
        if int(selection) - 1 == idx:
            print(f'Selected: {choice}: {choices[choice]}')
            return choice


def select_score_dialog():
    pass
