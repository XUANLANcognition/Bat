import ipaddress

class Scanner(object):
    """
    I am the source of all scanners.
    """

    def __init__(self, argv):
        self.argv = argv
        self.dnetwork = '127.0.0.1'
        self.dport = '8000'

    def check_ip_valid(self, ip):
        try:
            ipaddress.IPv4Network(ip)
            return True
        except ValueError:
            return False

    def p1(self):
        pass

    def p2(self):
        pass

    def p3(self):
        pass

    def execute(self):
        if len(self.argv) == 1:
            self.dnetwork = self.argv[0]
            self.p1()
        elif len(self.argv) == 2:
            if self.check_ip_valid(self.argv[0]):
                self.dnetwork = self.argv[0]
                self.dport = self.argv[1]
                self.p2()
            else:
                self.dnetwork = self.argv[0]
                self.dport = self.argv[1]
                self.p3()
        else:
            pass




