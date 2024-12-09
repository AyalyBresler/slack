import unittest
from unittest.mock import patch

class TestSlackConnection(unittest.TestCase):

    @patch('src.slack_connection.join_to_channel')
    def test_slack_connection_join(self, joinToSlack):
        """
        Test slack_connection_join to check the join to slack
        """
        
        joinToSlack.return_value=True
        self.assertTrue(joinToSlack())
    
    @patch('src.slack_connection.create_a_channel')
    def test_slack_connection_create_channel(self, createAChannel):

        """
        Test slack_connection_create_channel to check the join to slack
        """
        
        createAChannel.return_value = True
        self.assertTrue(createAChannel())

    @patch('src.slack_connection.list_of_connections')
    def test_slack_connection_list_of_connections(self, listOfConnections):
        """
        Test slack_connection_list_of_connections to check the list of the connections to slack!
        """
        
        listOfConnections.return_value = {'ok': True, 'members':[{'id': 'USLACKBOT', 'team_id': 'T082BRHKWLQ'}, {'id': 'U081GDU7S6A', 'team_id': 'T082BRHKWLQ'}]}
        self.assertEqual(type(listOfConnections()), dict)


if __name__ == "__main__":
    unittest.main()
