import unittest
import app

class TestDockerApp(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.app.test_client()

    def test_save_value(self):
        response = self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
        assert response.status_code ==200
        assert b'2' in response.data
        assert b'two' in response.data


if __name__ == '__main__':
    unittest.main()