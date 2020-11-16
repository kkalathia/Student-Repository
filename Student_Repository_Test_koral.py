import unittest
from datetime import datetime
from typing import List, Tuple, Dict
from HW08_koral_kalathia import date_arithmetic, file_reader, FileAnalyzer


class HW08_Testcases(unittest.TestCase):
    def test_date_arithmetic(self):
        """The function tests date_arithmetic function"""
        self.assertEqual(date_arithmetic(), (datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 241))
        self.assertNotEqual(date_arithmetic(), (datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 1, 0, 0), 240))

    def test_file_reader(self):
        """The function tests the file_reader() function."""
        calculated: List[tuple] = [('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'),
                                   ('345', 'Benji Cai', 'Software Engineering')]
        self.assertNotEqual(list(file_reader("func2_test.txt", 3, '|', False)), calculated)
        self.assertEqual(list(file_reader("func2_test.txt", 3, '|', True)), calculated)
        self.assertEqual(list(file_reader("func2_test.txt1", 3, '|', False)), ['File Not Found'])

    def test_fileanalyzer(self):
        """The function tests the Fileanalyzer class which gives scans directory and gives filename, number of
        classes, methods, lines and characters """
        fa: FileAnalyzer = FileAnalyzer("path")
        calculated: Dict[str, Dict[str, int]] = {
            '0_defs_in_this_file.py': {'classes': 0, 'functions': 0, 'lines': 3, 'characters': 55},
            'file1.py': {'classes': 2, 'functions': 4, 'lines': 25, 'characters': 270},
            'file2.py': {'classes': 2, 'functions': 5, 'lines': 20, 'characters': 205}

        }
        calculated1: Dict[str, Dict[str, int]] = {
            '0_defs_in_this_file.py': {'classes': 0, 'functions': 0, 'lines': 3, 'characters': 55},
            'file1.py': {'classes': 2, 'functions': 4, 'lines': 25, 'characters': 270},
            'file2.py': {'classes': 2, 'functions': 5, 'lines': 20, 'characters': 255}

        }
        self.assertEqual(fa.analyze_files(), calculated)
        self.assertNotEqual(fa.analyze_files(), calculated1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
