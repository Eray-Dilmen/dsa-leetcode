> 💡 **Not:** Bu problem optimal olarak **Fast and Slow Pointers** (Hızlı ve Yavaş İşaretçiler) kalıbı ile çözülmektedir. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0019. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Sana bir bağlı listenin `head` düğümü veriliyor. Senden istenen, listenin **sondan n. düğümünü** silmen ve güncellenmiş listenin başını (head) döndürmendir.

### Example 1:
> **Input:** `head = [1,2,3,4,5], n = 2`  
> **Output:** `[1,2,3,5]`  
> **Explanation:** Sondan 2. düğüm 4'tür. Çıkarıldığında liste 1 -> 2 -> 3 -> 5 olur.

### Example 2:
> **Input:** `head = [1], n = 1`  
> **Output:** `[]`  

### Example 3:
> **Input:** `head = [1,2], n = 1`  
> **Output:** `[1]`  

---

### 1. Fast and Slow Pointers Yaklaşımı (Optimal / One-Pass)

Bu yaklaşımın temel amacı, listeyi iki kez gezmek yerine iki işaretçi (`fast` ve `slow`) arasındaki mesafeyi sabitleyerek listeyi **tek geçişte (one-pass)** taramaktır. Asimptotik olarak her iki yöntem de $O(N)$ olsa da, tek geçişli yöntem işlemci seviyesinde adım sayısını yarıya indirir ve bellek erişimini (cache) optimize eder.

**$n+1$ Boşluğu ve Dummy Node Mantığı:**
Tek yönlü bir bağlı listede bir düğümü silebilmek için, işaretçimizin silinecek düğümden **tam 1 adım geride** (önceki düğümde) durması gerekir. Bunun için `slow` ve `fast` işaretçilerini doğrudan `head` üzerinden değil, `head`'in bir adım gerisine koyduğumuz `dummy` düğümünden başlatırız. 
`fast` işaretçisini `n` adım ileri aldığımızda aralarındaki mesafe ayarlanmış olur. İkisi de `dummy`'den başladığı için, `fast` listenin sonundaki `None` değerine ulaştığında, `slow` tam olarak silinecek düğümün bir adım gerisinde kalır.

<img src="slow_behind_target.png" width="500" />

Bu sayede `slow.next = slow.next.next` işlemi güvenle çalıştırılır ve aradaki düğüm koparılır.

**Neden `return head` yerine `return dummy.next` diyoruz?**
Eğer silinmesi gereken düğüm listenin **en başındaki düğüm** ise (örneğin liste `[1,2]` ve `n=2`), silme işleminden sonra `head` değişkeni hala silinmiş olan eski ilk düğümü göstermeye devam eder. Fakat `dummy.next` her zaman listenin güncel ve gerçek başını temsil eder. Bu yüzden hata almamak için mutlaka `dummy.next` döndürülmelidir.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        for _ in range(n):
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
```

**Time Complexity:** `O(N)`  
Liste sadece bir kez baştan sona taranır (One-pass). Toplam adım sayısı yaklaşık $N$'dir.

**Space Complexity:** `O(1)`  
Sadece `dummy`, `slow` ve `fast` işaretçileri kullanıldığı için ekstra hafıza gerektirmez.

--- 

### 2. Uzunluğu Bulup Tekrar İlerleme (Brute Force / Two-Pass)

Bağlı listenin boyutunu önceden bilemediğimiz için önce listeyi tam tur gezip uzunluğunu (`lenn`) bulduğumuz, ardından hedefe ulaşmak için listeyi tekrar gezdiğimiz (Two-pass) en basit yöntemdir.

**İlk Elemanın Silinmesi (Edge Case) Sorunu:**
Eğer listenin uzunluğu `n`'e eşitse (`lenn == n`), bu listenin en başındaki ilk elemanın silineceği anlamına gelir. Eğer bu durumu manuel olarak kontrol etmezsek, `lenn - n - 1` formülü `-1` çıkar, döngü çalışmaz ve işaretçi en başta kalır. Ardından `curr.next.next` yapılmaya çalışıldığında `AttributeError: 'NoneType' object has no attribute 'next'` hatası fırlatır. Bu yüzden `lenn == n` ise doğrudan `head.next` döndürülerek ilk eleman atlanır.

```python
class SolutionBruteForce:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        lenn = 0
        while curr:
            lenn += 1
            curr = curr.next
            
        if lenn == n:
            return head.next
            
        curr = head
        
        for i in range(0, lenn-n-1):
            curr = curr.next
            
        curr.next = curr.next.next
        return head
```

**Time Complexity:** `O(N)`  
Big-O notasyonunda $O(N)$ olsa da, listeyi iki kez gezdiği için (Two-pass) toplam adım sayısı yaklaşık $2N$'dir. Pratik kullanımda optimal çözümden daha yavaştır.

**Space Complexity:** `O(1)`  
Sadece sayaç ve işaretçi değişkenleri kullanılır.