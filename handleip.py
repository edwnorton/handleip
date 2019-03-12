# -*- coding: utf-8 -*-

class IPnetmask(object):
    def __init__(self, data):
        self._ipv4bit = 32
        x = data.split('/')
        if len(x) == 2:
            (ipstr, self.prifix) = x
            bytes = [int(i) for i in ipstr.split('.')]
            for i in bytes:
                if i < 0 or i > 255:
                    raise ValueError('ip value error, value must be 0<x<256')
            self.prifixlen = int(self.prifix)
        if len(x) == 1:
            ipstr = x[0]
            self.prifixlen = 32
        self.ipoct = ipaddressTooct(ipstr)
        self._prifixlen = localIplen(self.prifixlen)
        if not checkIpddressWithnet(self.ipoct, self.prifixlen):
            raise ValueError('network mask range error')

    def len(self):
        return 2 ** (32 - self.prifixlen)

    def __len__(self):
        return self.len()

    def __contains__(self, item):
        item = IPnetmask(item)
        if item.ipoct > self.ipoct and item.ipoct < self.ipoct + self.len():
            return True



def ipaddressTooct(ipstr):
    bytes = [int(i) for i in ipstr.split('.')]
    return (bytes[0] << 24) + (bytes[1] << 16) + (bytes[2] << 8) + bytes[3]

def localIplen(prifixlen):
    return 2 ** (32 - prifixlen)

def checkIpddressWithnet(net, prifixlen):
    return (net & prifixTomask(prifixlen) == net)

def prifixTomask(prifixlen):
    return (1 << prifixlen) - 1 << (32 - prifixlen)

if __name__ == '__main__':
    a = IPnetmask('192.168.1.0/26')
    if '192.168.1.2' in a:
        print('True')