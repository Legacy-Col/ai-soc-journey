This is where our telemetry will  be coming from and how they'll be processed

# Sysmon
---> Index: main
---> Sourcetype: XmlWinEventlog:Microsoft-Windows-Sysmon\Operational
---> Events
    --> Process Creation
    --> Network Connection
    --> File Creation
    --> Registry Activities

# Application / Security / System
---> Index: soc-lab
---> Sourcetype: "WinEventLog:Application" "WinEventLog:Security" "WinEventLog:System"
---> Events
    --> Process Creation
    --> Network Connection
    --> File Creation
    --> Registry Activities
    --> etc.

# WAZUH 
---> Platform: Cloud
---> Agent: Windows 11 (VM)
---> Purpose: Endpoint Detection

# Splunk
---> Platform: Splunk Enterprise
---> Host: Windows 11 (VM)
---> Purpose: SIEM / Investigation / Detection Engineering

NB: As a SOC analyst never say something that you are not sure of and have no proof about it.
