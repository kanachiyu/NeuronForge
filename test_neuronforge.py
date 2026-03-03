# test_neuronforge.py
"""
Tests for NeuronForge module.
"""

import unittest
from neuronforge import NeuronForge

class TestNeuronForge(unittest.TestCase):
    """Test cases for NeuronForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuronForge()
        self.assertIsInstance(instance, NeuronForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuronForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
