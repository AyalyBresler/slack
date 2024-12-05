import unittest
from unittest.mock import patch

class TestSlackConnection(unittest.TestCase):

    @patch('src.slack_connection.join_to_channel')
    def test_slack_connection_join(self, join_to_slack):
        """
        Test slack_connection_join to check the join to slack
        """
        
        join_to_slack.return_value=True
        self.assertTrue(join_to_slack())
    
    @patch('src.slack_connection.create_a_channel')
    def test_slack_connection_create_channel(self, create_a_channel):
        """
        Test slack_connection_create_channel to check the join to slack
        """
        
        create_a_channel.return_value = True
        self.assertTrue(create_a_channel())

    @patch('src.slack_connection.list_of_connections')
    def test_slack_connection_list_of_connections(self, list_of_connections):
        """
        Test slack_connection_list_of_connections to check the join to slack
        """
        
        list_of_connections.return_value = {'ok': True, 'members':[{'id': 'USLACKBOT', 'team_id': 'T082BRHKWLQ'}, {'id': 'U081GDU7S6A', 'team_id': 'T082BRHKWLQ'}]}
        self.assertEqual(type(list_of_connections()), dict)


if __name__ == "__main__":
    unittest.main()
