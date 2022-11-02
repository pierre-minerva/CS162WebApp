import unittest
import requests

class TestAPI(unittest.TestCase):
	URL = "http://127.0.0.1:5000/"

	def test_home(self):
		response = requests.get(self.URL)
		self.assertEqual(response.status_code, 200)
		print("Test completed!")

	def test_login(self):
		response = requests.get(self.URL+"auth/login")
		self.assertEqual(response.status_code, 200)
		print("Test completed!")

	def test_register(self):
		response = requests.get(self.URL+"auth/register")
		self.assertEqual(response.status_code, 200)
		print("Test completed!")

if __name__ == "__main__":
	unittest.main()
