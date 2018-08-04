# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 03:19:07 2018

@author: Akshay Jagadale
"""

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
#        mydcit = {}
#        for string in cpdomains:
#            visits, domain = string.split(" ")
#            visits = int(visits)
#            subdomains = domain.split(".")
#           
#            
#            con = str()
#            subdomains.reverse()
#
#            
#            for i in subdomains:
#                if subdomains.index(i) == 0:
#                    domadd = i + con  
#                else:
#                    domadd = i + '.' + con
#                    
#                con = domadd 
#                if domadd in mydcit.keys():
#                    mydcit[domadd] = mydcit[domadd] + visits
#                else:
#                    mydcit[domadd] = visits
#
#        #print (mydcit)        
#        res = []
#        for i in mydcit:
#            res.append(str(mydcit[i]) + ' ' + i)
        
        
        mydict = {}
        for string in cpdomains:
            visits, domain = string.split(" ")
            visits = int(visits)
            cdomains = domain.split(".")
            
            
            for i in range(len(cdomains)):
                item = '.'.join(cdomains[i:])
                if item not in mydict:
                    mydict[item] = visits
                else:
                    mydict[item] += visits
            
        return [" ".join((str(v),k)) for k,v in mydict.items()]
        
myobj = Solution()
res = myobj.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(res)