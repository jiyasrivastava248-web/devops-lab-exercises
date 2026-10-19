# Exercise 8: Creating a Hello World Jenkins Job



## Objective



To create a simple shell script, upload it to GitHub, configure a Jenkins Freestyle project to retrieve the script, and execute it successfully.



## 1. Create the Shell Script



Created a file named `hello-world.sh` with the following contents:



```bash

#!/bin/bash

echo "Hello, Jenkins!"

```



## 2. Push the Script to GitHub



Created a public GitHub repository named `devops-sample-code`.



**Repository URL:** https://github.com/jiyasrivastava248-web/devops-sample-code



Initialized Git, committed the script, and pushed it to the `main` branch.



Commit message: `Add hello-world.sh`



## 3. Create the Jenkins Job



Created a Freestyle project named `HelloWorld`.



**Description:**



Hello World! Jenkins job.



## 4. Configure Source Code Management



Selected Git under Source Code Management and configured the following settings:



- **Repository URL:** https://github.com/jiyasrivastava248-web/devops-sample-code.git

- **Branch Specifier:** `*/main`

- **Credentials:** None, because the repository is public.



Jenkins successfully cloned the repository and checked out the script from the `main` branch.



## 5. Configure the Build Step



Added an Execute shell build step with the following command:



```sh

sh hello-world.sh

```



Saved the job configuration.



## 6. Execute the Jenkins Job



Selected **Build Now** to execute the job and opened the build's Console Output.



The console output confirmed that the script executed successfully:



```text

Started by user Jiya Srivastava



Running as SYSTEM

Building in workspace /var/jenkins_home/workspace/HelloWorld



\+ sh hello-world.sh

Hello, Jenkins!

Finished: SUCCESS

```



## 7. Result



The `HelloWorld` Jenkins Freestyle project successfully retrieved the shell script from GitHub and executed it.



The console output displayed `Hello, Jenkins!` and the build finished with the status `SUCCESS`.



## Conclusion



This exercise demonstrated how to create a shell script, manage it using Git, push it to GitHub, configure Jenkins source code management, and execute a build successfully.





## Screenshots and Evidence

### Screenshot 2026-10-19 021949

![ Screenshot 2026-10-19 021949 ](./Screenshot%202026-10-19%20021949.png)

### Screenshot 2026-10-19 022035

![ Screenshot 2026-10-19 022035 ](./Screenshot%202026-10-19%20022035.png)

### Screenshot 2026-10-19 022255

![ Screenshot 2026-10-19 022255 ](./Screenshot%202026-10-19%20022255.png)

### Screenshot 2026-10-19 022401

![ Screenshot 2026-10-19 022401 ](./Screenshot%202026-10-19%20022401.png)

### Screenshot 2026-10-19 022457

![ Screenshot 2026-10-19 022457 ](./Screenshot%202026-10-19%20022457.png)

### Screenshot 2026-10-19 022530

![ Screenshot 2026-10-19 022530 ](./Screenshot%202026-10-19%20022530.png)


