> 💡 **Not:** Bu soru **Sliding Window** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

### Example 1:
> **Input:** `s1 = "ab", s2 = "eidbaooo"`
> **Output:** `true`
> **Explanation:** `s2` contains one permutation of `s1` ("ba").

### Example 2:
> **Input:** `s1 = "ab", s2 = "eidboaoo"`
> **Output:** `false`

---

### Türkçe Açıklama

Sana `s1` ve `s2` adında iki metin veriliyor. Senden istenen, `s1` metninin rastgele karıştırılmış herhangi bir versiyonunun (kombinasyonunun/permutasyonunun) `s2`'nin içinde kesintisiz bir alt dizge (substring) olarak bulunup bulunmadığını kontrol etmendir. Bulunuyorsa `true`, bulunmuyorsa `false` döndürmelisin.

---

### 1. Hash Map (Sözlük) ile Sabit Boyutlu Sliding Window (Optimal)

* Bir alt dizgenin permutasyon olması demek, içindeki harflerin ve o harflerin geçme sıklıklarının `s1` ile tamamen aynı olması demektir. Harflerin sırası önemli değildir.
* Bu yüzden `s2` üzerinde boyutu tam olarak `len(s1)` olan **Sabit Boyutlu (Fixed-Size) bir Sliding Window** kaydırırız.
* Önce `s1` içindeki harflerin frekansını bir sözlüğe (`letters_1`) kaydederiz.
* Sağ pointer (`r`) ile `s2`'yi tararken, penceredeki harfleri de ikinci bir sözlüğe (`letters_2`) ekleriz.
* Penceremizin boyutu istenen uzunluğa ulaştığında `(r - l + 1) == len(s1)`, iki sözlüğü birbiriyle kıyaslarız. Eğer sözlükler birebir aynıysa, permutasyonu bulmuşuz demektir ve `True` döndürürüz.
* Pencereyi kaydırmaya devam etmeden önce, en soldaki harfi (`s2[l]`) penceremizden ve sözlüğümüzden çıkarmamız gerekir. Eğer o harfin frekansı 0'a düşerse, `del` anahtar kelimesi ile onu sözlükten tamamen sileriz ki eşitlik kontrolünde boş yere sorun çıkarmasın. Ardından sol pointer'ı (`l`) bir artırırız.

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters_1 = {}
        letters_2 = {}
        
        for l in s1:
            letters_1[l] = letters_1.get(l, 0) + 1
            
        l = 0
        for r in range(len(s2)):
            letters_2[s2[r]] = letters_2.get(s2[r], 0) + 1
            
            if (r - l + 1) == len(s1):
                if letters_1 == letters_2:
                    return True
                    
                letters_2[s2[l]] -= 1
                if letters_2[s2[l]] == 0:
                    del letters_2[s2[l]]
                l += 1
                
        return False
```

**Time Complexity:** `O(N + M)`

`s1` uzunluğuna `N`, `s2` uzunluğuna `M` diyelim. İki diziyi de sadece birer kez tarıyoruz. Sözlük (dictionary) karşılaştırmaları teknik olarak `K` (sözlük boyutu) kadar sürse de, İngiliz alfabesindeki harf sayısı sınırlı olduğundan `K` bir sabittir (constant, maksimum 26). Bu yüzden zaman karmaşıklığı `O(N + M * K)` olmaz, asimptotik analizde sabitler atıldığı için net olarak `O(N + M)` şeklinde ifade edilir.

**Space Complexity:** `O(1)`

`letters_1` ve `letters_2` sözlükleri maksimum 26 adet harf barındırabilir. Tüketilen hafıza metnin uzunluğuna göre büyümeyip 26'da sabit kaldığı için alan karmaşıklığı `O(1)`'dir.

--- 

### 2. Alt Dizgeleri Sıralama (Brute Force)

* `s1` metnini alfabetik olarak sıralarız.
* Ardından `s2` içindeki `len(s1)` boyutundaki tüm olası alt dizgeleri tek tek keser, alfabetik olarak sıralar ve baştaki `s1` ile aynı olup olmadıklarına bakarız.
* Her adımda tekrar tekrar sıralama (sort) işlemi yapıldığı için çok ciddi performans kaybı yaşanır.

```python
class SolutionBruteForce:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        sorted_s1 = sorted(s1)
        
        for i in range(m - n + 1):
            if sorted(s2[i:i+n]) == sorted_s1:
                return True
                
        return False
```

**Time Complexity:** `O(M * N \log N)`

`s2` içindeki her bir başlangıç noktası için `O(M)`, `N` uzunluğunda bir listeyi sıralamak `O(N \log N)` zaman alır.

**Space Complexity:** `O(N)`

Kestigimiz alt dizgeleri ve `sorted_s1` değişkenini hafızada tutmak için ekstra alan ayırırız.