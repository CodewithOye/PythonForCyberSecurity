import time

ipAddress = input("What is your ip Address ? ")


def nmap(ipAddress):
    print(f"Ip address Attacked {ipAddress}")


print(f"Attacking {ipAddress}")
time.sleep(4)
nmap(ipAddress)
