> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)


You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

### Example 1:
> **Input:** `jewels = "aA"`, `stones = "aAAbbbb"`  
> **Output:** `3`

### Example 2:
> **Input:** `jewels = "z"`, `stones = "ZZ"`  
> **Output:** `0`

---

### Türkçe Açıklama
Sana mücevher türlerini temsil eden bir `jewels` metni ve elindeki taşları temsil eden bir `stones` metni veriliyor. `stones` içerisindeki her bir karakter elindeki bir taşı temsil eder. Amacın, sahip olduğun taşların kaç tanesinin aynı zamanda bir mücevher olduğunu bulmaktır.

Harfler büyük-küçük harfe duyarlıdır (case-sensitive), yani `"a"` ile `"A"` farklı türde taşlar olarak kabul edilir.

> **Not:** Hash Set kalıbı, bir elemanı ararken diziyi (veya stringi) baştan sona tekrar taramak yerine (ki bu `O(n)` sürer), elemanları bir kümeye (Set) kaydederek daha sonra bu elemanları `O(1)` sürede bulmak/sorgulamak için kullanılır.

---

### 1. Hash Set Yaklaşımı (Optimal)

String yerine `O(1)` sürede arama yapabilen bir Hash Set kullanılır. İşlem iki bağımsız aşamaya bölünür:

1. **Aşama 1 (Set Oluşturma):** `jewels` string'indeki tüm karakterler alınıp bir `Set` yapısına atılır (`s = set(jewels)`). `n` tane karakter tek tek okunup hash tablosuna eklenir; maliyeti `O(n)`'dir.
2. **Aşama 2 (Taşları Kontrol Etme):** `stones` string'i üzerinde tek bir döngü kurulur (`m` adım). Her bir taş için `stone in s` kontrolü yapılır. Set'te arama yapmak `O(1)` olduğu için her taşın kontrolü anında biter (`m * O(1) = O(m)`).

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        
        for stone in stones:
            if stone in s:
                count += 1
                
        return count
```

**Time Complexity:** `O(n + m)`

İç içe döngü olmadığı için karmaşıklıklar çarpılmaz (`n * m` olmaz), ardışık yapılan işlemler (`n` ve `m` adımları) toplanır.

**Space Complexity:** `O(n)`

`jewels` karakterlerini (yalnızca benzersiz olanları) saklamak için Set kullanılır, bu da `n` boyutunda ekstra hafıza gerektirir.

--- 

### 2. Brute Force Yaklaşımı

`stones` içindeki her bir taş (`m` tane) için tek tek `jewels` string'i taranır (`n` tane). Python'daki `in` operatörü string üzerinde arka planda gizli bir for döngüsü (`O(n)`) çalıştırır.

* İlk taş için `n` adım kontrol edilir.
* İkinci taş için `n` adım kontrol edilir.
* **Toplam işlem:** `m` defa `n` arama = `m * n` adım.

```python
class SolutionBruteForce:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        
        for stone in stones:
            if stone in jewels:
                count += 1
                
        return count
```

**Time Complexity:** `O(n * m)`

İç içe iki döngü (biri bizim yazdığımız `for`, diğeri arka planda çalışan `in`) oluştuğu için süre `O(n * m)` olur.

**Space Complexity:** `O(1)`

Ekstra bir veri yapısı oluşturulmaz.