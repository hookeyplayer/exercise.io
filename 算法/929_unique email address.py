# Input: ["test.email+alex@leetcode.com",
# "test.e.mail+bob.cathy@leetcode.com",
# "testemail+david@lee.tcode.com"]
# 用户名中如果包含有'.'，那么把这个'.'给去掉
# 如果用户名中有'+'，那么把加号以及后面的用户名部分全部去掉


# Output: 2

# Explanation: "testemail@leetcode.com","testemail@lee.tcode.com" receive mails
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
        	# elements = email.split('@')
        	# email_set.add(elements[0].split('+')[0].replace('.', '') + elements[1])
        	name, domain = email.split('@')
        	name = name.split('+')[0].replace('.', '')
        	email_set.add(name + '@' + domain)
        return len(email_set)

emails = ["test.email+alex@leetcode.com", 
"test.e.mail+bob.cathy@leetcode.com", 
"testemail+david@lee.tcode.com"]
a = Solution()
print(a.numUniqueEmails(emails))