class Solution:
	def appendLists(self, list1: ListNode, list2: ListNode) -> ListNode:
		# add your logic here
		temp=list1
		while temp.next:
			temp=temp.next
		temp.next=list2
		return list1
