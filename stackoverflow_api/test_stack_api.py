from stack_api import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_get_all_users(self):
        tester =app.test_client(self)
        response = tester.get('/api/v1/users/all', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_home_page_loads(self):
        tester =app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'StackOverflow-lite' in response.data)

    def test_get_correct_user_id(self):
        tester =app.test_client(self)
        response = tester.post(
            '/api/v1/users/userId', 
            data=dict(user_id="1"), follow_redirects=True)
        self.assertTrue(b'2', response.data)

    def test_get_all_questions(self):
        tester =app.test_client(self)
        response = tester.get('/api/v1/questions/all', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_correct_question_id(self):
        tester =app.test_client(self)
        response = tester.post(
            '/api/v1/questions/questionId', 
            data=dict(question_id="1"), follow_redirects=True)
        self.assertIn(b'1', response.data)
        
    


if __name__ == '__main__':
    unittest.main()