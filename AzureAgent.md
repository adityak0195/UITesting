
**Setting up Azure DevOps Thingworx agent**

Azure DevOps ThingWorx agent is responsible for executing the automation test scripts and generating reports. During the execution these scripts establish connection with TEST environment, run the automation tests and generate the reports. The agent runs on redhat linux.

![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/2563ae6a-7ec2-426a-ba6d-df20e63b5ed7)

  
**Setting up the agent**

1. Redhat Linux already comes with python distribution package
   Check all versions of python installed:

   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/2bcbffb1-0533-4730-8781-fa23960b7117)

   ***All Automation scripts are currently running on python 3.11.***
    
   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/fdbfd628-e332-4a63-a9b9-32e611ec79a5)

2. Install pip

   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/b68da794-acd4-43aa-a3c0-7ad6440da924)

3. Install Microsoft Edge distribution on linux - [Download Microsoft Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FJ)

   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/1dad7f03-d66b-47b1-a34e-8771b80d3b84)

   Check the version

   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/4b90b005-7a9f-473b-8150-8c83d90b4837)

4. Install [Microsoft Edge webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/57d34ca7-a567-406c-ba38-07151e9c0dc1)

5. Add webdriver location to PATH

   ![image](https://github.com/KB-smartProduction/UITesting/assets/133857066/5c9bd0e0-5fa6-4bf3-a457-2daa907d282c)



