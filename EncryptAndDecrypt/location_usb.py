import pyudev
import psutil

def getLocation():
    context = pyudev.Context()
    removable = [device for device in context.list_devices(subsystem='block', DEVTYPE='disk') if device.attributes.asstring('removable') == "1"]
    for device in removable:
        partitions = [device.device_node for device in context.list_devices(subsystem='block', DEVTYPE='partition', parent=device)]
        for p in psutil.disk_partitions():
            if p.device in partitions:
                mntpoint = p.mountpoint
                print(p.device + ' => ' + mntpoint)
                return mntpoint

print(getLocation())
