import docker

def check_docker_version():
    """
    Check and print the Docker version.
    """
    try:
        client = docker.from_env()
        version_info = client.version()
        print("Docker Version:")
        print(f"  Version: {version_info['Version']}")
        print(f"  API Version: {version_info['ApiVersion']}")
        print(f"  Go Version: {version_info['GoVersion']}")
        print(f"  Git Commit: {version_info['GitCommit']}")
        print(f"  OS/Arch: {version_info['Os']}/{version_info['Arch']}")
    except Exception as e:
        print(f"Error retrieving Docker version: {e}")

def list_running_containers():
    """
    List and print the running Docker containers.
    """
    try:
        client = docker.from_env()
        containers = client.containers.list()
        if containers:
            print("\nRunning Containers:")
            for container in containers:
                print(f"  Container ID: {container.id}")
                print(f"  Name: {container.name}")
                print(f"  Image: {container.image.tags}")
                print(f"  Status: {container.status}")
                print("-" * 20)
        else:
            print("\nNo containers are currently running.")
    except Exception as e:
        print(f"Error retrieving running containers: {e}")

if __name__ == "__main__":
    print("Checking Docker setup...\n")
    check_docker_version()
    list_running_containers()