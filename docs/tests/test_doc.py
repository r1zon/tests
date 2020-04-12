import unittest
from unittest.mock import patch
import app


class TestDocuments(unittest.TestCase):
    def setUp(self) -> None:
        with patch('app.input', return_value = 'q'):
            app.secretary_program_start()

    def test_is_doc_exists(self):
        doc_number = app.check_document_existance('11-2')
        self.assertTrue(doc_number)

    def test_is_doc_not_exists(self):
        doc_number = app.check_document_existance('112')
        self.assertFalse(doc_number)

    def test_get_doc_owner(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '11-2'
            doc_number = app.get_doc_owner_name()
            self.assertEqual(doc_number, 'Геннадий Покемонов')

            in_mock.return_value = '10006'
            doc_number = app.get_doc_owner_name()
            self.assertNotEqual(doc_number, 'Геннадий Покемонов')

    def test_get_all_doc_owners_names(self):
        user_list = app.get_all_doc_owners_names()
        self.assertSetEqual(user_list, {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})

    @unittest.expectedFailure
    def test_get_wrong_doc_owners_names(self):
        user_list = app.get_all_doc_owners_names()
        self.assertSetEqual(user_list, {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов', 'Брет Пит'})

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf('11-2')
        self.assertTrue({'1': ['2207 876234']})

    def test_add_new_shelf(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '4'
            shelf_nubmer, shelf_nubmer_bool = app.add_new_shelf()
            self.assertTrue(shelf_nubmer_bool)

            in_mock.return_value = '1'
            shelf_nubmer, shelf_nubmer_bool = app.add_new_shelf()
            self.assertFalse(shelf_nubmer_bool)

    def test_delete_doc(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '11-2'
            doc_nubmer, doc_nubmer_bool = app.delete_doc()
            self.assertTrue(doc_nubmer_bool)

    def test_get_doc_shelf(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '11-2'
            shelf_number = app.get_doc_shelf()
            self.assertEqual(shelf_number, '1')

            in_mock.return_value = '10006'
            shelf_number = app.get_doc_shelf()
            self.assertNotEqual(shelf_number, '1')

    def test_get_not_exist_doc_shelf(self):
        with patch('app.input') as in_mock:
            in_mock.return_value = '1102'
            shelf_number = app.get_doc_shelf()
            self.assertNotEqual(shelf_number, '1')

    def test_add_new_doc(self):
        with patch('app.input') as in_mock:
            in_mock.side_effect = ['1102', 'passport', 'Netolog Netologiev', '4']
            shelf_number = app.add_new_doc()
            self.assertEqual(shelf_number, '4')