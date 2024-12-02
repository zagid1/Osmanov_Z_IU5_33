import unittest
import main as RK2
from operator import itemgetter


class TestMainMethods(unittest.TestCase):

    def test_first_task(self):
        test_list = [
            ('Photoshop', 1988, 'Asus', 'Aleksey'),
            ('Firefox', 2002, 'Toshiba', 'Andrey'),
            ('Visual Studio', 1997, 'Toshiba', 'Andrey'),
            ('Slack', 2013, 'Huawei', 'Michael'),
            ('Blender', 1998, 'MacBook Air', 'Bob'),
            ('AutoCAD', 1982, 'HP', 'Charlie'),
            ('Notepad++', 2003, 'Dell XPS', 'Alice'),
            ('Edge', 2015, 'Dell XPS', 'Alice'),
            ('Google Chrome', 2008, 'Xiaomi', 'Zagid'),
            ('Zoom', 2019, 'Lenovo', 'Ivan'),
            ('Internet Explorer', 1995, 'Thinkpad', 'Gasan'),
            ('Vivaldi', 2016, 'Lenovo', 'Ivan'),
            ('Opera', 1995, 'HP', 'Charlie'),

        ]
        result = RK2.first_task(test_list)
        reference =[
            (['Photoshop'], 'Asus'),                         #Aleksey
            (['Notepad++', 'Edge'], 'Dell XPS'),             #Alice
            (['Firefox', 'Visual Studio'], 'Toshiba'),       #Andrey
        ]
        self.assertEqual(result, reference)

    def test_second_task(self):
        test_list = [
            ('Photoshop', 1988, 'Asus', 'Aleksey'),
            ('Firefox', 2002, 'Toshiba', 'Andrey'),
            ('Visual Studio', 1997, 'Toshiba', 'Andrey'),
            ('Slack', 2013, 'Huawei', 'Michael'),
            ('Blender', 1998, 'MacBook Air', 'Bob'),
            ('AutoCAD', 1982, 'HP', 'Charlie'),
            ('Notepad++', 2003, 'Dell XPS', 'Alice'),
            ('Edge', 2015, 'Dell XPS', 'Alice'),
            ('Google Chrome', 2008, 'Xiaomi', 'Zagid'),
            ('Zoom', 2019, 'Lenovo', 'Ivan'),
            ('Internet Explorer', 1995, 'Thinkpad', 'Gasan'),
            ('Vivaldi', 2016, 'Lenovo', 'Ivan'),
            ('Opera', 1995, 'HP', 'Charlie'),
        ]
        result = RK2.second_task(test_list)

        reference =[
            ( 1982, 'HP'),
            ( 1988, 'Asus'),
            ( 1995, 'Thinkpad'),
            ( 1997, 'Toshiba'),
            ( 1998, 'MacBook Air'),
            ( 2003, 'Dell XPS'),
            ( 2008, 'Xiaomi'),
            ( 2013, 'Huawei'),
            ( 2016, 'Lenovo'),
        ]
        self.assertEqual(result, reference)

    def test_third_task(self):
        test_list = [
            ('Photoshop', 1988, 'Asus'),
            ('AutoCAD', 1982, 'Asus'),
            ('Firefox', 2002, 'Toshiba'),
            ('Visual Studio', 1997, 'Toshiba'),
            ('Slack', 2013, 'Huawei'),
            ('Notepad++', 2003, 'HP'),
            ('Edge', 2015, 'Huawei'),
            ('Blender', 1998, 'MacBook Air'),
            ('AutoCAD', 1982, 'HP'),
            ('Notepad++', 2003, 'Dell XPS'),
            ('Edge', 2015, 'Dell XPS'),
        ]
        reference = [
            ('AutoCAD', 1982, 'Asus'),
            ('AutoCAD', 1982, 'HP'),
            ('Blender', 1998, 'MacBook Air'),
            ('Edge', 2015, 'Huawei'),
            ('Edge', 2015, 'Dell XPS'),
            ('Firefox', 2002, 'Toshiba'),
            ('Notepad++', 2003, 'HP'),
            ('Notepad++', 2003, 'Dell XPS'),
            ('Photoshop', 1988, 'Asus'),
            ('Slack', 2013, 'Huawei'),
            ('Visual Studio', 1997, 'Toshiba'),
        ]
        result = RK2.third_task(test_list)
        self.assertEqual(result, reference)


if __name__ == '__main__':
    unittest.main()
