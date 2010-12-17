#!/usr/bin/python2.5
#
# Copyright 2010 Sentinel Design. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''A minimalist Python interface for the Gowalla API'''

__author__ = 'Drew Yeaton <drew@sentineldesign.net>'
__version__ = '1.0'


import sys
import unittest
import types

from gowalla import Gowalla, GowallaException


USERNAME = ''
PASSWORD = ''
API_KEY = ''

TEST_USERNAME = 'xeeton'
TEST_SPOT_ID = '48462'
TEST_ITEM_ID = '608124'
TEST_TRIP_ID = '89'
TEST_SPOT_LAT = '30.2697'
TEST_SPOT_LNG = '-97.7494'
TEST_SPOT_RADIUS = '50'


class UserTestCase(unittest.TestCase):
    def test_get_user(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
        
        get_result = gowalla.users(id=TEST_USERNAME)
        
        self.assertEqual(type(get_result), types.DictType)
        self.assertNotEqual(get_result['first_name'], None)
    
    
    def test_list_friends(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)

        get_result = gowalla.users.friends(id=TEST_USERNAME)

        self.assertEqual(type(get_result), types.DictType)


class SpotTestCase(unittest.TestCase):
    def test_list_spots(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
        
        list_result = gowalla.spots(lat=TEST_SPOT_LAT, lng=TEST_SPOT_LNG, radius=TEST_SPOT_RADIUS)

        self.assertEqual(type(list_result), types.DictType)
        self.assertNotEqual(list_result['spots'], None)
        
    
    def test_get_spot(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)

        get_result = gowalla.spots(id=TEST_SPOT_ID)

        self.assertEqual(type(get_result), types.DictType)
        self.assertNotEqual(get_result['creator'], None)


class ItemTestCase(unittest.TestCase):
    def test_get_item(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
    
        get_result = gowalla.items(id=TEST_ITEM_ID)
        
        self.assertEqual(type(get_result), types.DictType)
        self.assertNotEqual(get_result['issue_number'], None)
    
    
    def test_get_user_items(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
    
        dict_result = gowalla.users.items(id=TEST_USERNAME)
    
        self.assertEqual(type(dict_result), types.DictType)
        self.assertNotEqual(dict_result['items'], None)
    
    
    def test_get_spot_items(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
    
        dict_result = gowalla.spots.items(id=TEST_SPOT_ID)
    
        self.assertEqual(type(dict_result), types.DictType)
        self.assertNotEqual(dict_result['items'], None)


class TripTestCase(unittest.TestCase):
    def test_list_trips(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
    
        list_result = gowalla.trips()
            
        self.assertEqual(type(list_result), types.DictType)
        self.assertNotEqual(list_result['trips'][0]['name'], None)
    
    
    def test_get_trip(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)

        get_result = gowalla.trips(id=TEST_TRIP_ID)

        self.assertEqual(type(get_result), types.DictType)
        self.assertNotEqual(get_result['description'], None)


class EventTestCase(unittest.TestCase):
    def test_get_item_events(self):
        gowalla = Gowalla(username=USERNAME, password=PASSWORD, api_key=API_KEY)
        
        get_list = gowalla.items.events(id=TEST_ITEM_ID)
                
        self.assertEqual(type(get_list), types.DictType)
        self.assertNotEqual(get_list['events'][0]['type'], None)


if __name__ == "__main__":
    try:
        case = eval(sys.argv[1])
        suite = unittest.TestLoader().loadTestsFromTestCase(case)
        unittest.TextTestRunner().run(suite)
    except IndexError:
        unittest.main()