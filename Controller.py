import Crud
import csv
import CheeseView

headers = ['CheeseId', 'CheeseNameEn', 'ManufacturerProvCode', 'ManufacturingTypeEn', 'WebSiteEn', 'FatContentPercent',
           'MoisturePercent', 'ParticularitiesEn', 'FlavourEn', 'CharacteristicsEn', 'RipeningEn', 'Organic',
           'CategoryTypeEn', 'MilkTypeEn', 'MilkTreatmentTypeEn', 'RindTypeEn', 'LastUpdateDate']


def load_data_from_csv(path):
    """Opens CSV file located at path, creates SQLite database, initializes table, and loads data into database"""
    Crud.drop_table()
    Crud.init_db()
    with open(path, 'r', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            Crud.create_cheese(row['CheeseId'], row['CheeseNameEn'], row['ManufacturerProvCode'],
                               row['ManufacturingTypeEn'], row['WebSiteEn'], row['FatContentPercent'],
                               row['MoisturePercent'], row['ParticularitiesEn'], row['FlavourEn'], row['CharacteristicsEn'],
                               row['RipeningEn'], row['Organic'], row['CategoryTypeEn'], row['MilkTypeEn'],
                               row['MilkTreatmentTypeEn'], row['RindTypeEn'], row['LastUpdateDate'])
    print('Finished reloading data.')


def write_data_to_csv(path):
    """Writes data from database into a CSV file at path"""
    with open(path, 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        records = Crud.read_all()
        for record in records:
            writer.writerow(record)


def sort_by():
    """Sorts data by user input"""
    records = Crud.read_all()
    CheeseView.display_name()
    print('You can enter "Cheese Name", "Flavor", "Category", or "Milk Type"')
    sort_by = input('What column would you like to sort by?')
    if sort_by.lower()=="cheese name": sort_int = 1
    elif sort_by.lower()=="flavor": sort_int = 8
    elif sort_by.lower() == "category": sort_int = 12
    elif sort_by.lower() == "milk type": sort_int = 13
    else:
        print("Invalid option, sorting by CheeseId")
        sort_int = int(0)
    records.sort(key=lambda x: x[sort_int])
    CheeseView.pretty_print_list(headers)
    for record in records:
        CheeseView.pretty_print_list(record)
    CheeseView.display_name()


def filtered():
    """Allows user to enter multiple search criteria and returns list of matching results from database"""
    sorted_by = "SELECT * FROM cheeses WHERE "
    n = int(input("How many columns would you like to filter by?  "))
    i = 1
    sorted_by = sorted_by
    col = (input("Column name to filter:  "))
    val = (input("Value for {}:  ".format(col)))
    sorted_by = sorted_by + col + ' LIKE ' + '"%' + val + '%"'
    while n > i:
        col = (input("Column name to filter:  "))
        val = (input("Value for {}:  ".format(col)))
        sorted_by = sorted_by + ' AND ' + col + ' LIKE ' + '"%' + val + '%"'
        i += 1
    sorted_by = sorted_by + ";"
    return Crud.filtered_read(sorted_by)