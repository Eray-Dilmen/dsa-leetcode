> 💡 **Not:** Bu soru **Two Pointers (İki İşaretçi)** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [344. Reverse String](https://leetcode.com/problems/reverse-string/)

**Problem Statement**
Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with `O(1)` extra memory.

### Example 1:
> **Input:** `s = ["h","e","l","l","o"]`  
  **Output:** `["o","l","l","e","h"]`

### Example 2:
> **Input:** `s = ["H","a","n","n","a","h"]`  
  **Output:** `["h","a","n","n","a","H"]`

---

**Türkçe Açıklama**
Sana karakterlerden oluşan bir `s` dizisi veriliyor. Senden istenen, bu diziyi tersine çevirmendir. 
Bunu yaparken yeni bir dizi oluşturmamalı, işlemi doğrudan verilen diziyi değiştirerek (in-place) ve `O(1)` ekstra hafıza kullanarak yapmalısın.

---

### 1. Two Pointers Yaklaşımı (Optimal)

Hafızayı `O(1)`'de tutabilmek için yeni bir dizi yaratamayız. Bunun yerine **Two Pointers** (İki İşaretçi) tekniğini kullanırız: Bir işaretçiyi dizinin en başına (`left`), diğerini en sonuna (`right`) yerleştiririz.

Bu iki işaretçinin gösterdiği elemanların yerini değiştiririz (swap) ve işaretçileri dizinin ortasına doğru hareket ettiririz (`left += 1` ve `right -= 1`). İşaretçiler ortada buluştuğunda (`left < right` koşulu bozulduğunda) işlem tamamlanmış olur. Python'da iki değişkenin değerini değiştirmek için geçici bir `temp` değişkeni kullanmaya gerek yoktur; `a, b = b, a` (tuple unpacking) sözdizimi ile bu işlemi tek satırda çok temiz bir şekilde yapabiliriz.

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Space Complexity = O(1) -> İşlemler dizinin kendi üzerinde (in-place) yapılır
        left = 0
        right = len(s) - 1
        
        # Time Complexity = O(N) -> Dizinin sadece yarısı taranır (N/2 yer değiştirme)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        return s
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N)$
Döngü dizinin tam ortasına kadar çalışır ($N/2$ adım). Asimptotik analizde katsayılar atıldığı için karmaşıklık doğrusal $O(N)$ olarak kabul edilir.
**Space Complexity (Alan Karmaşıklığı):** $O(1)$
Ekstra bir dizi veya veri yapısı kullanılmamıştır.

--- 

### 2. Built-in (Gömülü) Metot Yaklaşımı (Alternatif)

Python listelerinde, elemanları kendi içinde tersine çeviren hazır bir `.reverse()` metodu bulunur. Arka planda C dilinde çok optimize çalışsa da, bu sorunun asıl amacı olan algoritma mantığını (pointer manipülasyonunu) es geçer. Yine de gerçek dünya projelerinde bir listeyi ters çevirmenin en "Pythonic" ve pratik yoludur.

```python
class SolutionAlternative:
    def reverseString(self, s: list[str]) -> None:
        # Space Complexity = O(1) -> reverse metodu in-place çalışır
        # Time Complexity = O(N) -> Diziyi tersine çevirme maliyeti
        s.reverse()
        return s
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N)$
Gömülü fonksiyon diziyi tersine çevirmek için tüm elemanlara dokunur.
**Space Complexity (Alan Karmaşıklığı):** $O(1)$
`.reverse()` metodu yeni bir hafıza ayırmadan listeyi kendi üzerinde (in-place) günceller.