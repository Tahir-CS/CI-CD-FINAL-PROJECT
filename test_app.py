"""
Unit tests for the Counter Service
"""

import unittest
import json
from service.app import app


class TestCounterService(unittest.TestCase):
    """Test cases for Counter Service"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_create_counter(self):
        """Test creating a new counter"""
        response = self.app.post('/counters/test_counter')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['test_counter'], 0)
    
    def test_get_counter(self):
        """Test getting a counter"""
        # Create a counter first
        self.app.post('/counters/test_counter')
        
        # Get the counter
        response = self.app.get('/counters/test_counter')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['test_counter'], 0)
    
    def test_increment_counter(self):
        """Test incrementing a counter"""
        # Create a counter first
        self.app.post('/counters/test_counter')
        
        # Increment the counter
        response = self.app.put('/counters/test_counter/increment')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['test_counter'], 1)


if __name__ == '__main__':
    unittest.main()