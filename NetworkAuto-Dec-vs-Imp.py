from netmiko import *



#### Example Network Automation: Declarative Vs Imperative #### 
####Utilising classes, class attributes and class functions ####


#Declarative Example
class DeclarativeExample():
    
    attr_Interface="gigabitEthernet 0/45"
    attr_ip = "2.2.9.9" 
    attr_subnet = "255.255.255.0"

    cisco_C3750X = {
        'device_type': 'cisco_ios',
        'host':   '192.168.2.1',
        'username': 'tamedcobra',
        'password': 'tanyatamirtame',
        'port' : 22,          # defaults SSH port 22
        'secret': 'tame2011',     # 
        }
    net_connect = ConnectHandler(**cisco_C3750X)

    net_connect.enable()

     
    


    def setInterfaceIPDec(self):
        
        command = ['Interface '+self.attr_Interface, 'ip address '+self.attr_ip+" "+ self.attr_subnet]        
        result = self.net_connect.send_config_set(command)
        print("New Ip address set for this interface "+self.attr_ip)

# DecEx = DeclarativeExample()
# DecEx.setInterfaceIPDec() 


#Imperative Example
class ImperativeExample:
    attr_Interface="gigabitEthernet 0/45"
    attr_ip = "10.1.1.1" 
    attr_subnet = "255.255.255.0"

   
    def CheckInterfaceIP(self):

        assignedIP =   'show ip int br | inc  GigabitEthernet0/45'
        unassigned =   'unassigned'
        Checkresult = DeclarativeExample.net_connect.send_command(assignedIP)
        
        if unassigned in Checkresult:
            print('This interface has no IP address set, setting IP.....') 
            print (Checkresult)
            ImpEX=DeclarativeExample()
            ImpEX.setInterfaceIPDec()
        else:
            print("sorry the following ip address has been set for this interface")
            print (Checkresult)        

ImpEx = ImperativeExample()
ImpEx.CheckInterfaceIP()   


