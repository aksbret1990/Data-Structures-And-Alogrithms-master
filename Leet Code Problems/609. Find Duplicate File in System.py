# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:36:16 2018

@author: Akshay Jagadale
"""

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        
        #my approach
#        files = []
#        for i in paths:
#            #print(i.split(" "))
#            dirlist = i.split(" ")
#            #print()
#            for k in range(1,len(dirlist)):
#                mdict = {}
#                directory = dirlist[0]
#                wholefilename = dirlist[k]
#                name = wholefilename[:wholefilename.find('(')]
#                contents = wholefilename[wholefilename.find('(') + 1 : -1]
#                mdict['directory'] = directory
#                mdict['name'] = name
#                mdict['contents'] = contents
#                files.append(mdict)
#                #print(mdict)
#                
#                
#                
#            
#        #print(directories)
#        #print(files)
#        
#        secdict = {}
#        for i in files:
#            contents = i['contents']
#            if contents in secdict:
#                directory = i['directory']
#                filename = i['name']
#                fullpath = directory + '/' + filename
#                flist = []
#                flist.append(fullpath)
#                secdict[contents].append(fullpath)
#                
#            else:
#                directory = i['directory']
#                filename = i['name']
#                fullpath = directory + '/' + filename
#                flist = []
#                flist.append(fullpath)
#                secdict[contents] = flist
#                
#        #print(secdict)
#        
#        retlist = []
#        
#        for i in secdict.values():
#            if len(i) > 1:
#                retlist.append(i)
#                
#        return retlist
        
        
        #fastest
        
        from collections import defaultdict
        d=defaultdict(list)
        
        for i in paths:
            part=i.split()
            path=part[0]
            for j in range(1,len(part)):
                fname,content=part[j].split('(')
                fpath=path+'/'+fname
                d[content[:-1]].append(fpath)
        return [v for k,v in d.items() if len(v)>1]
                
                
            
            
        
myobj = Solution()
print(myobj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))