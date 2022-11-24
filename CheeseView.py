"""
Display module designed to be used with CheeseWiz.py

Written by Patty Mosher
"""
# import CheeseWiz
import Crud
import datetime

headers = ['CheeseId', 'CheeseNameEn', 'ManufacturerProvCode', 'ManufacturingTypeEn', 'WebSiteEn', 'FatContentPercent',
           'MoisturePercent', 'ParticularitiesEn', 'FlavourEn', 'CharacteristicsEn', 'RipeningEn', 'Organic',
           'CategoryTypeEn', 'MilkTypeEn', 'MilkTreatmentTypeEn', 'RindTypeEn', 'LastUpdateDate']


def pretty_print_list(list):
    """Prints a list a little prettier. Intended for headers/rows of data"""
    s = ''
    for item in list:
        s = s + str(item) + " "*(30 - len(str(item))) + " | "
    print(s)


def display_menu():
    """Displays the Menu, and returns user's selection"""
    print('***************************************************************')
    print('* Menu                                | Patty Mosher Fall2019 *')
    print('*  ---------------------------------------------------------- *')
    print('* 1. Reload data from original csv file                       *')
    print('* 2. Create new cheese record                                 *')
    print('* 3. Display all records                                      *')
    print('* 4. Display a single record                                  *')
    print('* 5. Update a record                                          *')
    print('* 6. Delete a record                                          *')
    print('* 7. Save data to a new csv file                              *')
    print('* 8. Sort data                                                *')
    print('* 9. Filter data by multiple headers                          *')
    print('***************************************************************')


def enter_new_cheese():
    """Prompts user for input and creates a new cheese entry in the database."""
    print('--------------------------------------------------------------')
    cheeseId = input('Enter the Cheese Id: ')
    nm = input('Enter the Cheese Name: ')
    prov = input('Enter the Manufactuerer Province Code: ')
    m_type = input('Enter the Manufacturing Type: ')
    web = input('Enter the webiste: ')
    fat = input('Enter the Fat Content Percent: ')
    moist = input('Enter the Moisture Precent: ')
    part = input('Enter the Particularities: ')
    flvr = input('Enter the Flavour: ')
    chrtr = input('Enter the Characteristics: ')
    ripe = input('Enter the Ripening: ')
    org = input('Is it organic? (0 no, 1 yes): ')
    cat = input('Enter the Category Type: ')
    milk_typ = input('Enter the Milk Type: ')
    milk_treat = input('Enter the Milk Treatment Type: ')
    rind = input('Enter the Rind Type: ')
    date = datetime.datetime.now()
    print('--------------------------------------------------------------')
    Crud.create_cheese(cheeseId, nm, prov, m_type, web, fat, moist, part, flvr, chrtr, ripe, org, cat, milk_typ, milk_treat, rind, date)


def display_name():
    """Displays author's name"""
    print('------------------------------------------------- Patty Mosher')


def display_all():
    """Displays all of the records in the database"""
    pretty_print_list(headers)
    records = Crud.read_all()
    for record in records:
        pretty_print_list(record)