import unittest
from flask import Flask
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)

    def test_add_student(self):
        data = {
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "birth": 1990,
            "sex": "male",
            "university": "Example University",
            "major": "Computer Science"
        }
        response = self.app.post('/addStudent', json=data)
        self.assertEqual(response.status_code, 201)

    def test_delete_student(self):
        response = self.app.delete('/deleteStudent/1')
        self.assertEqual(response.status_code, 200)

    def test_view_student(self):
        response = self.app.get('/view/1')
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        data = {
            "name": "Jane Smith",
            "username": "janesmith",
            "birth": 1992,
            "sex": "female",
            "university": "Example University",
            "major": "Computer Science"
        }
        response = self.app.put('/updateStudent/1', json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
