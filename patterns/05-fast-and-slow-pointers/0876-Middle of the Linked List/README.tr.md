> 💡 **Not:** Bu problem optimal olarak **Fast and Slow Pointers** (Hızlı ve Yavaş İşaretçiler) kalıbı ile çözülmektedir. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

Sana tek yönlü bir bağlı listenin (singly linked list) `head` düğümü veriliyor. Senden istenen, bu bağlı listenin **orta düğümünü** döndürmendir.

Eğer ortada iki tane düğüm varsa (liste uzunluğu çift sayıysa), **ikinci orta düğümü** döndürmelisin.

### Example 1:
> **Input:** `head = [1,2,3,4,5]`  
> **Output:** `[3,4,5]`  
> **Explanation:** Listenin orta düğümü 3 değerine sahip düğümdür.

### Example 2:
> **Input:** `head = [1,2,3,4,5,6]`  
> **Output:** `[4,5,6]`  
> **Explanation:** Listenin uzunluğu çift olduğu için ortada 3 ve 4 var. Bizden ikincisi istendiği için 4 değerine sahip düğümü (ve sonrasını) döndürüyoruz.

---

### Türkçe Açıklama

Bağlı listelerin dizilerden (array) en büyük farkı, boyutlarını (eleman sayısını) önceden bilemememizdir. Bu soruda listenin tam ortasını bulmamız isteniyor. Bunu yapmanın en verimsiz yolu listeyi baştan sona sayıp tekrar başa dönmektir. En optimal yolu ise işaretçileri farklı hızlarda koşturmaktır.

---

### 1. Fast and Slow Pointers Yaklaşımı (Optimal / Tek Tur)

Bağlı bir listenin ortasını "tek bir turda" (One Pass) bulmanın en zekice yolu iki farklı hızda hareket eden işaretçi kullanmaktır (Tavşan ve Kaplumbağa mantığı).

**Nasıl Çalışır?**
`head` düğümünden başlayan iki adet işaretçi tanımlarız: `slow` (yavaş) ve `fast` (hızlı)[cite: 16].
* `slow` işaretçisi her adımda **1 düğüm** ileri gider (`slow = slow.next`)[cite: 16].
* `fast` işaretçisi her adımda **2 düğüm** ileri gider (`fast = fast.next.next`)[cite: 16].

`fast` işaretçisi `slow` işaretçisinden tam iki kat daha hızlı ilerler. Bu matematiksel bir gerçektir ki; hızlı olan işaretçi listenin en sonuna ulaştığında, yavaş olan işaretçi tam olarak yolun yarısında, yani **listenin ortasında** kalmış olacaktır.
Döngüdeki `while (fast and fast.next):` kontrolü, hızlı işaretçinin 2 adım atarken boşluğa (None) düşüp hata (`NullReferenceException`) vermesini engeller[cite: 16].

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        return slow
```

**Time Complexity:** `O(N)`  
Listeyi sadece bir kez gezeriz. `fast` işaretçisi $N/2$ adımda sona ulaştığı için tek turda (One Pass) çözüm bulunmuş olur. Zaman karmaşıklığı lineerdir.

**Space Complexity:** `O(1)`  
Sadece `slow` ve `fast` olmak üzere iki adet işaretçi kullandığımız için ekstra hafıza (yeni bir dizi vb.) kullanılmaz[cite: 16].

--- 

### 2. Uzunluğu Bulup Tekrar İlerleme Yaklaşımı (Brute Force / İki Tur)

En temel ve akla ilk gelen kaba kuvvet (brute force) yöntemidir. Madem boyutu bilmiyoruz, o zaman önce tüm listeyi baştan sona bir kez gezer ve eleman sayısını sayarız.

1. Bir `curr` işaretçisi ile listeyi sonuna kadar gezip `lenght` değişkenini artırırız.
2. Toplam uzunluğu bulduktan sonra, orta noktayı bulmak için tam sayı bölmesi (`lenght // 2`) yaparız.
3. `curr` işaretçisini tekrar en başa (`head`) alırız.
4. Bulduğumuz `middle` değeri kadar `for` döngüsü ile tekrar ilerleriz. Döngü bittiğinde işaretçimiz tam olarak orta düğümün üzerinde durmuş olur.

```python
class SolutionBruteForce:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        lenght = 0
        
        curr = head
        
        while (curr):
            lenght += 1
            curr = curr.next
            
        middle = lenght//2 # tam sayı bölmesi
        
        curr = head
        
        for i in range(0, middle):
            curr = curr.next
            
        return curr
```

**Time Complexity:** `O(N)`  
Listeyi uzunluğu bulmak için bir tam tur ($N$ adım) ve orta noktaya gelmek için yarım tur ($N/2$ adım) geziyoruz. Toplamda $O(N)$ zaman alsa da, optimal çözüme kıyasla yavaştır çünkü aynı elemanların üzerinden iki kez geçmiş oluruz.

**Space Complexity:** `O(1)`  
Sadece sayaç ve takip amaçlı birkaç değişken (`lenght`, `middle`, `curr`) kullanılmıştır.