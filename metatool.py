import os
import subprocess
import platform

class MetaTool:
    def __init__(self):
        self.os_platform = platform.system()
        if self.os_platform != "Windows":
            raise EnvironmentError("MetaTool is designed to run on Windows systems only.")

    def check_ping(self, host='8.8.8.8'):
        """Check network connectivity by pinging a host."""
        print(f"Pinging {host}...")
        command = ['ping', '-n', '4', host]
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            print("Network is up and running.")
        else:
            print("Network connectivity issues detected.")

    def flush_dns(self):
        """Flush DNS cache to improve connectivity."""
        print("Flushing DNS Resolver Cache...")
        command = ["ipconfig", "/flushdns"]
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            print("DNS Resolver Cache flushed.")
        else:
            print("Failed to flush DNS Resolver Cache.")

    def display_network_info(self):
        """Display the network configuration details."""
        print("Fetching network configuration details...")
        command = ["ipconfig", "/all"]
        subprocess.run(command)

    def reset_network(self):
        """Reset network settings to default to fix connectivity issues."""
        print("Resetting network settings...")
        try:
            subprocess.run(["netsh", "winsock", "reset"], check=True)
            subprocess.run(["netsh", "int", "ip", "reset"], check=True)
            print("Network settings reset successfully. Please restart your computer.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to reset network settings: {e}")

if __name__ == "__main__":
    tool = MetaTool()
    tool.display_network_info()
    tool.check_ping()
    tool.flush_dns()
    tool.reset_network()