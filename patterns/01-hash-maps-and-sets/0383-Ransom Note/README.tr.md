> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

**Problem Statement**
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1:
> **Input:** `ransomNote = "a"`, `magazine = "b"`  
> **Output:** `false`

### Example 2:
> **Input:** `ransomNote = "aa"`, `magazine = "ab"`  
> **Output:** `false`

### Example 3:
> **Input:** `ransomNote = "aa"`, `magazine = "aab"`  
> **Output:** `true`

---

**Türkçe Açıklama**
Bizden, `ransomNote` stringini yazabilmek için elimizdeki `magazine` stringinde yeterli harf olup olmadığını bulmamız isteniyor. Harflerin sıralaması önemli değildir. Sadece `ransomNote` içindeki her bir harf için, `magazine` içinde o harften en az o kadar sayıda bulunması ve her harfin yalnızca bir kez kullanılabilmesi kuralına dikkat etmemiz gerekiyor.

> **Not:** Hash table kalıbı (pattern), string veya dizilerdeki elemanların frekansını (kaç adet olduklarını) saymak ve daha sonra bu elemanları `O(1)` sürede aramak/kontrol etmek için kullanılır.

---

### 1. Hash Map Yaklaşımı (Optimal)

* Öncelikle `magazine` içindeki tüm harfleri tek bir döngüyle gezip, hangi harften kaç tane olduğunu bir sözlüğe (Hash Map) kaydederiz.
* Ardından `ransomNote` harflerini döngüye sokar, sözlükte var mı ve adedi yeterli mi (`>0`) diye kontrol ederiz.
* Varsa değerini `1` eksiltir, yolumuza devam ederiz. Yoksa anında `False` döneriz.

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        guide = {}

        for letter in magazine:
            if letter in guide:
                guide[letter] += 1
            else:
                guide[letter] = 1

        for char in ransomNote:
            if char not in guide or guide[char] == 0:
                return False
            guide[char] -= 1

        return True
```

**Time Complexity:** `O(m + n)`

Birinci döngü `magazine` uzunluğu (`m`) kadar çalışır ve `O(m)` zaman alır. İkinci döngü `ransomNote` uzunluğu (`n`) kadar çalışır ve `O(n)` zaman alır. Bu iki döngü iç içe (nested) değil, ardışık (arka arkaya) olduğu için karmaşıklıklar çarpılmaz, toplanır. Arama işlemleri (`in` anahtar kelimesi) hash map üzerinde yapıldığı için `O(1)` sürer. Sonuç olarak toplam süre `O(m + n)` olur.

**Space Complexity:** `O(1)`

`guide` adında ekstra bir sözlük yapısı oluşturduk. En kötü senaryoda bile İngilizce alfabesinde en fazla 26 adet küçük harf bulunur. Yani sözlüğün boyutu girdi ne kadar büyük olursa olsun en fazla 26 elemana kadar büyüyebilir. Büyüme miktarı girdiye bağlı olmayıp sabit (constant) bir sınıra sahip olduğu için alan karmaşıklığı `O(1)` olarak kabul edilir.

--- 

### 2. Brute Force Yaklaşımı

```python
class SolutionBruteForce:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = list(magazine)
        
        for char in ransomNote:
            if char in mag_list:
                mag_list.remove(char)
            else:
                return False
                
        return True
```

**Time Complexity:** `O(n * m)`

`ransomNote` içindeki her bir karakter (`n`) için, `mag_list` listesinde hem arama (`in`) hem de silme (`remove`) işlemi yapılır. Listelerde bu işlemler `O(m)` sürede gerçekleştiğinden toplam süre `O(n * m)` olur.

**Space Complexity:** `O(m)`

String değiştirilemez (immutable) olduğu için `magazine` karakterlerini tutan ve silme işlemlerini gerçekleştirdiğimiz ek bir liste (`mag_list`) oluşturulur; bu liste `m` eleman kadar yer kaplar.