from collections import namedtuple

Thing = namedtuple('Thing',['name','connection','endpoint'])

a = Thing('Test!!','Ethernet1','router2')
print(a.name)


# Using a variable to pull out a specific value:
# hint: getattr

print(getattr(a,'connection'))

setofdata = {
    'leaf1001': Thing('leaf1001', 'Eth1/1', 'Spine101'),
    'Spine101': Thing('Spine101', 'Eth1/48', 'leaf1001'),
}
print(setofdata["leaf1001"].connection)
print(getattr(setofdata["Spine101"],"endpoint"))