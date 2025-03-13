import json
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("{:-<50} {:-<20} {:-<6} {:-<6}".format("", "", "", ""))

for item in data["imdata"][:3]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    
    print("{:<50} {:<20} {:<6} {:<6}".format(dn, descr, speed, mtu))
