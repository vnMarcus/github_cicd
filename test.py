import unittest
import requests


URL = "http://127.0.0.1:9090"


class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any necessary test data or environment before running the test cases
        pass

    def setUp(self):
        # Set up any necessary test data or environment before each test case
        pass

    def tearDown(self):
        # Clean up any resources or reset the environment after each test case
        pass

    def test_get_all_students(self):
        response = requests.get(URL)
        self.assertEqual(response.status_code, 200)

    def test_insert_student(self):
        data = {
            'STT': 37,
            'name': 'Bùi Minh Sơn',
            'year': 2002,
            'gender': 'Nam',
            'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội',
            'major': 'Công nghệ thông tin'
        }
        response = requests.post(f"{URL}/addStudent", data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        student_id = 37  # Giá trị của STT cần xóa
        response = requests.delete(f"{URL}/deleteStudent/{student_id}")
        self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        student_id = 37
        response = requests.get(f"{URL}/view/{student_id}")
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        data = {
            'STT': 37,
            'name': 'Bùi Minh Sơn',
            'year': 2002,
            'gender': 'Nam',
            'school': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội',
            'major': 'Công nghệ thông tin'
        }
        response = requests.post(f"{URL}/updateStudent/{data['STT']}", data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
