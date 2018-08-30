# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:47:07 2018

@author: Akshay Jagadale
"""


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        #method ugly recursive 
#        for e in employees:
#            if e.id == id:
#                employee = e
#        res = 0
#        
#        if not employee.subordinates:
#            return employee.importance
#        else:
#            res = res + employee.importance
#            for sub in employee.subordinates:
#                res = self.getImportance(employees, sub) + res
#            return res
        
        #method 2 : Depth-First Search [Accepted]
#        emap = {e.id:e for e in employees}
#        def dfs(id):
#            employee = emap[id]
#            return employee.importance + sum(dfs(eid) for eid in employee.subordinates)
#        #print( dfs(id))
#        return dfs(id)
        

        d={e.id:e for e in employees}
        ret=0
        stk=[d[id]] #we can go straight to the employee since we have a map already
        while stk: 
            top=stk.pop()
            ret+=top.importance
            for n in top.subordinates:
                stk.append(d[n])
        return ret
        
        
        

       
peter = Employee(2,3,[])
viv = Employee(3,3,[])
francu = Employee(1,5,[2,3])        
myobj = Solution()
print(myobj.getImportance([francu,peter,viv], 1))