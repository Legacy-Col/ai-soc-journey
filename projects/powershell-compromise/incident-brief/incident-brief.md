This is a brief on the incident that occured. This brief contains information on:

### Incident Information

|Field   | Details |
|---|---|
|Incident ID | INC-001 |
|Date | 30/08/26 |
|Incident Severity | Medium |
|Status | Open |
|Detection Type | Suspicious Powershell Activity |
|Affected Asses | Windows 11 |
|Assiged Analyst | CHUKWU COLLINS |

### Incident Summary
An Alert occured that said that there was a suspicious powershell action that occured on our clients windows 11 Operating System. 
Initial security activities were carried out to accertain the severity of the activity and to analys if the alert was a False Positive or True Positive.

### Initial Information Available
|Field | Details |
|---|---|
|Endpoint | Windows 11 |
|Monitoring | WAZUH and SYSMON |
|Log Analysis | Splunk Enterprise |
|Activity | Suspicious Powershell |
|Legitimacy | Unknow still under Analysis |

### Investigation Objective
- To discover the severity and legitmacy of the alert
- Discovery of the type of activity that occured on the endpoint
- What processes were created
- Was there any communication with the outside world
- What is the process command and what it executed
- Any encoded command in the powershell
- What evidence are avaiable to show that there was any such activity

### Scope
## In-Scope
- Windows 11 endpoint
- Sysmon Telemetry
- Windows Application/Security/System
- Wazuh Alerts
- Splunk log analysis
- Related network and process activity

## Out-of-Scope
- Endpoints that are not affected
- Activities unrelated to the endpoint
- External endpoint devices or activities

### Available Telemtry
|Source | Location | Purpose |
|---|---|---|
|Wazuh | Wazuh cloud | Endpoint Monitoring and Alert |
|Sysmon | Splunk `main` | Endpoint Telemetry |
|Windows Application | Splunk `soc-labs` | Endpoint Telemetry
|Windows System | Splunk `soc-labs` | Endpoint Telemetry
|Windows Security | Splunk `soc-labs` | Endpoint Telemetry

### Initial Analyst Guide
- The investigation should be evidence-driven.
- No activity should be classified as malicious solely because it is
unfamiliar or unusual.
- Findings should be supported by available telemetry and documented
with appropriate evidence.
- Where evidence is insufficient to establish a conclusion, the finding
should be documented as inconclusive or requiring further investigation.

### Investigation Status
**Status:** Investigation not yet completed
**Initial Assesment:** Medium
**Next Action:** Log Analysis using Splunk

### Evidence
Initial Evidence will be made available as the analysis advances
