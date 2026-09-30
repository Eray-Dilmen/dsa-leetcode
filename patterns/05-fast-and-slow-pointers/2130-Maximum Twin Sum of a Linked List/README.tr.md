> 💡 **Not:** Bu problem optimal olarak **Fast and Slow Pointers** (Hızlı ve Yavaş İşaretçiler) ve **Bağlı Listeyi Ters Çevirme (Reverse)** kalıplarının birleşimi ile çözülmektedir. Teorik detaylar için [README.md](../README.md) dosyasına bakabilirsiniz.

# [2130. Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

Çift sayıda (`n` uzunluğunda) elemana sahip bir bağlı listede, `i.` düğüm ile `(n-1-i).` düğüm birbirinin **ikizi (twin)** olarak kabul edilir. (Sınır: `0 <= i <= (n / 2) - 1`).

* Örneğin `n = 4` ise, 0. düğüm ile 3. düğüm ikizdir. Aynı şekilde 1. düğüm ile 2. düğüm ikizdir.

**Twin sum (İkiz Toplamı):** Bir düğüm ile onun ikizinin değerlerinin toplamıdır.

Sana çift uzunluklu bir bağlı listenin `head` düğümü veriliyor. Bu listedeki **en büyük ikiz toplamını (maximum twin sum)** bulman isteniyor.

### Example 1:
> **Input:** `head = [5,4,2,1]`  
> **Output:** `6`  
> **Explanation:**  
> Düğüm 0 ve 1'in ikizleri sırasıyla 3 ve 2'dir. İkiz toplamları 5+1=6 ve 4+2=6'dır. Maksimum toplam 6'dır.

---

### 1. Fast & Slow Pointers ve Reverse Yaklaşımı (Optimal)

Bu problemi ekstra hafıza kullanmadan ($O(1)$ space) çözebilmek için bağlı listenin kendi düğüm bağlantıları üzerinde oynamamız gerekir. 

Optimal çözüm üç ana adımdan oluşur:
1. **Ortayı Bul:** Fast ve Slow pointer kullanarak listenin yarısını buluruz. Hızlı işaretçi sona ulaştığında, yavaş işaretçi tam olarak ikinci yarının başında durur.
2. **İkinci Yarıyı Ters Çevir:** Yavaş işaretçiden itibaren listenin ikinci yarısındaki okların yönünü tersine çeviririz. Bu sayede ikinci yarıyı sondan başa (merkeze) doğru okuyabilir hale geliriz.
3. **İki Uçtan Merkeze Doğru Topla:** İlk yarıyı `head`'den, ters çevrilmiş ikinci yarıyı ise `prev`'den başlatarak aynı anda ilerletiriz ve karşılaştıkları değerleri toplayıp maksimumu buluruz.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        # 1. Ortayı bul
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. İkinci yarıyı ters çevir
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        # 3. İki uçtan merkeze doğru topla
        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next
            
        return ans
```

**Time Complexity:** `O(N)`  
Ortayı bulmak ($N/2$), ikinci yarıyı ters çevirmek ($N/2$) ve toplamları hesaplamak ($N/2$) toplamda $O(N)$ yani lineer zaman alır.

**Space Complexity:** `O(1)`  
Listeyi hafızada başka bir yapıya kopyalamak yerine sadece birkaç işaretçi (`slow`, `fast`, `prev`) kullanarak kendi üzerinde (in-place) değiştirdiğimiz için ekstra alan kullanılmaz.

--- 

### 2. Diziye Çevirme Yaklaşımı (Alternatif)

Eğer bellek kısıtlamamız yoksa, en basit çözüm bağlı listeyi normal bir diziye (array) kopyalamaktır. Diziye kopyaladıktan sonra indeksler üzerinden işlem yapmak çok kolaylaşır.

**$0 \le i \le (n/2) - 1$ Eşitsizliğinin Mantığı Nedir?**
Döngüyü neden sadece `n // 2`'ye kadar çalıştırıyoruz? Bu şart, bizim sadece **ilk yarıdaki** indeksleri aldığımızı gösteren matematiksel bir yazımdır.
* İndeksler 0'dan başladığı için ilk eleman $i = 0$'dır.
* Dizi çift uzunluklu olduğu için ilk yarının son elemanının indeksi $(n/2) - 1$'dir (Örn: 6 elemanlı dizide ilk yarının son indeksi 2'dir).
Böylece indeks (i) en fazla yarısından 1 azına kadar gidebilir çünkü diğer yarısına aşmasını ve aynı hesaplamaları baştan yapmasını istemiyoruz. En baştaki ile en sondaki, ikinci ile sondan ikinci şeklinde iki uçtan merkeze doğru tam bir ilerleme sağlamış oluruz.

```python
class SolutionAlternative:
    def pairSum(self, head: ListNode | None) -> int:
        maxx = float('-inf')
        curr = head
        vals = []
        
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        n = len(vals)
        for i in range(n // 2):
            maxx = max(maxx, vals[i] + vals[n - 1 - i])
            
        return maxx
```

**Time Complexity:** `O(N)`  
Listeyi diziye aktarmak $N$ adım, ardından ilk yarıyı dönmek $N/2$ adım sürer. Toplamda $O(N)$ zaman alır.

**Space Complexity:** `O(N)`  
Listedeki tüm elemanların değerleri yeni bir `vals` dizisine kopyalandığı için lineer bir hafıza maliyeti oluşur.