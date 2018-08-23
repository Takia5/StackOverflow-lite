from stack_api import app
import unittest

class StackTestCase(unittest.TestCase):

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
        response = tester.get('/api/v1/users/userId?user_id=1', content_type='application/json')
        self.assertTrue(b'coder456' in response.data)

    def test_get_all_questions(self):
        tester =app.test_client(self)
        response = tester.get('/api/v1/questions/all', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_correct_question_id(self):
        tester =app.test_client(self)
        response = tester.get('/api/v1/questions/questionId?question_id=1', content_type='application/json')
        self.assertTrue(b'typeError' in response.data)

    def test_post_question(self):
        tester =app.test_client(self)
        response = tester.post(
            '/api/v1/questions/question/add', 
            data=dict(question_id="4", title="How to host my app on Heroku", category="Hosting"), follow_redirects=True)
        self.assertIn(b'Successfully posted your question!', response.data)

    def test_post_answer(self):
        tester =app.test_client(self)
        response = tester.post(
            '/api/v1/questions/questionId/answers/post', 
            data=dict(question_id="1", name="dGang", email="gang@gmail.com"), follow_redirects=True)
        self.assertIn(b'You have successfully posted your answer!', response.data)
        
    
if __name__ == '__main__':
    unittest.main()