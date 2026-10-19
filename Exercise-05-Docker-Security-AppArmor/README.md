# Exercise 5: Docker Security with AppArmor

## Aim

To explore Docker container security using a Flask application, Docker, the Docker Python SDK, and an AppArmor security profile option.

## Technologies Used

- Python
- Flask
- Docker
- Docker Python SDK
- AppArmor
- Ubuntu on WSL2
- Visual Studio Code

## Project Structure

```text
Exercise-05-Docker-Security-AppArmor/
├── app.py
├── Dockerfile
├── requirements.txt
├── apply_apparmor.py
├── test_restricted_actions.py
├── README.md
├── Screenshot 2026-10-19 170758.png
├── Screenshot 2026-10-19 172317.png
└── Screenshot 2026-10-19 172345.png
```

## Flask Application

The Flask application displays a message confirming that it is running inside a Docker container.

Open the application in your browser at:

`http://localhost:5000`

Expected output:

> Hello, this is a secure Flask application running inside a Docker container!

## Screenshots

### Flask Application

![Flask application running in the browser](Screenshot%202026-10-19%20170758.png)

### Restricted Actions Test

![Restricted actions test output](Screenshot%202026-10-19%20172317.png)

### AppArmor Configuration Test

![AppArmor configuration test output](Screenshot%202026-10-19%20172345.png)

## Docker Image

The Docker image was built successfully and tagged as `flask-apparmor`.

The Flask application was run inside a Docker container and accessed through the browser using port 5000.

## Restricted Actions Test

The `test_restricted_actions.py` script tests the following operations:

- Reading `/etc/passwd`
- Executing Bash

Both commands succeeded in the observed test run. These results do not demonstrate that AppArmor blocked or restricted the operations.

## AppArmor Configuration Test

The `apply_apparmor.py` script uses the Docker Python SDK to:

- Build the Docker image.
- Check AppArmor availability.
- Request the `my-apparmor-profile` security option.
- Create a temporary container.
- Stop and remove the temporary container.

The requested Docker security option was:

`apparmor=my-apparmor-profile`

The test container was created and subsequently stopped and removed.

## Observed Results

| Test | Result |
|---|---|
| Docker image build | Successful |
| Flask application | Ran successfully |
| Read `/etc/passwd` | Command succeeded |
| Execute Bash | Command succeeded |
| AppArmor option requested | `apparmor=my-apparmor-profile` |
| AppArmor enabled in WSL | No (`N`) |
| AppArmor enforcement | Not verified |

## Security Limitation

The Ubuntu WSL2 environment reported `N` for `/sys/module/apparmor/parameters/enabled`. Therefore, effective AppArmor enforcement was not demonstrated.

Passing an AppArmor security option to Docker does not, by itself, prove that the profile was active or that restricted operations were blocked.

To verify enforcement, repeat this exercise in a compatible Linux environment with AppArmor enabled and a valid profile loaded.

## Conclusion

The Flask application was successfully built and run inside Docker. The Docker Python SDK was used to request an AppArmor security option and check AppArmor availability.

However, AppArmor enforcement could not be confirmed in the current WSL2 environment. The results document the successful Docker application setup and the limitation encountered while testing AppArmor.
