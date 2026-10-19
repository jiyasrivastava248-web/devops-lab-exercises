import subprocess

tests = [
    ("Read /etc/passwd", ["cat", "/etc/passwd"]),
    ("Execute Bash", ["/bin/bash", "-c", "echo Bash executed"]),
]

print("Testing commands in the current environment.")
print("These tests do not prove AppArmor enforcement.\n")

for name, command in tests:
    print(f"Test: {name}")
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=10,
    )

    print(f"Exit code: {result.returncode}")
    if result.returncode == 0:
        print("Result: Command succeeded")
    else:
        print("Result: Command failed or was blocked")

    if result.stdout:
        print(result.stdout[:500])

    if result.stderr:
        print(result.stderr[:500])

    print("-" * 40)
