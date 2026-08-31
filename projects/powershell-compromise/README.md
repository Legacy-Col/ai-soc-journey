This is a project tutorial that was done in order to test my analyst skills and also to build detection knowledge and below is the project guide 

### Project 1 — Suspicious PowerShell Activity & Endpoint Compromise
Level
Intermediate

Primary objective
Detect, investigate, and respond to suspicious PowerShell activity on a Windows endpoint using:

Kali Linux — attack simulation
Windows 11 — victim endpoint
Sysmon — endpoint telemetry
Wazuh Cloud — endpoint detection/alerting
Splunk Enterprise — SIEM/investigation
n8n — SOAR
AI — analyst assistance
MITRE ATT&CK — adversary behavior mapping

But we're not connecting everything at once.

We'll build the project progressively:

                    PROJECT 1
                        │
          ┌─────────────┴─────────────┐
          │                           │
       ATTACK                       TELEMETRY
          │                           │
       Kali ───────► Windows ◄──── Sysmon
                         │             │
                         ▼             │
                       Wazuh           │
                         │             │
                         └──────┐      │
                                ▼      ▼
                               Splunk
                                  │
                                  ▼
                              Investigation
                                  │
                           ┌──────┴──────┐
                           │             │
                          AI            n8n
                           │             │
                           └──────┬──────┘
                                  ▼
                           Analyst Decision
                                  │
                                  ▼
                            Final Report































                            
