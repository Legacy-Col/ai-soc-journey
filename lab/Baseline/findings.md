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
