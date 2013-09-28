import unittest
import math
maximum=10**12
from triangle import detect_triangle
class SimpleWidgetTestCase(unittest.TestCase):
        def setUp(self):
            pass

        # chuoi khong chuyen doi duoc ---------------------------------
        def test_saikieu_input1(self):
            self.assertEqual(detect_triangle('abc',7.5,8.6), -1)
            
        def test_saikieu_input2(self):
            self.assertEqual(detect_triangle(7.1,'abc',8.3), -1)
            
        def test_saikieu_input3(self):
            self.assertEqual(detect_triangle(7.3,8.2,'abc'), -1)


        #chuoi khong chuyen doi duoc, vuot ngoai gioi han
        def test_saikieu_input4(self):    
            self.assertEqual(detect_triangle('abc',9,-7), -1)
        def test_saikieu_input5(self):    
            self.assertEqual(detect_triangle('abc',maximum+1,9), -1)
            
        #so am.---------------------------------------------------------
        def test_gioihan_input1(self):    
            self.assertEqual(detect_triangle(-1,7,8), -2)
            self.assertEqual(detect_triangle('-1',7,8), -2)
            
        def test_gioihan_input2(self):
            self.assertEqual(detect_triangle(7,-7,8), -2)
            self.assertEqual(detect_triangle(7,'-7',8), -2)
        def test_gioihan_input3(self):
            self.assertEqual(detect_triangle(7,9,-7), -2)
            self.assertEqual(detect_triangle(7,9,'-7'), -2)
            
        #vuot max.------------------------------------------------------- 
        def test_gioihan_input4(self):    
            self.assertEqual(detect_triangle(maximum+1,7,9), -2)
        def test_gioihan_input5(self):    
            self.assertEqual(detect_triangle(7,maximum+1,9), -2)
        def test_gioihan_input6(self):    
            self.assertEqual(detect_triangle(7,9,maximum+1), -2)
                             
            
        def test_tamgiacdeu1(self):
            self.assertEqual(detect_triangle(1,1,1), 1)
            self.assertEqual(detect_triangle(math.sqrt(6),math.sqrt(6),math.sqrt(6)), 1)
        def test_tamgiacdeu2(self):    
            self.assertEqual(detect_triangle('4','4','4'), 1)
        def test_tamgiacdeu3(self):    
            self.assertEqual(detect_triangle('4.5',4.5,4.5), 1)
        def test_tamgiacdeu4(self):                     
            self.assertEqual(detect_triangle(4.5,'4.5',4.5), 1)
        def test_tamgiacdeu5(self):                     
            self.assertEqual(detect_triangle(4.5,4.5,'4.5'), 1)
            
            
        def test_tamgiacvuong1(self):
            self.assertEqual(detect_triangle(3,5,4), 4)
        def test_tamgiacvuong2(self):
            self.assertEqual(detect_triangle('4',3,5), 4)
        def test_tamgiacvuong3(self):
            self.assertEqual(detect_triangle(4,'5',3), 4)
        def test_tamgiacvuong4(self):
            self.assertEqual(detect_triangle(5,3,'4'), 4)
            
            
        def test_tamgiaccan1(self):
            self.assertEqual(detect_triangle(5,5,3), 3)
            self.assertEqual(detect_triangle(5.6,5.6,3), 3)                 
        def test_tamgiaccan2(self):
            self.assertEqual(detect_triangle('5',5,3), 3)
                             
        def test_tamgiacvuongcan1(self):
            self.assertEqual(detect_triangle(math.sqrt(2),1,1), 2)
        def test_tamgiacvuongcan2(self):
            self.assertEqual(detect_triangle(1,math.sqrt(2),1), 2)
        def test_tamgiacvuongcan3(self):
            self.assertEqual(detect_triangle(1,1,math.sqrt(2)), 2)
        def test_khonglatamgiac1(self):
            self.assertEqual(detect_triangle(2,1,1), 0)
        def test_khonglatamgiac2(self):
            self.assertEqual(detect_triangle('2',1,1), 0)
            
      
            
                    
if __name__ == '__main__':
    unittest.main()
