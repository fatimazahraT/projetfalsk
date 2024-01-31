from os import name
from pysnmp.hlapi import *

def get_snmp_data(ip_address, community_string, oid_list):
 
    data = {}

    for oid in oid_list:
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(community_string),
                   UdpTransportTarget((ip_address, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid)))
        )

        if errorIndication:
            print(f"Erreur lors de la récupération de l'OID {oid}: {errorIndication}")
        elif errorStatus:
            print(f"Erreur lors de la récupération de l'OID {oid}: {errorStatus.prettyPrint()}")
        else:
            for varBind in varBinds:
                value = varBind[1]
                if oid == "1.3.6.1.2.1.25.2.2.0":
                    total_ram_bytes = int(value)
                    total_ram_gb = total_ram_bytes / (1024 ** 3)
                    data["Total Memory"] = f"{total_ram_gb:.2f} GB"
                elif oid == "1.3.6.1.2.1.25.2.3.1.6.1":
                    used_ram_bytes = int(value)
                    used_ram_gb = used_ram_bytes / (1024 ** 3)
                    data["Used Memory"] = f"{used_ram_gb:.2f} GB"
                    available_ram_gb = total_ram_gb - used_ram_gb
                    data["Available Memory"] = f"{available_ram_gb:.2f} GB"
                else:
                    data[oid] = value.prettyPrint()

    return data

# ...
if name == "main":
    device_ip = "192.168.11.111"
    community_string = "SNS"  

    oids_to_query = ["1.3.6.1.2.1.25.2.2.0",   
                     "1.3.6.1.2.1.25.2.3.1.6.1",  
                     "1.3.6.1.2.1.25.2.3.1.5.1",   
                     "1.3.6.1.2.1.25.3.3.1.2.10",  
                     "1.3.6.1.2.1.25.3.3.1.2.11",   
                     "1.3.6.1.2.1.25.3.3.1.2.8",   
    
                     "1.3.6.1.2.1.25.2.3.1.6.2"]   

    snmp_data = get_snmp_data(device_ip, community_string, oids_to_query)

    print("Données récupérées du périphérique:")
    for oid, value in snmp_data.items():
        print(f"{oid}: {value}")