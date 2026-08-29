# BL 001 - Windows Endpoint Baseline

## OBJECTIVE
Establish the normal operational and security state of the Windows 11 endpoint before we introduce adversary activity into our SOC.

This will help us to diffrentiate between Suspicious / Dangerous / Normal activity when we look into the system.

## SCOPE
- Windows 11 virtual machine
- Sysmon Telemetry
- Splunk Log Analysis
- WAZUH Endpoint Monitoring
- Windows Application, System, Security

## TOOLS
- Windows 11
- Sysmon
- WAZUH Cloud
- Splunk Enterprise
- VirtualBox

## DATA SOURCES
| Data Source | Index | Sourcetype | Purpose |
|---|---|---|---|
| Sysmon | main | XmlWinEventLog:Microsoft-Windows-Sysmon/Operational | Endpoint telemetry |
| Windows Application | soc-lab | WinEventLog:Application | Windows application events |
| Windows Security | soc-lab | WinEventLog:Security | Security and authentication events |
| Windows System | soc-lab | WinEventLog:System | System-level events |


## BASELINE AREAS
- Endpoint Identity
- Local users information
- Running processes
- Listening Ports
- Running Services
- Scheduled Tasks

## Evidence
Screenshots and supporting eveidence can be found in the `screenshots/` directories

## FINDINGS
We can see the findinds in [Findings.md](findings.md) for the detailed findings.

## LIMITATIONS
This baseline represents the state of the endpoint at the time of
collection. System activity may change as applications, services,
Windows processes and security tools operate normally.

The baseline should therefore be treated as a reference rather than
an absolute definition of legitimate activity.
