"""
This is the ListNode class definition

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

"""
Add Element at Kth Position in Linked List

Given a Linked List, an integer k and an element, add that element at the kth position of the linked list.

class Solution:
	def addAtkthElement(self, head: ListNode, k: int, newElement: ListNode) -> ListNode:
		# add your logic here
		if k == 1:
			newElement.next = head
			return newElement
		temp=head
		
		while temp and k>2:
			k-=1
			temp=temp.next
			
			
		if temp is None:
			return head 
		newElement.next=temp.next
		temp.next=newElement
		return head
			
		
