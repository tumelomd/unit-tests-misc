import unittest
from process_json import Hubspot

class Test_Mapping(unittest.TestCase):
    def test_updateContact_with_successful_request(self):
        hubspot = Hubspot()

        self.assertEqual(
            hubspot.process_json({"first_name":"tumelo","last_name":"ceba","phone":"0123456"}),
            {'hs_first_name': 'tumelo', 'hs_last_name': 'ceba', 'hs_phone': '0123456'})

if __name__ == '__main__':
    unittest.main()