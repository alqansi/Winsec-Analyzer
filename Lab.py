feled_login = {}
totel_feled = 0

with open("login.txt", "r") as file:
            for user in file:
                if ":" not in user :
                    continue
                s = user.strip().split(":")
                us = s[0]
                st = s[1]
                if us not in feled_login:
                        feled_login[us]=0
                if st == "failed":    
                    feled_login[us]+=1 
                    totel_feled +=1
                                    

with open("secoryt_report.txt","w") as f :
     f.write("======= Secourty report =======")
     f.write(f"\nTotel failed attampets : {totel_feled}\n")
     for user , attempts in feled_login.items():
                if attempts >= 3 :
                    f.write(f"WARINING: The user : {user} has : {attempts} attempts !\n")

             

            

         