> 💡 **Not:** Bu problem optimal olarak **Hash Map** kalıbı kullanılarak, karakterler arasında birebir eşleme (bijection) kurularak çözülmektedir. Kalıbın genel mantığı ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

Sana `s` ve `t` adında iki string veriliyor. Bu iki string'in **isomorphic** (eşyapılı) olup olmadığını belirlemen isteniyor.

Eğer `s` içindeki karakterler, sırası bozulmadan başka karakterlerle değiştirilerek `t` elde edilebiliyorsa bu iki string isomorphictir.

Aynı karakterin tüm tekrarları, eşleştiği karakterle değiştirilmelidir. İki farklı karakter asla aynı karaktere eşlenemez, ancak bir karakter kendi kendine eşlenebilir.

### Example 1:
> **Input:** `s = "egg", t = "add"`  
> **Output:** `true`  
> **Explanation:** 'e' -> 'a' ve 'g' -> 'd' olarak eşlendiğinde "add" elde edilir.

### Example 2:
> **Input:** `s = "foo", t = "bar"`  
> **Output:** `false`  
> **Explanation:** 'o' karakteri hem 'a' hem de 'r' karakterine eşlenemeyeceği için eşyapılı değildir.

---

### 1. İki Hash Map Yaklaşımı (Optimal)

İki string'in isomorphic olabilmesi için aralarında kusursuz bir **birebir eşleme (bijection)** olmalıdır. Bunun iki kuralı vardır:
1. `s` içindeki bir karakter `t`'de her zaman aynı karaktere gitmelidir.
2. `t` içindeki bir karakter de `s`'de her zaman aynı karakterden gelmelidir.

Bunu kontrol etmek için iki farklı Hash Map (sözlük) tutarız: `map_st` ve `map_ts`. Karakterleri sırayla gezerken her iki sözlüğe de bakarız. Eğer daha önceden başka birine söz verilmişse (eşlenmişse), anında `False` döndürürüz. 

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        map_st = {}
        map_ts = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # 1. Kontrol: char_s daha önce kime eşlendi?
            if char_s in map_st and map_st[char_s] != char_t:
                return False
                
            # 2. Kontrol: char_t daha önce kime bağlandı?
            if char_t in map_ts and map_ts[char_t] != char_s:
                return False
                
            # Sorun yoksa eşleştirmeyi kaydet
            map_st[char_s] = char_t
            map_ts[char_t] = char_s
            
        return True
```

**Time Complexity:** `O(N)`  
String'i sadece bir kez baştan sona tararız. Sözlük (Hash Map) içinde arama ve ekleme işlemleri ortalamada $O(1)$ zaman alır. Bu yüzden toplam süre lineerdir.

**Space Complexity:** `O(1)`  
Sözlüklerin boyutu eşsiz karakter sayısına bağlıdır. Alfabe ve sembol sayısı sabit bir üst sınıra (örn. ASCII için 256) sahip olduğu için asimptotik olarak alan karmaşıklığı sabittir, $O(1)$ kabul edilir.

--- 

### 2. İlk Görülme İndeksi Yaklaşımı (Brute Force)

Python'un yerleşik `find()` fonksiyonunu kullanan yaratıcı ama çok yavaş bir alternatiftir. Eğer iki string eşyapılıysa, karakterlerin tekrarlanma şablonları da tamamen aynı olmalıdır.

Bir karakterin string içinde *ilk görüldüğü* indeksi veren `find()` metodunu kullanarak şu kontrolü yaparız: O anki `s[i]` karakterinin `s` içindeki ilk konumu ile `t[i]` karakterinin `t` içindeki ilk konumu birbiriyle uyuşuyor mu? Uyuşmuyorsa, desen bozulmuş demektir.

```python
class SolutionBruteForce:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # İki string'in uzunluğu farklıysa zaten eşlenemez
        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            # s[i]'nin s içindeki ilk geçtiği indeks ile
            # t[i]'nin t içindeki ilk geçtiği indeks aynı mı?
            if s.find(s[i]) != t.find(t[i]):
                return False
                
        return True
```

**Time Complexity:** `O(N^2)`  
Dışarıdaki `for` döngüsü $N$ adım çalışır. Ancak içerideki `find()` fonksiyonu da aradığı karakteri bulmak için string'i baştan tarar (en kötü durumda $N$ adım). Döngü içinde döngü mantığı oluştuğu için karesel bir zaman karmaşıklığı yaratır, uzun metinlerde Zaman Aşımı (TLE) yeme ihtimali yüksektir.

**Space Complexity:** `O(1)`  
Ekstra hiçbir veri yapısı (sözlük, dizi vb.) kullanılmadığı için ekstra alan maliyeti yoktur.