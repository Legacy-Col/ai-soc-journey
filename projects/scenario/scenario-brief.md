This is a briefing on what I did and the Scenario is recorded below

### INC-001 — Suspicious PowerShell Execution

- Date: 29 August 2026
- Severity: Medium — Initial
- Status: Open
- Affected Asset: Windows 11 workstation
- Detection Source: SOC monitoring infrastructure

### Analyst Briefing

The SOC has received an alert concerning unusual PowerShell activity originating from a monitored Windows workstation.
The alert indicates that PowerShell was executed in a manner that differs from the endpoint's established baseline.
The user associated with the workstation is believed to be a legitimate employee.
At this stage, the SOC does not know whether the activity is:

legitimate administrative activity,
a misconfigured application,
a security-testing activity,
or malicious execution.

### Your objective
## Determine:

What happened on the endpoint, whether the activity is malicious, how the activity was initiated, and what additional actions should be taken.

### Your investigation questions
Your final investigation should answer these:

### Initial triage
- What endpoint generated the activity?
- When did the suspicious activity begin?
- Which user/account was involved?
- What process executed?
- What was the parent process?
- What command line was used?
- Was PowerShell interacting with another process?


