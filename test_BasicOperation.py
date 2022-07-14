import BasicOperation

class TestBasicOperation:
    
    def test_add(self):
        assert 4 == BasicOperation.add(3,1)
        
    def test_sub(self):
        assert 1 == BasicOperation.sub(3,2)
        
    def test_mul(self):
        assert 6 == BasicOperation.mul(3,2)
