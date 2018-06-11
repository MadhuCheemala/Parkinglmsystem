import unittest
from tdirdlotmg.model.businesslogic import car_entry,car_exit
import pandas as pd
class PLotcar(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_car_entry(self):
        """Is five successfully determined to be prime?"""
        slotlist=["aa","ab","ac","ad","ae"]
        slotdatapath="C:\\Users\\MADHU\\PycharmProjects\\Projectlotmg\\datap\\slotdata.csv"
        exitdf=pd.read_csv(slotdatapath)
        Total_no_slot=5
        car=3
        avial_slot,car_slotid=car_entry(slotdatapath,slotlist,exitdf,Total_no_slot,car)
        expect=avial_slot
        self.assertEquals(avial_slot,expect)

    def test_car_exit(self):
        """Is five successfully determined to be prime?"""
        slotdatapath="C:\\Users\\MADHU\\PycharmProjects\\Projectlotmg\\datap\\slotdata.csv"
        exitdf=pd.read_csv(slotdatapath)
        carid="ab"
        car_slotid,avial_slot=car_exit(slotdatapath,carid,exitdf)
        expect=avial_slot
        self.assertEquals(avial_slot,expect)

if __name__ == '__main__':
    unittest.main()
