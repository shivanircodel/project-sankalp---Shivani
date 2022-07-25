# tests/test_app.py

import unittest
import os

os.environ['TESTING']='true'

from app import app

class AppTestCase(unittest.TestCase):
   def setUp(self):
       self.client=app.test_client()

   def test_home(self):
       response=self.client.get("/")
       assert response.status_code == 200
       html = response.get_data(as_text=True)
       assert "<h1>About Arpitha</h1>" in html
       

   def test_home_navbar(self):
       response=self.client.get("/Hobbies")
       assert response.status_code == 200
       html = response.get_data(as_text=True)
       assert "<p>➼Reading</p>" in html 


   def test_timeline(self):
       response=self.client.get("/api/timeline_post")
       assert response.status_code == 200
       assert response.is_json
       json = response.get_json()
       assert"timeline_posts"in json
       assert len(json["timeline_posts"]) == 0

   def test_timeline_post(self):
      response=self.client.post("/api/timeline_post", data= {"name":"John Doe","email":"john@example.com","content":"Hello world,I'm John!"})
      response=self.client.get("/api/timeline_post")
      assert response.status_code == 200
      assert response.is_json
      json = response.get_json()
      assert"timeline_posts"in json
      assert len(json["timeline_posts"]) == 1


   def test_malformed_timeline_post_name(self):
    #POST request missing name
       response=self.client.post("/api/timeline_post", data= {"email":"john@example.com","content":"Hello world,I'm John!"})
       assert response.status_code==400
       html = response.get_data(as_text = True)
       assert "Invalid name" in html 
    
   def test_malformed_timeline_post_content(self):
    #Post request with missing content
       response= self.client.post("/api/timeline_post", data= {"name":"John Doe","email":"john@example.com","content":""})
       assert response.status_code==400
       html = response.get_data(as_text = True)
       assert "Invalid content" in html 
       
   def test_malformed_timeline_post_email(self):
    #POST request with malformed email
       response = self.client.post("/api/timeline_post", data={"name":"John Doe","email":"not-an-email","content":"Hello world,I'm John!"})
       assert response.status_code==400
       html = response.get_data(as_text = True)
       assert "Invalid email" in html
