template = """     <host>
            <host>*</host>
            <name>*</name>
            <templates>
                <template>
                    <name>Template App HTTP Service</name>
                </template>
                <template>
                    <name>Template App HTTPS Service</name>
                </template>
                <template>
                    <name>Template Module ICMP Ping</name>
                </template>
            </templates>
            <groups>
                <group>
                    <name>Discovered hosts</name>
                </group>
                <group>
                    <name>Hypervisors</name>
                </group>
                <group>
                    <name>Linux servers</name>
                </group>
                <group>
                    <name>Templates</name>
                </group>
                <group>
                    <name>Templates/Applications</name>
                </group>
                <group>
                    <name>Templates/Databases</name>
                </group>
                <group>
                    <name>Templates/Modules</name>
                </group>

                <group>
                    <name>Templates/Network devices</name>
                </group>
                <group>
                    <name>Templates/Operating systems</name>
                </group>
                <group>
                    <name>Templates/Server hardware</name>
                </group>
                <group>
                    <name>Templates/Virtualization</name>
                </group>
                <group>
                    <name>Virtual machines</name>
                </group>
                <group>
                    <name>Zabbix servers</name>
                </group>
            </groups>
            <interfaces>
                <interface>
                    <useip>NO</useip>
                    <ip/>
                    <dns>*</dns>
                    <port>80</port>
                    <interface_ref>if1</interface_ref>
                </interface>
            </interfaces>
            <inventory_mode>DISABLED</inventory_mode>
            </host>"""

file1 = open('modif.txt','r')
file2 = open('import.xml','a')
Lines = file1.readlines()
for line in Lines:

    modif_template = template.replace("*",line.rstrip())
    file2.writelines(modif_template)



