from cassandra.cluster import Cluster # type: ignore
from cassandra.auth import PlainTextAuthProvider # type: ignore
import logging

logging.basicConfig(filename='logfiles/test.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Connector:
    def __init__(self):
        """
        :DESC: Creates connection with Database
        """
        logging.info('Creating connection with Cassandra Database')
        self.Client_id = 'cGCxxwzjAYFYXpzpNdehynhD'
        self.Client_secret = 'ZzZ.t0ae-iqf9sTylmge9WX-2ah.6-57000DXqBhY6LbvU8dbC-ZoYSchaKmsANk-,ghfZm00Sq7lwZCoKPMYpoAm,GTaSicMDpXUXxMu9RYSokdvEFm1E9T503BANeW'
        cloud_config = {'secure_connect_bundle': 'secure-connect-flightdatabase.zip'}
        auth_provider = PlainTextAuthProvider(self.Client_id, self.Client_secret)
        logging.info('Creating Clusters')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect('flightdb')


    def Database(self):
        """
        :DESC: Retrieves Data from Database
        :return: tuples of records from Database
        """
        logging.info('Retrieving data from flight Database')
        self.session.execute('use flightdb')
        row = self.session.execute('SELECT * FROM "FlightFare";')
        collection = []
        for i in row:
            collection.append(tuple(i))
        return tuple(collection)