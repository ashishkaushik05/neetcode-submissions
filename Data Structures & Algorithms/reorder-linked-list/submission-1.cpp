class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head || !head->next) return;

        // 1. Find middle
        ListNode* s = head;
        ListNode* f = head;
        while(f->next && f->next->next){
            s = s->next;
            f = f->next->next;
        }

        // 2. Split into two halves
        ListNode* second = s->next;
        s->next = nullptr;  // terminate first half

        // 3. Reverse second half
        ListNode* prev = nullptr;
        while(second){
            ListNode* nxt = second->next;
            second->next = prev;
            prev = second;
            second = nxt;
        }
        second = prev;

        // 4. Merge alternately
        ListNode* first = head;
        while(second){
            ListNode* t1 = first->next;
            ListNode* t2 = second->next;
            first->next = second;
            second->next = t1;
            first = t1;
            second = t2;
        }
    }
};