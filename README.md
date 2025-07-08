## Automation Testing
--------

## Pre-requisites for Automation Tests

- [python](https://www.python.org/downloads/)
- [python-selenium](https://pypi.org/project/selenium/)
- [edge webdriver](https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp#Download%20Microsoft%20Edge%20Webdriver)


**[Setting up Azure DevOps Thingworx agent](https://github.com/KB-smartProduction/UITesting/blob/main/docs/AzureAgent.md)**



## Azure DevOps pipelines

Automation Test scripts run are orchestrated by three pipelines in CVS, RVS and CAPS environments.

- [QA-UI-TWX-CVS](https://github.com/KB-smartProduction/UITesting/blob/main/CVS-Automation-Testing.yml)        [![Build Status](https://dev.azure.com/knorrbremse/idib-dev-thingworx/_apis/build/status%2FTWX-UI-AutomationTesting%2FQA-UI-TWX-CVS?branchName=main)](https://dev.azure.com/knorrbremse/idib-dev-thingworx/_build/latest?definitionId=777&branchName=main)

- [QA-UI-TWX-RVS](https://github.com/KB-smartProduction/UITesting/blob/main/RVS-Test-Automation.yml)      [![Build Status](https://dev.azure.com/knorrbremse/idib-dev-thingworx/_apis/build/status%2FTWX-UI-AutomationTesting%2FQA-UI-TWX-RVS?branchName=main)](https://dev.azure.com/knorrbremse/idib-dev-thingworx/_build/latest?definitionId=778&branchName=main)

- [QA-UI-TWX-CAPS-RVS](https://github.com/KB-smartProduction/UITesting/blob/main/CAPS_Test_Automation.yml)   [![Build Status](https://dev.azure.com/knorrbremse/idib-dev-thingworx/_apis/build/status%2FTWX-UI-AutomationTesting%2FQA-UI-TWX-CAPS-RVS?branchName=main)](https://dev.azure.com/knorrbremse/idib-dev-thingworx/_build/latest?definitionId=779&branchName=main)

## Servers

Below servers are used to run automation tests and the timing of the runs schedulued.

> [!NOTE]
>*As of now, these pipelines are NOT shutting down the Azure server VMs on which the tests are being run.*

|Dept|Server|Schedule|
|----|------|--------|
|CVS|KECTEST|​Scheduled run at 7 AM CET|
|​RVS|​MILTEST, PNATEST, MLKTEST|​Scheduled run at 7  AM CET|
|​CAPS|​KBATEST|​Scheduled run at 7  AM CET|

The manual test cases covered are documented under [TWX-19](https://knorr-bremse.atlassian.net/browse/TWX-19).

The test results and auto generated report can be found from published aritfacts under the run of a pipeline. 

Results are further bifercated into two folders. 

- **TestImages**: contain screenshots/images of the validated selections and clicks.

- **Test reports**: contain a report in html format mentioning no of test cases passed and failed.

The automation scripts are written in **Python 3.11.4** and are availabe under **UITesting repository on Github**.

## Development

Objectives - To ensure quality of software development by validating test cases using automation test scripts. 

Working procedures and code snippets can be found [here](https://github.com/KB-smartProduction/UITesting/blob/main/docs/Development.md).

