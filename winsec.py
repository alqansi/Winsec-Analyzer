import xml.etree.ElementTree as ET
from Evtx.Evtx import Evtx

with Evtx("private_data/security.evtx") as log:

    Total_Failed_Logins = 0
    failed_users = {}

    for record in log.records():

        root=ET.fromstring(record.xml())
        event =root.find(".//{*}EventID")
        
        if event is not None and event.text == "4625" :
            Total_Failed_Logins +=1
            user = root.find(".//{*}Data[@Name='TargetUserName']")
            if user is not None and user.text is not None:
                if user.text not in failed_users :
                 failed_users[user.text]=0
                failed_users[user.text]+=1
                   
unknown_login = Total_Failed_Logins-sum(failed_users.values())            
with open("reports/security_report.txt", "w") as f:
    f.write("===== Security Report =====\n")
    f.write(f"Total failed logins: {Total_Failed_Logins}\n")
    f.write(f"Failed login without username :{unknown_login}\n\n")
    f.write("Failed logins by user :\n")
    
    for user, attempts in failed_users.items():
        f.write(f"{user}: {attempts}\n")


        if attempts >= 3:
            f.write(f"WARNING: {user} has {attempts} failed logins\n")

print("Security report created successfully '_' ")            
             

            

         