"""
Unit tests for the API app
"""
from django.test import TestCase, Client
from django.urls import reverse
from api.views import calculate_lcm_range, lcm


class LCMCalculationTestCase(TestCase):
    """Test cases for LCM calculation logic"""
    
    def test_lcm_basic(self):
        """Test LCM calculation for basic cases"""
        # LCM of 1 and 1 should be 1
        self.assertEqual(lcm(1, 1), 1)
        
        # LCM of 2 and 3 should be 6
        self.assertEqual(lcm(2, 3), 6)
        
        # LCM of 4 and 6 should be 12
        self.assertEqual(lcm(4, 6), 12)
    
    def test_lcm_range_1_to_10(self):
        """
        Test LCM of range 1 to 10
        Expected result: 2520
        """
        result = calculate_lcm_range(1, 10)
        self.assertEqual(result, 2520)
        
        # Verify that 2520 is divisible by all numbers from 1 to 10
        for i in range(1, 11):
            self.assertEqual(result % i, 0, f"2520 should be divisible by {i}")
    
    def test_lcm_range_1_to_5(self):
        """
        Test LCM of range 1 to 5
        Expected result: 60
        """
        result = calculate_lcm_range(1, 5)
        self.assertEqual(result, 60)
        
        # Verify divisibility
        for i in range(1, 6):
            self.assertEqual(result % i, 0, f"60 should be divisible by {i}")
    
    def test_lcm_range_1_to_1(self):
        """
        Test LCM of range 1 to 1
        Expected result: 1
        """
        result = calculate_lcm_range(1, 1)
        self.assertEqual(result, 1)
    
    def test_lcm_range_2_to_5(self):
        """
        Test LCM of range 2 to 5
        Expected result: 60
        """
        result = calculate_lcm_range(2, 5)
        self.assertEqual(result, 60)
        
        # Verify divisibility
        for i in range(2, 6):
            self.assertEqual(result % i, 0, f"60 should be divisible by {i}")
    
    def test_lcm_range_1_to_20(self):
        """
        Test LCM of range 1 to 20
        """
        result = calculate_lcm_range(1, 20)
        
        # Verify divisibility for all numbers 1 to 20
        for i in range(1, 21):
            self.assertEqual(result % i, 0, f"{result} should be divisible by {i}")
        
        # The result should be positive
        self.assertGreater(result, 0)


class LCMAPIEndpointTestCase(TestCase):
    """Test cases for LCM API endpoints"""
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
        self.url = reverse('api:calculate_lcm')
    
    def test_get_request_valid(self):
        """Test GET request with valid parameters"""
        response = self.client.get(self.url, {'x': 1, 'y': 10})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 2520)
        self.assertEqual(response.json()['x'], 1)
        self.assertEqual(response.json()['y'], 10)
    
    def test_get_request_missing_parameters(self):
        """Test GET request with missing parameters"""
        response = self.client.get(self.url, {'x': 1})
        
        self.assertEqual(response.status_code, 400)
    
    def test_get_request_invalid_range(self):
        """Test GET request with x > y"""
        response = self.client.get(self.url, {'x': 10, 'y': 1})
        
        self.assertEqual(response.status_code, 400)
    
    def test_post_request_valid(self):
        """Test POST request with valid parameters"""
        data = {'x': 1, 'y': 10}
        response = self.client.post(self.url, data, content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 2520)
    
    def test_post_request_invalid(self):
        """Test POST request with invalid parameters"""
        data = {'x': 'invalid', 'y': 10}
        response = self.client.post(self.url, data, content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
    
    def test_negative_numbers(self):
        """Test with negative numbers (should fail)"""
        response = self.client.get(self.url, {'x': -1, 'y': 10})
        
        self.assertEqual(response.status_code, 400)
    
    def test_zero_values(self):
        """Test with zero values (should fail)"""
        response = self.client.get(self.url, {'x': 0, 'y': 10})
        
        self.assertEqual(response.status_code, 400)
