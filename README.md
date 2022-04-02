This project attempts to triage common Nessus findings with large number of instances.

# Usage:
./diagnostic.py <service> <check> <iplist>

For e.g. ./diagnostic.py DNS CVE-2005-1794 iplist.txt

# List of checks supported:
* SMBv1 supported
* SMB Signing
* RDP : CVE-2005-1794
