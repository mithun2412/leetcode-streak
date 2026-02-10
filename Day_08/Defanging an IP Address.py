class Solution:
    def defangIPaddr(self, address: str) -> str:
    #  return address.replace(".", "[.]")
        s=""
        for i in range(len(address)):
            if address[i]==".":
                s+="[.]"
            else:
                s+=address[i]
        return s