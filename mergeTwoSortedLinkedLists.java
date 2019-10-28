/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    ListNode l3 = null;    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {    
        ListNode dummyNode = new ListNode(99); // initialize to some random variable, we're going to ignore anyway
      
        ListNode cursor = dummyNode; 
        while(true)  
        { 
            if(l1 == null) 
            { 
                cursor.next = l2; 
                break; 
            } 
            if(l2 == null) 
            { 
                cursor.next = l1; 
                break; 
            } 
            if(l1.val <= l2.val) 
            { 
                cursor.next = l1; 
                l1 = l1.next; 
            }  
            else
            { 
                cursor.next = l2; 
                l2 = l2.next; 
            } 
            cursor = cursor.next; 
        } 
        return dummyNode.next; // ignoring the initial element 0
        }
}