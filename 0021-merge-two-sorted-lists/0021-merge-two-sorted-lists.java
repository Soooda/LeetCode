/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) {
            return null;
        }
        
        ListNode ret = new ListNode();
        ListNode current = ret;
        
        while (list1 != null || list2 != null) {
            if (list1 == null) {
                current.val = list2.val;
                list2 = list2.next;
            } else if (list2 == null) {
                current.val = list1.val;
                list1 = list1.next;
            } else if (list1.val < list2.val) {
                current.val = list1.val;
                list1 = list1.next;
            } else {
                current.val = list2.val;
                list2 = list2.next;
            }
            
            if (list1 != null || list2 != null) {
                current.next = new ListNode();
            }
            current = current.next;
        }
        
        return ret;
    }
}