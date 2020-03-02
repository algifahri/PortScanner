from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print("[+] %d/tcp Open" %tgtPort)
    except:
        print("[-] %d/tcp Closed" %tgtPort)
    finally:
        sock.close()

def portScan(tgtHost, tgtPort):
    try: 
        tgtIP = gethostbyname(tgtHost)
        print("[*] Scan result for: %s" %tgtIP)
    except:
        print("Unknown Host %s" %tgtHost)
        exit()
    
    setdefaulttimeout(1)
    for tgtPort in tgtPort:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('[*] Usage of program: python PortScanner.py -H <host> -p <ports> \n[*] python PortScanner.py --help for more options')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')

    if(tgtHost == None) | (tgtPort == None):
        print(parser.usage)
        exit(0)
    else :
        portScan(tgtHost,tgtPort)
        

if __name__ == "__main__":
    main()