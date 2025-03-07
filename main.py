# Imports

from menu import main_menu
from data_management import load_data, view_data, date_range, add_tran, edit_tran

#name
file_path = "sampledata.csv"
data = load_data(file_path)

# Art


# Application Loop


while True:

    # Choice verification
    main_menu()
    user_choice = input("Your Choice : ")
    if user_choice in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']:

        # Main choices
        if user_choice == '0':
            data = load_data(file_path)
            print("\033[32mCSV file imported successfully.\033[0m")
        elif user_choice == '1':
            view_data(data)
        elif user_choice == '2':
            date_range(data)
        elif user_choice == '3':
            add_tran(data)
        elif user_choice == '4':
            edit_tran(data)
        elif user_choice == '5':
            edit_tran(data)
        elif user_choice == '6':
            edit_tran(data)
        elif user_choice == '7':
            edit_tran(data)
        elif user_choice == '8':
            edit_tran(data)
        elif user_choice == '9':
            edit_tran(data)
        elif user_choice == '10':
            edit_tran(data)
        elif user_choice == '11':
            edit_tran(data)
        elif user_choice == '12':
            edit_tran(data)
        elif user_choice == '13':
            edit_tran(data)
        elif user_choice == '14':
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break  # Exit the program

    else:
        print("\033[31mInvalid choice! Please, try again.\033[0m")