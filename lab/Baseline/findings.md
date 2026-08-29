# BL-001 — Baseline Findings

## Case Information

| Field | Value |
|---|---|
| Case ID | BL-001 |
| Investigation Type | Endpoint Baseline |
| Status | Completed |
| Analyst | [COLLINS] |
| Endpoint | [KAIZEN] |
| Operating System | Windows 11 |
| Collection Date | [28 / 08 / 26] |
| Primary SIEM | Splunk Enterprise |
| Endpoint Monitoring | Wazuh + Sysmon |

---

## 1. Endpoint Identity

### Observation

The Windows endpoint was identified as `[windows]`.

The currently logged-in user was `[kaizen]`.

The endpoint was assigned the IPv4 address `[10.0.2.3]`.

### Evidence

![Endpoint Identity](../screenshots/endpoint-identity.png)

### Assessment

The endpoint identity and network information were successfully
identified and recorded as part of the baseline.

---

## 2. Local Accounts

### Observation

The endpoint contains the following local accounts:

- `[kaizen]`
- `[WDAGUtilityAccount]`

### Evidence

![Local Accounts](../screenshots/local-accounts.png)

### Assessment

The identified accounts and administrative memberships have been
recorded as part of the endpoint baseline.

No conclusion regarding malicious activity was made solely from the
presence of an account or administrative privilege.


## 3. Running Processes

### Observation

A process inventory was collected from the Windows endpoint during
baseline collection.

The inventory included standard Windows processes as well as processes
associated with installed applications and security tooling.

### Analysis

The process inventory was reviewed to establish a reference point for
future process-based investigations.

Processes were not classified as malicious solely based on unfamiliar
names or paths. Additional evidence such as process ancestry,
command-line arguments, file location, signatures and network activity
would be required before making a maliciousness determination.

### Evidence

![Running Processes](../screenshots/running-processes.png)

### Baseline Value

This process inventory will be used as a comparison point during future
investigations involving suspicious process creation.

## 4. Network Listening Ports

### Observation

Network connections and listening ports were reviewed using Windows
networking utilities.

The following listening services were observed:

| Protocol | Local Address | Port | PID | Associated Process |
|---|---|---:|---:|---|
| TCP | [address] | [port] | [PID] | [process] |
| TCP | [address] | [port] | [PID] | [process] |

### Analysis

The observed listening ports represent the network services present
during baseline collection.

These ports will serve as a reference when investigating unexpected
network exposure or newly opened services during subsequent attack
simulations.

### Evidence

![Listening Ports](../screenshots/listening-ports.png)

## 5. Windows Services

### Observation

Running Windows services were enumerated during baseline collection.

The collected service inventory included Windows operating system
services and services associated with installed software.

### Analysis

The service inventory establishes a reference for detecting potential
service-based persistence or unexpected service creation in later
investigations.

### Evidence

![Running Services](../screenshots/services.png)

## 6. Scheduled Tasks

### Observation

Scheduled tasks configured on the Windows endpoint were enumerated.

### Analysis

The scheduled-task inventory provides a baseline for identifying
unexpected task creation or modification during future attack
simulations.

A scheduled task was not classified as malicious solely because it was
unknown during baseline collection. Further investigation would be
required to establish its purpose, execution path, creator and
associated activity.

### Evidence

![Scheduled Tasks](../screenshots/scheduled-tasks.png)

## 7. Sysmon Telemetry Baseline

### Observation

Sysmon telemetry was reviewed in Splunk to determine the types and
frequency of endpoint events generated during normal lab operation.

The following Event IDs were observed:

| Event ID | Event Type | Observed |
|---:|---|---|
| 1 | Process Creation | Yes |
| 3 | Network Connection | Yes |
| 11 | File Creation | Yes |
| [ID] | [Event Type] | Yes |

### Splunk Query

```spl
[YOUR ACTUAL SPL QUERY]

```

**Use your actual Event IDs.**

Don't copy the example IDs above unless you actually observed them.

---

# 8. Wazuh Baseline

## 8. Wazuh Monitoring Status

### Observation

The Windows 11 endpoint was registered with Wazuh Cloud and the Wazuh
agent was observed to be active during baseline collection.

### Analysis

Wazuh provides endpoint monitoring and alert generation for the Windows
endpoint. The agent status confirms that the endpoint is connected to
the monitoring infrastructure at the time of baseline collection.

### Evidence

![Wazuh Agent Status](../screenshots/wazuh-agent-status.png)

## 9. Splunk Telemetry Availability

### Observation

Windows and Sysmon telemetry was queried from Splunk Enterprise.

Sysmon events were observed in the `main` index, while Windows
Application, Security and System events were observed in the `soc-lab`
index.

### Analysis

The available telemetry provides a foundation for security monitoring,
threat hunting and detection engineering within the lab.

### Evidence

![Splunk Telemetry](../screenshots/sysmon-events.png)

## Overall Assessment

The Windows 11 endpoint was successfully baselined prior to the
introduction of adversarial activity.

The baseline established reference information for:

- Endpoint identity
- User and administrative accounts
- Running processes
- Network listening services
- Windows services
- Scheduled tasks
- Sysmon telemetry
- Windows event telemetry
- Wazuh monitoring

The collected information will be used as a reference during subsequent
SOC investigations.

No malicious activity was concluded from the baseline collection alone.
Any future determination of suspicious or malicious activity will be
based on additional evidence collected during the relevant investigation.

## Next Step

The baseline will be preserved as the reference state for Project 1:
Windows Attack Detection & AI-Assisted Threat Hunting.
