import subprocess

def dev_down():
    try:
        subprocess.run(["docker", "stop", "my_flask_container"], check=True)
        subprocess.run(["docker", "rm", "my_flask_container"], check=True)
        print("Development environment has been stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dev_down()
