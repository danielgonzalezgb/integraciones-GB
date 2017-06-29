from Scanner import Scanner
from Scan import Scan


scanner = Scanner('admin','gbadvisors', True, 'https://gbsites.ddns.net:33335')
scanner.LoginScanner()
scans = scanner.GetScans()
for scan in range(0, len(scans)):
    scan_pro = Scan(int(scans[scan]["id"]), scanner )
    scan_pro.GetScanDetails()