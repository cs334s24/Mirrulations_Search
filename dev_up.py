import subprocess

def dev_up():
    try:
        subprocess.run(["docker", "build", "-t", "kickoff_webapp", "."], check=True)
        subprocess.run(["docker", "run", "-p", "8000:8000", "--env-file", ".env", "--name", "my_flask_container", "kickoff_webapp"], check=True)
        print("Development environment is up and running.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dev_up()