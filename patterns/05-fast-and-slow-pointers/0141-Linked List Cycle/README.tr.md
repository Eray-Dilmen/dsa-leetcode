> 💡 **Not:** Bu problem optimal olarak **Fast and Slow Pointers** (Hızlı ve Yavaş İşaretçiler) kalıbı ile çözülmektedir. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Sana bir bağlı listenin `head` düğümü veriliyor. Bu bağlı listenin içinde bir **döngü (cycle)** olup olmadığını belirlemen isteniyor.

Eğer listedeki bir düğümün `next` işaretçisi sürekli takip edildiğinde daha önce geçilmiş bir düğüme tekrar ulaşılabiliyorsa, bu listede bir döngü var demektir. 

Eğer döngü varsa `true`, yoksa `false` döndürmelisin.

### Example 1:
> **Input:** `head = [3,2,0,-4], pos = 1`  
> **Output:** `true`  
> **Explanation:** Bağlı listenin sonundaki düğüm (-4), 1. indeksteki düğüme (2) geri bağlandığı için bir döngü oluşmuştur.

### Example 2:
> **Input:** `head = [1,2], pos = 0`  
> **Output:** `true`  
> **Explanation:** Son düğüm (2), 0. indeksteki düğüme (1) bağlandığı için döngü vardır.

### Example 3:
> **Input:** `head = [1], pos = -1`  
> **Output:** `false`  
> **Explanation:** Bağlı listede döngü yoktur, düz bir şekilde biter.

---

### 1. Fast and Slow Pointers Yaklaşımı (Optimal)

Bir bağlı listede döngü olup olmadığını bulmanın bellek (space) açısından en verimli ve standart yolu Floyd'un Tavşan ve Kaplumbağa algoritmasıdır.

**Nasıl Çalışır?**
Aynı anda `head` düğümünden başlayan iki işaretçi (`slow` ve `fast`) tanımlarız. `slow` işaretçisi her adımda 1 düğüm ilerlerken, `fast` işaretçisi her adımda 2 düğüm ilerler. Eğer listede döngü yoksa, hızlı olan işaretçi kısa sürede listenin sonuna (`None`) ulaşır. Fakat eğer bir döngü (çember) varsa, hızlı olan işaretçi o çemberin içinde dönmeye başlar ve eninde sonunda yavaş olan işaretçiye arkadan yetişip onunla aynı düğümde buluşur (`slow == fast`).

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False
```

**Önemli Uygulama Detayı:**
`if slow == fast:` kontrolünün işaretçiler ilerletildikten *sonra* yapılması kritik bir detaydır. Eğer bu kontrol `while` döngüsünün en başında, işaretçiler hareket etmeden yapılırsa; döngü içermeyen tek düğümlü bir listede (örn. `head = [1], pos = -1`) algoritma hatalı biçimde `True` döndürür. Bunun nedeni `slow` ve `fast` işaretçilerinin başlangıçta aynı `head` düğümünde bulunmasıdır.

**Time Complexity:** `O(N)`  
Döngü varsa iki işaretçi lineer zaman içinde kesişir, döngü yoksa zaten `N/2` adımda algoritma sonlanır.

**Space Complexity:** `O(1)`  
Sadece iki adet işaretçi (`slow` ve `fast`) kullanıldığı için ekstra hafıza maliyeti yoktur.

--- 

### 2. Hash Set Yaklaşımı (Alternatif)

İşaretçi matematiği kullanmadan, geçtiğimiz yolları bir yere not alarak (Set kullanarak) döngüyü bulduğumuz yöntemdir. 

**Nasıl Çalışır?**
Listeyi gezerken uğradığımız her düğümü `sett` adlı kümeye ekleriz. Eğer döngü yoksa liste sonuna (`null`) gelene kadar döngü devam edecek ve doğal yollardan sonlanıp `False` döndürecektir. Ancak döngü varsa, daha önce kümeye eklediğimiz bir düğüme tekrar denk geliriz. Bu durumda zaten döngünün içindeyiz diyerek anında `return True` ile çıkış yaparız.

```python
class SolutionHashSet:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        sett = set()
        
        while(curr):
            if curr in sett:
                return True
            sett.add(curr)
            curr = curr.next
            
        return False
```

**Time Complexity:** `O(N)`  
Listeyi baştan sona bir kez gezeriz, Set içine ekleme ve arama işlemleri ortalamada `O(1)` zaman alır.

**Space Complexity:** `O(N)`  
Listedeki tüm düğümleri hafızada (Set içinde) tuttuğumuz için doğrusal bir alan karmaşıklığı oluşur. Optimal olmamasının sebebi budur.

---

### 3. İç İçe Döngüler Yaklaşımı (Brute Force)

Geçmişte ziyaret edilen düğümleri kontrol etmek için ekstra hafıza (Set) kullanmak yerine, her adımda listenin en başından bulunduğumuz yere kadar tekrar tarama yaptığımız en verimsiz yöntemdir.

**Neden İndeks Kullanıyoruz?**
Tek yönlü bağlı listelerde sadece ileriye gidebiliriz. Geriye dönük "ben bu düğümü daha önce gördüm mü?" sorusunu cevaplayabilmek için `inner` (iç) döngünün sadece baştan başlayıp, o anki `outer` (dış) düğümüne kadar çalışmasını sağlamalıyız. İşte `outer_index` ve `inner_index` değişkenleri bu sınırı belirlemek için vardır. Eğer dış döngünün bir sonraki adımı (`outer.next`), iç döngünün geçmişte taradığı düğümlerden herhangi birine eşit çıkarsa, liste geriye bağlanmış (döngü oluşmuş) demektir.

```python
class SolutionBruteForce:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        outer = head
        outer_index = 0
        
        while outer:
            inner = head
            inner_index = 0
            
            while inner_index < outer_index:
                if inner == outer.next:
                    return True
                inner = inner.next
                inner_index += 1
                
            outer = outer.next
            outer_index += 1
            
        return False
```

**Time Complexity:** `O(N^2)`  
Her bir düğüm noktası için iç döngü baştan sona tekrar çalıştığı için karesel bir zaman karmaşıklığı yaratır, LeetCode üzerinde Zaman Aşımına (Time Limit Exceeded) sebep olabilir.

**Space Complexity:** `O(1)`  
Sadece indeks tutan değişkenler kullanıldığı için alan karmaşıklığı sabittir.