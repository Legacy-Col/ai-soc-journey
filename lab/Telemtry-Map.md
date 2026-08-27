This is where our telemetry will  be coming from and how they'll be processed

# Sysmon
---> Index: main
---> Sourcetype: XmlWinEventlog:Microsoft-Windows-Sysmon\Operational
---> Events
    --> Process Creation
    --> Network Connection
    --> File Creation
    --> Registry Activities

# Windows Application / Security / System

---> Index: soc-lab
---> Sourcetypes:
     --> WinEventLog:Application
     --> WinEventLog:Security
     --> WinEventLog:System

---> Purpose:
     --> Windows operating system and security telemetry

---> Event types:
     --> To be identified and documented based on observed Event IDs

# Wazuh

---> Platform: Wazuh Cloud
---> Agent: Windows 11 VM
---> Purpose:
     --> Endpoint security monitoring
     --> Alert generation
     --> Log collection
     --> Security event analysis

# Splunk

---> Platform: Splunk Enterprise
---> Host: Windows 11 VM
---> Purpose:
     --> SIEM
     --> Security investigation
     --> Threat hunting
     --> Detection engineering
     --> Event correlation

NB: As a SOC analyst never say something that you are not sure of and have no proof about it.

# Evidence
---> !Index and Sourcetype 
    --> ScreenShots/Telemetry/index-sourcety.png
---> !WAZUH Agent status
    --> ScreenShots/Telemetry/"WAZUH DASH.png"
---> !Sysmon Events
    --> ScreenShots/Telemtry/event-code--mon.png
---> !EventCode for Windows Event Logs
    --> ScreenShots/Telemtry/eventcode.png
    
