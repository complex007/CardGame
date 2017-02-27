import ssdp

yeelight_master = ssdp.discover(":yeelink:yeebox")
yeeIP = yeelight_master[0].location
print 'IP of gateway: ', yeeIP