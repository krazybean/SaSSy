from ..communication import APIComms

# TODO: used as an example for sending agent


if __name__ == '__main__':
    c = APIComms()
    print(c.send('test'))
