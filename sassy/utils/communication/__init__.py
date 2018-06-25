import zmq
from time import sleep
import random
from sassy.cortex.app import app
from sassy.utils.tools import Struct
from sassy.utils.errors import communications


# Type construction for connection property management
def host_port(host, port):
    return Struct('connection', **{'host': host,
                                   'port': port})


API_Connection = {'tx': host_port('127.0.0.1', 5557),
                  'rx': host_port('127.0.0.1', 5558)}

Cont_Connection = {'tx': host_port('127.0.0.1', 5558),
                   'rx': host_port('127.0.0.1', 5557)}


def forever() -> bool:
    return True


def shutdown(number: int) -> str:
    for num in range(number, -1, -1):
        print(f" -- [ Shutting down in: {num}]", end='\r')
        sleep(1)


class Comms(object):
    def __init__(self, serviceconn=None):
        self.serviceconn = serviceconn
        self.tx, self.rx = self._marshal_()

    def _marshal_(self):
        """ _marshal_ allows for class inheretance to utilize super for config overrides
        to setup other sockets
        """
        try:
            tx = f"tcp://{self.serviceconn['tx'].host}:{self.serviceconn['tx'].port}"
            rx = f"tcp://{self.serviceconn['rx'].host}:{self.serviceconn['rx'].port}"
            return tx, rx
        except Exception as e:
            msg = f"Failed to parse service object"
            raise communications.CommunicationServiceParseError(msg, e)

    def send(self, message):
        """ Sender using the provided broadcast port tx

        Args:
            message (str): Message to be put on the bus for consumption
        Returns:
            None
        """
        context = zmq.Context()
        zmq_socket = context.socket(zmq.PUSH)
        zmq_socket.bind(self.tx)
        zmq_socket.send_json({'message': message})
        return 'sent'

    def service(self):
        """ Service needs to be subprocessed and ran on both tx/rx  configurations

        # Example Usage:
        # API Subprocess
        api = APIComms()
        api.service()

        # Controller Subprocess
        controller = ControllerComms()
        controller.service()

        # Individual messages can be sent from the API runtime
        api_sender = APIComms()
        api_sender.send("test message")

        # This will trigger the response event, the controller needs
        # an adapter so that it can take action upon

        """
        service_id = random.randrange(1, 10005)
        context = zmq.Context()
        # get work
        consumer_receiver = context.socket(zmq.PULL)
        consumer_receiver.connect(self.tx)
        # send work
        consumer_sender = context.socket(zmq.PUSH)
        consumer_sender.connect(self.rx)
        response = None

        while forever():
            try:
                message = consumer_receiver.recv_json()
                data = message['message']
                result = {'original': data, 'response': f'{data} - responded, by: [{service_id}]'}
                # TODO: Controller event handle before sending acknowledgement below
                consumer_sender.send_json(result)

            except KeyboardInterrupt:
                app.logger.warning('\n')
                app.logger.warning(" - Requested service interruption, shutting down in 5")
                shutdown(5)
                break

            try:
                response = self.response()
                if response:
                    print("Take Action")
                else:
                    sleep(2)
            except Exception as e:
                print(e)
                print("Wait")
                break

    def response(self) -> str:
        """ To be used for a method as an event response

        Args:
            None
        Returns:
            result (str): response from the consumer
        """
        context = zmq.Context()
        results_receiver = context.socket(zmq.PULL)
        results_receiver.bind(self.rx)
        result = results_receiver.recv_json()
        return result


class APIComms(Comms):
    """ Inherited comms class with API connections configs"""
    def __init__(self):
        super(APIComms, self).__init__(serviceconn=API_Connection)


class ControllerComms(Comms):
    """ Inherited comms class with Controller connection configs"""
    def __init__(self):
        super(ControllerComms, self).__init__(serviceconn=Cont_Connection)

