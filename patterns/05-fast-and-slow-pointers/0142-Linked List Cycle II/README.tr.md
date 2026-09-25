> 💡 **Not:** Bu problem, döngü bulma mantığının bir uzantısıdır ve optimal olarak **Fast and Slow Pointers** (Floyd's Cycle-Finding) algoritması ile çözülmektedir. Kalıbın teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

Sana bir bağlı listenin `head` düğümü veriliyor. Senden istenen, eğer listede bir döngü varsa, **döngünün başladığı o ilk düğümü** (başlangıç noktasını) döndürmendir. Eğer döngü yoksa `null` döndür.

Bağlı listeyi **değiştirmemen (modify etmemen)** gerekmektedir.

### Example 1:
> **Input:** `head = [3,2,0,-4], pos = 1`  
> **Output:** `tail connects to node index 1`  
> **Explanation:** Listedeki son düğüm (-4), 1. indeksteki düğüme (2) bağlandığı için döngünün başlangıç noktası o düğümdür.

### Example 2:
> **Input:** `head = [1,2], pos = 0`  
> **Output:** `tail connects to node index 0`  
> **Explanation:** Listedeki son düğüm, 0. indeksteki düğüme bağlandığı için döngü başlangıcı orasıdır.

---

### 1. Fast and Slow Pointers Yaklaşımı (Optimal / Floyd'un Algoritması)

Döngünün başladığı noktayı ekstra hafıza kullanmadan tam olarak bulmak için Floyd'un algoritmasının iki aşamalı yapısını kullanırız.

**Adım 1: Başlangıç**
`slow` ve `fast` işaretçilerinin ikisini de listenin en başından (`head`) başlatırız.
<br>
<img src="step1_initial.jpg" width="500" />

**Adım 2: Döngüyü Tespit Etme (1. Aşama)**
`slow` 1 adım, `fast` 2 adım ilerler. Eğer döngü varsa, hızlı olan yavaşa arkadan yetişir ve kesişirler (`slow == fast`). Bu kesişme döngünün varlığını kanıtlar.
<br>
<img src="step2_meeting.jpg" width="500" />

**Adım 3: Hızlı İşaretçiyi Başa Alma (2. Aşama Başlangıcı)**
İşaretçiler kesiştiğinde döngünün içindedirler ama başlangıç noktasında olmak zorunda değillerdir. Başlangıcı bulmak için `slow` işaretçisini kesişim noktasında bırakırız, `fast` işaretçisini ise en başa (`head`) geri çekeriz.
<br>
<img src="step3_reset.jpg" width="500" />

**Adım 4: Başlangıç Noktasını Bulma**
Artık ikisini de **aynı hızda (birer adım)** ilerletiriz. Tekrar karşılaştıkları ilk düğüm, matematiksel olarak garanti bir şekilde döngünün başlangıç noktasıdır.
<br>
<img src="step4_cycle_start.jpg" width="500" />

**Matematiksel İspat:**
Neden ikisini aynı hızda yürüttüğümüzde tam kapıda buluşuyorlar? Mesafeleri formüle dökelim.
<br>
<img src="floyds_math.jpg" width="600" />

* `A` = `head`'den döngünün başladığı yere olan mesafe.
* `B` = Döngünün başından, işaretçilerin ilk kesiştiği yere olan mesafe.
* `k` = Döngünün toplam uzunluğu (çevresi).
* `n` = `fast` işaretçisinin kesişmeden önce döngü içinde attığı tam tur sayısı.

1. `slow` işaretçisinin gittiği toplam yol: $A + B$
2. `fast` işaretçisinin gittiği toplam yol: $A + B + n \cdot k$
3. Hızlı işaretçi yavaşın iki katı hızda gittiği için: $2 \cdot (A + B) = A + B + n \cdot k$
4. Sadeleştirdiğimizde: $A + B = n \cdot k \implies A = n \cdot k - B$

**$A = n \cdot k - B$ Ne Anlama Geliyor?**
Başlangıçtan döngü girişine kadar olan `A` mesafesi, kesişim noktasından döngü girişine kadar kalan mesafeye ($k - B$) eşittir. Bu yüzden bir işaretçiyi en başa alıp, diğerini kesişim noktasında bırakıp aynı hızda yürüttüğümüzde tam olarak döngünün başlangıç noktasında çarpışırlar.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                return fast
                
        return None
```

**Time Complexity:** `O(N)`  
İlk aşamada kesişimi bulmak lineer zaman alır. İkinci aşamada döngü başlangıcını bulmak en fazla lineer zaman alır. Toplamda `O(N)`.

**Space Complexity:** `O(1)`  
Listeyi hafızada tutmayıp sadece iki işaretçi değişkeni kullandığımız için bellek kullanımı sabittir.

--- 

### 2. Hash Set Yaklaşımı (Brute Force / Naive)

Eğer hafıza kullanma kısıtlamamız yoksa en kolay yöntem geçtiğimiz yolları bir `set` (küme) içine kaydetmektir.

**Nasıl Çalışır?**
Listeyi düğüm düğüm gezeriz. Her düğümü `sett` içine ekleriz. Eğer `sett` içinde zaten var olan bir düğüme tekrar denk gelirsek, o düğüm tam olarak döngünün başladığı, listeyi geriye bağlayan ilk noktadır. Döngü biterse `None` döndürürüz.

```python
class SolutionHashSet:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sett = set()
        curr = head
        
        while(curr):
            if curr in sett:
                return curr
                
            sett.add(curr)
            curr = curr.next
            
        return None
```

**Neden $O(N)$ yazılması gerekir?**
Big-O notasyonu algoritmanın en kötü durumdaki (worst-case) üst sınırını ifade eder.

**Time Complexity:** `O(N)`  
Listede döngü yoksa tüm liste taranır ($N$ adım). Döngü varsa döngünün başladığı yere kadar gidilip durulur ($k \le N$ adım). Her düğümde `set` içine ekleme (`add`) ve arama (`in`) kontrolü ortalama $O(1)$ olduğundan, $N$ adımın toplam zaman maliyeti $O(N)$ olur.

**Space Complexity:** `O(N)`  
* Eğer listede döngü yoksa (`pos = -1`), küme (`sett`) listenin tüm elemanlarını içine alır ve boyutu tam olarak $N$ olur. Dolayısıyla en kötü durumda $N$ elemanlık alan tuttuğu için kesinlikle $O(N)$ yazılır.
* Listedeki döngü başı $k$. indeksteyse küme boyutu $k + 1$ olur; ancak asimptotik analizde katsayı ve alt sınırlar değil, giriş boyutuna bağlı üst sınır ($N$) esas alınır.