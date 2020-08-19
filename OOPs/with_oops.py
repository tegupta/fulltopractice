import os

class Tomcat:
    def get_details_for_each_tomcat(self,server_xml):
        self.tcf=server_xml
        self.th=os.path.dirname(os.path.dirname(server_xml))
        return None

    def display_details(self):
            print(f'The tomcat config file is: {self.tcf}\n The tomcat home is: {self.th}')
            return None




def main():

    tomcat7=Tomcat()
    tomcat9=Tomcat()
    tomcat7.get_details_for_each_tomcat("/home/Automation/tomcat7/conf/server.xml")
    #tomcat7_cf="/home/Automation/tomcat7/conf/server.xml"
    tomcat9.get_details_for_each_tomcat("/home/Automation/tomcat9/conf/server.xml")

    #tomcat9_cf="/home/Automation/tomcat9/conf/server.xml"

    tomcat7.display_details()
    tomcat9.display_details()

    return None


if __name__=="__main__":
    main()