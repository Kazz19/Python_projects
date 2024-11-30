import random 

# For the purpose of the simulation, we indicate 6 IP addresses with packets that will 
# be dropped and not allowed by the firewall

# Code based on https://www.youtube.com/watch?v=UfyF6CvL4Ts&list=PLB7R26sRn2aLhKbDDRtd7wluaX91pqAQD 



def generate_random_ip():
    return f"192.168.1.{random.randint(1,30)}"

def check_firewall_rules(ip_address,firewall_rules):
    if (ip_address in firewall_rules):
        return "block"
    else:
        return "allowed"
    
def main():  #Simulation data traffic through generation of 20 random IP addresses 
    print("---------------------------------------------------------")
    for i in range(5):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address,firewall_rules)
        id = random.randint(1,9999)
        print(f"IP: {ip_address}, Action: {action}, Identifier : {id}")
        print("---------------------------------------------------------")
        
## ----------------------------------- MAIN ----------------------------------- ## 
if __name__ == "__main__":
    
    firewall_rules = set(str)

    firewall_rules.update({
    "192.168.1.1",
    "192.168.1.4",
    "192.168.1.10",
    "192.168.1.18",
    "192.168.1.22",
    "192.168.1.24"
    })
    
    print(firewall_rules)
    main()