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
        ListNode l1=list1;
        ListNode l2=list2;
        ArrayList<Integer> f=new ArrayList<>();
        while(l1!=null){
            f.add(l1.val);
            l1=l1.next;
        }
        while(l2!=null){
            f.add(l2.val);
            l2=l2.next;
        }
        Collections.sort(f);
        ListNode h=new ListNode(0);
        ListNode head=h;
        for(int i:f){
            head.next=new ListNode(i);
            head=head.next;
        }
        return h.next;

    }
}