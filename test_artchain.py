# test_artchain.py
"""
Tests for ArtChain module.
"""

import unittest
from artchain import ArtChain

class TestArtChain(unittest.TestCase):
    """Test cases for ArtChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtChain()
        self.assertIsInstance(instance, ArtChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
