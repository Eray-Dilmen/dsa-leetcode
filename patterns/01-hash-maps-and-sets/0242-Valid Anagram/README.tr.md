> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)


Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
> **Input:** `s = "anagram"`, `t = "nagaram"`  
> **Output:** `true`  

### Example 2:
> **Input:** `s = "rat"`, `t = "car"`  
> **Output:** `false`  

---

### Türkçe Açıklama
Sana `s` ve `t` adında iki metin veriliyor. Eğer `t` metni, `s` metninin bir **anagramı** ise `true`, değilse `false` döndürmen isteniyor. 
Anagram, bir kelimedeki harflerin yerlerinin değiştirilerek (her harfin tam olarak aynı sayıda kullanılması şartıyla) yeni bir kelime oluşturulmasıdır.

---

### 1. Tek Hash Map Yaklaşımı (Optimal)

Eğer iki metnin uzunluğu birbirinden farklıysa anagram olmaları imkansızdır. Başlangıçta tek bir sözlük oluşturup, `s` metnindeki harflerin frekansını (kaç kere geçtiklerini) sayarız. Daha sonra `t` metnini gezeriz. Eğer `t`'deki bir harf sözlüğümüzde yoksa veya adedi `0`'a düşmüşse, anında `False` döndürürüz. Aksi takdirde sözlükteki değerini 1 azaltırız. Erken çıkış (early exit) yapabildiği için en optimal çözümdür.

> 💡 **Kod Temizliği İpucu: `count.get(char, 0) + 1`**
> 
> Bir harfin sözlükte olup olmadığını kontrol etmek için 4 satırlık bir `if/else` bloğu yazmak yerine, `.get()` metodunu kullanarak aynı işlemi tek satırda, çok daha sade ve temiz bir şekilde yapabiliriz:
> * **`count.get(char, 0)` ne yapar?:** Normalde sözlükte olmayan bir anahtarı çağırdığınızda (`count[char]`) Python `KeyError` hatası verir. `.get()` metodu ise hata vermek yerine belirlediğimiz varsayılan bir değeri (default value) döndürür.
> * **Parametreler:** İlk parametre (`char`) sözlükte aranan anahtardır. İkinci parametre (`0`) ise harf sözlükte henüz yoksa döndürülecek varsayılan değerdir.
> * **Neden `+ 1`?:** Harf sözlükte yoksa `.get()` ifadesi `0` döner, sonuna `+ 1` ekleyince harf ilk kez `1` değeriyle kaydedilir. Harf zaten varsa mevcut sayıyı getirir (örneğin `2`), `+ 1` ekleyince adedi bir artırılmış olur (`3`).

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        
        # s içindeki harfleri say
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # t içindeki harfleri eksilt
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n)` İki string de birer kez taranır.

**Space Complexity (Alan Karmaşıklığı):** `O(1)`
Sözlük en fazla 26 adet İngilizce küçük harf tutacağı için harcanan alan sabittir.

--- 

### 2. İki Hash Map Yaklaşımı (Alternatif)

Tek bir sözlüğü artırıp azaltmak yerine, hem `s` hem de `t` için iki ayrı sözlük oluşturup harfleri sayabiliriz. İşlem sonunda bu iki sözlüğün birbirine tam olarak eşit olup olmadığını (`sm == st`) kontrol ederiz.

```python
class SolutionTwoMaps:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = {}
        st = {}
        
        for l in s:
            if l in sm:
                sm[l] += 1
            else:
                sm[l] = 1
                
        for l in t:
            if l in st:
                st[l] += 1
            else:
                st[l] = 1
                
        return sm == st
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n)` İki sözlüğü doldurmak da `O(n)` zaman alır.

**Space Complexity (Alan Karmaşıklığı):** `O(1)` İki sözlük de maksimum 26 eleman tutar.

---

### 3. Built-in Counter Yaklaşımı (Alternatif)

Python'un `collections` kütüphanesinde bulunan `Counter` sınıfı, arka planda manuel olarak yaptığımız frekans sayma işlemini otomatik yapar. Temiz ve "Pythonic" bir koddur. Mantık olarak İki Hash Map yaklaşımıyla tamamen aynıdır.

```python
from collections import Counter

class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_dict = Counter(s)
        t_dict = Counter(t)
        
        return s_dict == t_dict
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n)` `Counter` fonksiyonu verilen metni baştan sona taradığı için `O(n)` sürer.

**Space Complexity (Alan Karmaşıklığı):** `O(1)` Sayaçlar maksimum 26 karakter tutar.

---

### 4. Sorting Yaklaşımı (Brute Force)

Eğer iki metin gerçekten anagramsa, alfabetik olarak sıralandıklarında birbirlerinin tamamen aynısı olmalıdırlar. Kodlaması en kısa yöntemdir ancak sıralama algoritmalarının maliyeti yüksek olduğu için yavaş çalışır.

```python
class SolutionBruteForce:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n log n)` Sıralama (sorting) algoritması `O(n log n)` sürede çalışır.

**Space Complexity (Alan Karmaşıklığı):** `O(n)` `sorted()` fonksiyonu bellekte yeni bir liste kopyası oluşturduğu için `O(n)` alan kaplar.