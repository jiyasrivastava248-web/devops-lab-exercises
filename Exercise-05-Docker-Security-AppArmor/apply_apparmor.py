import docker

IMAGE_NAME = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-security-test"
APPARMOR_PROFILE = "my-apparmor-profile"

client = docker.from_env()

print("Building Docker image...")
client.images.build(path=".", tag=IMAGE_NAME)
print(f"Image '{IMAGE_NAME}' built successfully.")

print("\nChecking AppArmor support...")
try:
    with open("/sys/module/apparmor/parameters/enabled") as file:
        enabled = file.read().strip()
except OSError:
    enabled = "Unavailable"

print(f"AppArmor enabled on this Linux environment: {enabled}")

print("\nCreating a test container with the requested AppArmor profile...")
try:
    try:
        old = client.containers.get(CONTAINER_NAME)
        old.remove(force=True)
    except docker.errors.NotFound:
        pass

    container = client.containers.create(
        IMAGE_NAME,
        name=CONTAINER_NAME,
        detach=True,
        ports={"5000/tcp": 5001},
        security_opt=[f"apparmor={APPARMOR_PROFILE}"],
    )

    print(f"Container created: {container.id[:12]}")
    print(f"Requested security option: apparmor={APPARMOR_PROFILE}")
    print("Note: this does not prove AppArmor enforcement is active.")

    container.start()
    print(f"Container status: {container.status}")

except docker.errors.APIError as error:
    print(f"Docker could not create or start the container: {error}")

finally:
    try:
        container.stop(timeout=2)
        container.remove()
        print("Test container stopped and removed.")
    except (NameError, docker.errors.NotFound, docker.errors.APIError):
        pass
