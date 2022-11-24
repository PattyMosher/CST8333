import unittest
import CheeseWiz
import csv
import Crud
import sqlite3


class CheeseWizTest(unittest.TestCase):
    def test_database_read_all(self):
        csv_counter = 0
        with open(CheeseWiz.path, 'r', encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader: csv_counter += 1
        slqite_records = Crud.read_all()
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        db_count = cursor.execute('SELECT COUNT(*) FROM cheeses').fetchone()
        self.assertEqual(csv_counter, db_count)

    def test_filtering_function(self):
        """Tests database filtering matches csv filtering"""
        csv_matches = []
        with open(CheeseWiz.path, 'r', encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['MilkTypeEn'] == 'Buffalo Cow':
                    csv_matches.append(row)
        db_matches = Crud.filtered_read('Select * from cheeses WHERE MilkTypeEn LIKE "%Buffalo Cow%";')
        self.assertEqual(csv_matches, db_matches)


if __name__ == '__main__':
    unittest.main()