import unittest
import os
import json
from app import create_app

class PoliticalPartiesTestCase(unittest.TestCase):

    #This class represents the political parties test case
    
    def setUp(self):
        """ Initialize app and test variables """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.politicalparty = { 
            "name" : "African Liberation Party" ,
            "abbreviation" : "ALP" ,
            "members" : "15" ,
            "headquarters": "Biafra House, Kaaunda Road",
            "chairperson": "Betty Sade"
            }

    def test_politicalparty_creation (self):
        """Test that API can create political party"""
        response = self.client.post('/api/v1/politicalparties', json=self.politicalparty)
        self.assertEqual(response.status_code, 201)