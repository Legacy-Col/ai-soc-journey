# Authentication Event Detection Engine

## Project Overview

This project implements a basic Python-based security event
processor that analyzes authentication events to identify
repeated failed login attempts.

It uses Python data structures, loops, conditionals, and
threshold-based detection logic to summarize authentication
activity and flag potentially suspicious IP addresses.

## Objectives

- Process authentication event records.
- Count successful and failed login attempts.
- Identify unique IP addresses.
- Aggregate failed attempts by IP address.
- Classify overall authentication activity.
- Identify IP addresses exceeding a configured threshold.
- Detect and report unexpected event statuses.

## Technologies

- Python 3
- Python dictionaries
- Lists
- Sets
- Loops and conditionals

## Detection Logic

### Overall classification

| Failed attempts | Classification |
| --------------- | -------------- |
| 0–2             | NORMAL         |
| 3–4             | WARNING        |
| 5 or more       | CRITICAL       |

### Individual IP detection

An IP address is flagged when it generates three or more
failed login attempts in the processed dataset.

## Test Results

The combined test dataset contains:

- 12 authentication events
- 9 failed attempts
- 3 successful attempts
- 3 unique IP addresses

The overall classification was CRITICAL.

The IP address 192.168.1.25 generated five failed attempts
and was flagged by the individual IP detection rule.

## Unexpected Event Handling

Events with statuses other than Success or Failure are
recorded separately and reported for further review.

They are not automatically classified as malicious.

## Limitations

- Detection thresholds are static.
- Events are analyzed as one dataset, without time-window
  analysis.
- The system does not correlate events across users,
  devices, or authentication services.
- IP addresses alone do not establish attacker identity.
- A threshold alert is an investigative lead, not proof
  of account compromise.
- The project currently uses a manually defined dataset
  rather than live security telemetry.

## Future Improvements

- Add timestamps and time-window-based detection.
- Detect repeated failures against individual accounts.
- Introduce configurable thresholds.
- Read events from CSV or JSON files.
- Add structured alert output.
- Integrate with a SIEM or SOAR platform.

## Learning Outcomes

This project demonstrates the use of Python for basic
security event processing, data aggregation, rule-based
detection, and alert reporting.
