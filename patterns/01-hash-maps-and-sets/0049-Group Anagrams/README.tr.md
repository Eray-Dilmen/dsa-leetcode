> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)


Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
**Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`  
**Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`

### Example 2:
**Input:** `strs = [""]`  
**Output:** `[[""]]`

### Example 3:
**Input:** `strs = ["a"]`  
**Output:** `[["a"]]`

---

### Türkçe Açıklama
Sana kelimelerden oluşan bir `strs` dizisi veriliyor. Senden istenen, birbirinin anagramı olan kelimeleri aynı gruplar (listeler) içine alıp döndürmendir.
*(Anagram: Aynı harflerin aynı sayıda kullanıldığı farklı kelimeler).*

---

### 1. Frekans Tablosu (Tuple İmza) Yaklaşımı (Optimal)

Burada harfleri sıralama (sort etme) işlemi yoktur. Sıralama yerine **harf sayma** mantığı kullanılır. Anagram olan kelimelerin harf frekansları tamamen aynı olacağı için, bu frekans dizisini o kelime grubunun "ortak imzası" olarak kullanabiliriz.

**Kodun Adım Adım Çalışma Mantığı:**
* **`defaultdict(list)`:** Normal bir sözlükte var olmayan bir anahtara eleman eklemeye (append) çalışırsan `KeyError` alırsın. `defaultdict(list)` şu anlama gelir: *"Eğer aradığım anahtar sözlükte henüz yoksa hata verme, onun için otomatik olarak boş bir liste `[]` oluştur"*.
* **`count = [0] * 26`:** İngiliz alfabesindeki 26 harfi temsil eden, içi 26 adet sıfırla dolu bir liste oluşturulur. Bu, anagramların ortak kimliği olacaktır. Her yeni kelimeye geçildiğinde bu liste sıfırlanır.
* **`ord(c) - ord('a')`:** `ord()` fonksiyonu karakterin bellekteki ASCII sayısal değerini verir (Örn: 'a'=97, 'b'=98). `ord(c) - ord('a')` işlemi 'a' harfini 0. indekse, 'b' harfini 1. indekse yerleştiren matematiksel bir numaradır. Örneğin `c` harfi 'b' ise: $98 - 97 = 1$. Böylece `count[1] += 1` çalışır ve 'b' harfinin sayısı artırılır.
* **`key = tuple(count)`:** Python'da listeler (`[]`) değiştirilebilir (mutable) olduğu için sözlüklerde anahtar (key) olarak kullanılamazlar. Bu satır, sayım listesini değiştirilemez (immutable) olan `tuple ()` yapısına dönüştürür.
* **`anagrams_dict[key].append(s)`:** Artık "eat", "tea" ve "ate" kelimeleri bu döngüden çıktığında birebir aynı tuple imzasını (örn: `(1, 0, 0, 0, 1... 1...)`) üretmiş olur. Sözlükte bu ortak imzaya gidilir ve orijinal kelime o grubun listesine eklenir.
* **`anagrams_dict.values()`:** Sonuçta bizden sadece kelime grupları isteniyor. Tuple anahtarları göz ardı edilerek sadece sözlüğün içindeki gruplanmış listeler döndürülür.

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Space Complexity = O(N * M)
        anagrams_dict = defaultdict(list)
        
        # Time Complexity = O(N * M)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            key = tuple(count)
            anagrams_dict[key].append(s)
            
        return list(anagrams_dict.values())
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N \cdot M)$
* $N$: Toplam kelime sayısı. $M$: Bir kelimenin maksimum harf sayısı (uzunluğu).
* Dıştaki döngü listedeki her kelimeyi gezer ($N$ kere döner). İçteki döngü o anki kelimenin her harfini okur ($M$ adım sürer).
* Her harf için yapılan işlem (`ord` hesabı ve artırma) ile sözlüğe ekleme işlemi Hash Table mantığıyla $O(1)$'dir.
* 26 elemanlık diziyi tuple'a çevirmek $O(26) = O(1)$'dir (çünkü 26 sabittir).
* $N$ adet kelime olduğu için toplam zaman: $N \times O(M) = O(N \cdot M)$.

**Space Complexity (Alan Karmaşıklığı):** $O(N \cdot M)$
* En kötü senaryoda (hiçbir kelime birbirinin anagramı değilse) sözlükte $N$ farklı grup açılır.
* Tüm orijinal kelimeler sözlüğün içindeki listelerde saklanır. Listedeki tüm karakterlerin toplam boyutu en fazla $N \times M$ kadardır.
* 26 elemanlık tuple anahtarları sabit ($O(1)$) alan kaplar. Sonuç olarak kaplanan alan $O(N \cdot M)$ olur.

--- 

### 2. Sorting Yaklaşımı (Alternatif / Daha Yavaş)

Eğer iki kelime anagram ise, alfabetik olarak sıralandıklarında tamamen aynı metne dönüşürler (örneğin "eat" ve "tea" sıralandığında ikisi de "aet" olur). Bu sıralanmış metni direkt anahtar (key) olarak kullanabiliriz. Kod daha kısa olsa da, her kelimeyi sıralamak zaman karmaşıklığına ekstra logaritmik yük bindirir.

```python
from collections import defaultdict

class SolutionSorting:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Space Complexity = O(N * M)
        anagrams_dict = defaultdict(list)
        
        # Time Complexity = O(N * M log M)
        for s in strs:
            sorted_word = "".join(sorted(s))
            anagrams_dict[sorted_word].append(s)
            
        return list(anagrams_dict.values())
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N \cdot M \log M)$
Uzunluğu $M$ olan bir kelimeyi sıralamak $O(M \log M)$ sürer. Bu işlem $N$ kelime için yapıldığından süre uzar.

**Space Complexity (Alan Karmaşıklığı):** $O(N \cdot M)$
Kelimeleri tutmak için gereken alan aynıdır.