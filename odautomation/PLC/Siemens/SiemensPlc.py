import ipaddress
from snap7.client import Client
from odautomation.PLC.Siemens.SmartTags import SmartTags






class SiemensPlc(SmartTags):
    def __init__(self, ipaddr, name=None):
        self.ipaddr = ipaddress.IPv4Address(ipaddr)
        self.name = name
        self._port = 102
        self._client = Client()
        self.SmartTags = SmartTags(self)


    def connect(self):
        return self._client.connect(self.ipaddr, 0, 0, self.port)

    def get_connected(self):
        return self._client.get_connected()

    def disconnect(self):
        return self._client.disconnect()

    def get_plc_state(self):
        return self._client.get_cpu_state()

    def get_plc_info(self):
        return self._client.get_cpu_info()

    def get_datetime(self):
        return self._client.get_plc_datetime()


if __name__ == '__main__':
    x = SiemensPlc('192.168.1.1')
    y = x.SmartTags.Int(1,1)
    print(1)
