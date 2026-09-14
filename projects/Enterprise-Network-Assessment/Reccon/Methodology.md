#This will contain the methods that I used to carry out reconnaisance on the Organization and the tools and processes used to carry it out.

### Findings 001: Exposed Windows Network Services
Target: `192.168.49.131` 

# Method
Nmap Service/Version Scan
Command used: `nmap -sV 192.168.49.131`

## Discovery
- Host active with a latency of 1.6ms
- OS name: `Microsoft Windows`
- 4 Open ports
  | Port | State | Service      | Nmap identification   |
  | ---: | ----- | ------------ | --------------------- |
  |  135 | Open  | MSRPC        | Microsoft Windows RPC |
  |  139 | Open  | NetBIOS-SSN  | Microsoft NetBIOS     |
  |  445 | Open  | Microsoft-DS | SMB                   |
  | 5357 | Open  | HTTP         | Microsoft HTTPAPI 2.0 |

This endpoint exposed several Windows Network Services which can serve as attack surfaces for any attacker.
