# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:15:33 2018

@author: Akshay Jagadale
"""

class Solution:
    def cross(self, A, B, C):
        p1 = [B[0] - A[0], B[1] - A[1]]
        p2 = [C[0] - A[0], C[1] - A[1]]
        return (p1[0] * p2[1] - p1[1] * p2[0])/2

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        listABC = [[A, B, C] for A in points for B in points for C in points if A != B and B != C and A != C]
        area = 0
        for item in listABC:
            if area < self.cross(item[0], item[1], item[2]):
                area = self.cross(item[0], item[1], item[2])
        return area
