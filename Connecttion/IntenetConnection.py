import urllib


def connectionToEthernet():

    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
