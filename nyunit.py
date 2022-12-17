"""
Description:
Unit tests for the New Year application

Creation date: 16/12/2022

Author: Aleksandr Gordienko
Version: 0.11A
"""
import unittest
from datetime import datetime

from nycalc import label
from nycalculator import NewYearApplication


class NYClockMethods(unittest.TestCase):
    """
    New Year application test case class.
    Used to complete unit tests of the application
    """
    application = NewYearApplication(100, 100)

    def test_clock(self):
        time_label = label.TimeLabel(self.application)
        time_label.updater()
        self.assertEqual(
            time_label.tk_var.get(),
            datetime.now().strftime("%H:%M:%S")
        )

    def test_time_remain(self):
        ny_label = label.NewYearLabel(self.application)
        ny_label.updater()
        self.assertEqual(
            ny_label.remain_time,
            datetime(datetime.now().year + 1, 1, 1).timestamp() - datetime.now().timestamp() + 1
        )
