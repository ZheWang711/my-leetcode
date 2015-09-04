__author__ = 'WangZhe'
from collections import deque

class Node:
    __slots__ = 'index'

    def __init__(self, index):
        '''
        :type index: int
        :rtype: int
        '''
        self.index = index

    def __str__(self):
        return str(self.index)


class Graph:
    def __init__(self):
        self.outgoing = {}  # self.outgoing[index1][index2] = 1 or None

    def build_graph(self, array):
        '''
        :type array: List[int]
        '''
        for i in range(len(array) - 1):
            self.outgoing[i] = {}
            for j in range(i + 1, min(array[i] + i + 1, len(array))):
                self.outgoing[i][j] = 1

    def BFS(self, end):
        distance = [0 for i in range(end + 1)]
        explored = [False for i in range(end + 1)]
        explored[0] = True
        queue = deque([0])
        while len(queue) != 0:
            head = queue.popleft()
            if head == end:
                return distance[head]
            else:
                for i in self.outgoing[head].keys():
                    if not explored[i]:
                        distance[i] = distance[head] + 1
                        if i == end:
                            return distance[i]
                        else:
                            explored[i] = True
                            queue.append(i)


    def solution(self, array):
        self.build_graph(array)
        return self.BFS(len(array) - 1)

class Solution(object):


    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy algorithm

        distance = 0
        current = 0

        while current <= len(nums) - 1:
            if current == len(nums) - 1:
                return distance
            elif current + nums[current] >= len(nums) - 1:
                return distance + 1
            else:
                max_next = (None, -float('inf'))
                for i in range(1, nums[current] + 1):
                    if max_next[1] < i + nums[i + current]:
                        max_next = (i, i + nums[i + current])
                current = current + max_next[0]
                distance += 1

        return distance





if __name__ == '__main__':
    print(Solution().jump([2,3,1,1,4]))




