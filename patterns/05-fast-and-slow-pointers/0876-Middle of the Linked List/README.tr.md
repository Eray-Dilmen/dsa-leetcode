> 💡 **Not:** Bu problem optimal olarak **Fast and Slow Pointers** (Hızlı ve Yavaş İşaretçiler) kalıbı ile çözülmektedir. Şu anki dosyada sadece kaba kuvvet (iki tur) yaklaşımı bulunmaktadır. Kalıbın genel mantığı ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

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

Bağlı listelerin dizilerden (array) en büyük farkı, boyutlarını (eleman sayısını) önceden bilemememizdir[cite: 14]. Dizilerde `len(dizi)` diyerek anında boyutu bulabilirken, bağlı listelerde boyutu bulmak için baştan sona tüm düğümleri tek tek gezmek zorundayız[cite: 14].

Bu soruda listenin tam ortasını bulmamız isteniyor. 

---

### 1. Uzunluğu Bulup Tekrar İlerleme Yaklaşımı (Brute Force / İki Tur)

En temel ve akla ilk gelen yöntemdir[cite: 14]. Madem boyutu bilmiyoruz, o zaman önce tüm listeyi baştan sona bir kez gezer ve eleman sayısını sayarız.

1. Bir `curr` işaretçisi ile listeyi sonuna kadar gezip `lenght` değişkenini artırırız[cite: 14].
2. Toplam uzunluğu bulduktan sonra, orta noktayı bulmak için tam sayı bölmesi (`lenght // 2`) yaparız[cite: 14].
3. `curr` işaretçisini tekrar en başa (`head`) alırız[cite: 14].
4. Bulduğumuz `middle` değeri kadar for döngüsü ile tekrar ilerleriz[cite: 14]. Döngü bittiğinde işaretçimiz tam olarak orta düğümün üzerinde durmuş olur[cite: 14].

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
Listeyi uzunluğu bulmak için bir tam tur ($N$ adım) ve orta noktaya gelmek için yarım tur ($N/2$ adım) geziyoruz. Toplamda $O(N)$ zaman alır fakat verimsiz bir şekilde aynı elemanların üzerinden iki kez geçmiş oluruz.

**Space Complexity:** `O(1)`  
Sadece sayaç ve takip amaçlı birkaç değişken (`lenght`, `middle`, `curr`) kullandığımız için ekstra hafıza maliyeti yoktur[cite: 14].