import Crud
import CheeseView
import Controller

"""
CheeseWiz:  Final Project for CST8333 by Patty Mosher Dec 2019.

CRUD implemented with SQLite DB. Can restore to original CSV or export to new CSV, sort and filter by user's input.
"""
original_path = "D:\Level 4\Prog Lang Research\Dataset\canadianCheeseDirectory.csv"
path = "D:\Level 4\Prog Lang Research\Dataset"
headers = ['CheeseId', 'CheeseNameEn', 'ManufacturerProvCode', 'ManufacturingTypeEn', 'WebSiteEn', 'FatContentPercent',
           'MoisturePercent', 'ParticularitiesEn', 'FlavourEn', 'CharacteristicsEn', 'RipeningEn', 'Organic',
           'CategoryTypeEn', 'MilkTypeEn', 'MilkTreatmentTypeEn', 'RindTypeEn', 'LastUpdateDate']


CheeseView.display_menu()
choice = input('Please choose a number from 1-9:  ')

if choice is "1":
    Controller.load_data_from_csv(original_path)
    CheeseView.display_name()

elif choice is "2":
    CheeseView.enter_new_cheese()
    CheeseView.display_name()

elif choice is "3":
    CheeseView.display_all()
    CheeseView.display_name()

elif choice is "4":
    id = input('Enter CheeseId for record to display: ')
    CheeseView.pretty_print_list(headers)
    CheeseView.pretty_print_list(Crud.read_cheese_by_id(id))
    CheeseView.display_name()

elif choice is "5":
    cId = input('Enter CheeseId for record to update: ')
    col_name = input('Enter column name to update: ')
    new_val = input('Enter new value: ')
    Crud.update_cheese_by_id(col_name,new_val,cId)
    CheeseView.display_name()

elif choice is "6":
    cId = input('Enter CheeseId for record to delete: ')
    confirm = input("are you sure you want to delete record with CheeseId {}?".format(cId))
    if confirm.lower() is "y" or "yes":
        Crud.delete_cheese_by_id(cId)
    CheeseView.display_name()

elif choice is "7":
    new_fname = input('Enter new filename: ')
    fullpath = path + '\\' + new_fname
    Controller.write_data_to_csv(fullpath)
    print('File saved to ?'.format(fullpath))
    CheeseView.display_name()

elif choice is "8":
    Controller.sort_by()
    CheeseView.display_menu()

elif choice is "9":
    f = Controller.filtered()
    CheeseView.pretty_print_list(headers)
    for item in f:
        CheeseView.pretty_print_list(item)
    print("Returned {} records".format(len(f)))
    CheeseView.display_name()




