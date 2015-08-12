#! *-* coding:utf-8 *-*

import wmi

def normalize(s):
    if type(s) == unicode: 
        return s.encode('utf8', 'ignore')
    else:
        return str(s)
##
# print nic info
def print_nic(nic):
	print "%-28s --> %s" % ("Caption", normalize(nic.Caption))
	print "%-28s --> %s" % ("DatabasePath", normalize(nic.DatabasePath))
	print "%-28s --> %s" % ("DefaultIPGateway", normalize(nic.DefaultIPGateway))
	print "%-28s --> %s" % ("DefaultTTL", normalize(nic.DefaultTTL))
	print "%-28s --> %s" % ("Description", normalize(nic.Description))
	print "%-28s --> %s" % ("DHCPEnabled", normalize(nic.DHCPEnabled))
	print "%-28s --> %s" % ("DHCPLeaseExpires", normalize(nic.DHCPLeaseExpires))
	print "%-28s --> %s" % ("DHCPLeaseObtained", normalize(nic.DHCPLeaseObtained))
	print "%-28s --> %s" % ("DHCPServer", normalize(nic.DHCPServer))
	print "%-28s --> %s" % ("DNSDomainSuffixSearchOrder", normalize(nic.DNSDomainSuffixSearchOrder))
	print "%-28s --> %s" % ("DNSEnabledForWINSResolution", normalize(nic.DNSEnabledForWINSResolution))
	print "%-28s --> %s" % ("DNSHostName", normalize(nic.DNSHostName))
	print "%-28s --> %s" % ("DNSServerSearchOrder", normalize(nic.DNSServerSearchOrder))
	print "%-28s --> %s" % ("DomainDNSRegistrationEnabled", normalize(nic.DomainDNSRegistrationEnabled))
	print "%-28s --> %s" % ("FullDNSRegistrationEnabled", normalize(nic.FullDNSRegistrationEnabled))
	print "%-28s --> %s" % ("GatewayCostMetric", normalize(nic.GatewayCostMetric))
	print "%-28s --> %s" % ("Index", normalize(nic.Index))
	print "%-28s --> %s" % ("InterfaceIndex", normalize(nic.InterfaceIndex))
	print "%-28s --> %s" % ("IPAddress", normalize(nic.IPAddress))
	print "%-28s --> %s" % ("IPConnectionMetric", normalize(nic.IPConnectionMetric))
	print "%-28s --> %s" % ("IPEnabled", normalize(nic.IPEnabled))
	print "%-28s --> %s" % ("IPFilterSecurityEnabled", normalize(nic.IPFilterSecurityEnabled))
	print "%-28s --> %s" % ("IPSecPermitIPProtocols", normalize(nic.IPSecPermitIPProtocols))
	print "%-28s --> %s" % ("IPSecPermitTCPPorts", normalize(nic.IPSecPermitTCPPorts))
	print "%-28s --> %s" % ("IPSecPermitUDPPorts", normalize(nic.IPSecPermitUDPPorts))
	print "%-28s --> %s" % ("IPSubnet", normalize(nic.IPSubnet))
	print "%-28s --> %s" % ("MACAddress", normalize(nic.MACAddress))
	print "%-28s --> %s" % ("PMTUBHDetectEnabled", normalize(nic.PMTUBHDetectEnabled))
	print "%-28s --> %s" % ("PMTUDiscoveryEnabled", normalize(nic.PMTUDiscoveryEnabled))
	print "%-28s --> %s" % ("ServiceName", normalize(nic.ServiceName))
	print "%-28s --> %s" % ("SettingID", normalize(nic.SettingID))
	print "%-28s --> %s" % ("TcpipNetbiosOptions", normalize(nic.TcpipNetbiosOptions))
	print "%-28s --> %s" % ("WINSEnableLMHostsLookup", normalize(nic.WINSEnableLMHostsLookup))
	print "%-28s --> %s" % ("WINSScopeID", normalize(nic.WINSScopeID))
	print "\n"

def print_nics():
	nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

	for nic in nic_configs:
		print_nic(nic)

def set_cano():
	nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

	for nic in nic_configs:
		if "[00000022] Hyper-V 虚拟以太网适配器" == nic.Caption:
			ip         = u'10.16.19.50'
			subnetmask = u'255.255.255.0'
			# gateway    = u'192.168.0.1'
			nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
			# print nic info
			print_nic(nic)

def print_result(code):
	if 0 == code:
		print "Successful completion, no reboot required."
	if 1 == code:
		print "Successful completion, reboot required."

def set_b289():
	nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

	for nic in nic_configs:
		if "{E6F42687-C3CF-434B-AC6B-D2BF6BC9A1B3}" == nic.SettingID:
			print_result(nic.EnableDHCP())
			# print nic info
			print_nic(nic)

# set_b289()
print_nics()
