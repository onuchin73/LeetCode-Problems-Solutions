# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

address = "1.1.1.1"


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


print(Solution().defangIPaddr(address))
