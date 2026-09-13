> 💡 **Not:** Bu soru **Sliding Window** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.
Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

### Example 1:
> **Input:** `nums = [1,12,-5,-6,50,3]`, `k = 4`  
> **Output:** `12.75000`  
> **Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

### Example 2:
> **Input:** `nums = [5]`, `k = 1`  
> **Output:** `5.00000`  

---

### Türkçe Açıklama

Sana `n` elemanlı bir `nums` dizisi ve bir `k` sayısı veriliyor. Senden istenen, dizinin içinde uzunluğu tam olarak `k` olan ve **ortalaması en yüksek** olan alt dizgeyi (subarray) bulman ve bu ortalama değerini döndürmendir.

---

> 🧠 **Neden `float('-inf')` veya `float('inf')` kullanıyoruz?**
> * **Maksimumu (`max`) arıyorsan:** Başlangıç çıtasını en küçük sayıya koymalısın ki gelen herhangi bir sayı onu geçebilsin. O yüzden `-inf` (eksi sonsuz) kullanılır. Sen `+inf` (artı sonsuz) koyarsan, evrendeki hiçbir sayı artı sonsuzdan büyük olamayacağı için `max(inf, 12.75)` hep `inf` olarak kalır ve kod hatalı sonuç verir.
> * **Minimumu (`min`) arıyorsan:** Çıtayı en tepeye koymalısın ki gelen her sayı daha küçük kalıp onu güncelleyebilsin. O zaman `+inf` kullanılır.

---

### 1. Sabit Boyutlu Sliding Window Yaklaşımı (Optimal)

* Uzunluğu tam olarak `k` olan bir alt dizi aradığımız için **Sabit Boyutlu (Fixed-Size) Sliding Window** kullanırız.
* Bir `for` döngüsü ile sağ pointer'ımızı (`r`) ilerletir ve sayıları toplam değişkenimize (`summ`) ekleriz.
* Penceremizin boyutu istenen `k` değerine ulaştığında (`r - l + 1 == k`), ortalamayı hesaplar ve `max_avg` değerimizi güncelleriz.
* Pencereyi bir adım sağa kaydırmak için, en soldaki elemanı (`nums[l]`) toplamdan çıkarır ve sol pointer'ı (`l`) bir artırırız. Böylece bir sonraki döngü adımı için penceremizin boyutu tekrar bozulmamış olur.

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        # Herhangi bir ortalamanın bunu geçebilmesi için eksi sonsuz ile başlatıyoruz
        max_avg = float('-inf') 
        summ = 0
        
        for r in range(len(nums)):
            summ += nums[r]
            
            if (r - l + 1) == k:
                avg = summ / k
                max_avg = max(max_avg, avg)
                summ -= nums[l]
                l += 1
                
        return max_avg
```

**Time Complexity:** `O(N)`

Sağ pointer diziyi yalnızca bir kez tarar ve sol pointer da onunla birlikte ilerler. Her eleman bir kez eklenip en fazla bir kez çıkarıldığı için süre lineerdir.

**Space Complexity:** `O(1)`

Algoritma yalnızca birkaç sayısal değişken (`l`, `max_avg`, `summ`, `avg`) kullanır, bu yüzden fazladan bellek harcanmaz.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force)

* Dizideki her bir indexten başlayarak uzunluğu `k` olan tüm alt dizileri sırayla kontrol edebiliriz. 
* Mantıken doğru çalışsa da, alt dizilerin kesişen (ortak) kısımlarını her seferinde baştan hesapladığı için büyük dizilerde **Time Limit Exceeded (TLE)** hatası alarak çok yavaş çalışır.

```python
class SolutionBruteForce:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = float('-inf')
        n = len(nums)
        
        for i in range(n - k + 1):
            summ = sum(nums[i:i+k])
            avg = summ / k
            max_avg = max(max_avg, avg)
            
        return max_avg
```

**Time Complexity:** `O(N * K)`

Her bir başlangıç elemanı için `k` elemanlık bir toplama işlemi yapılır.

**Space Complexity:** `O(1)`

Ekstra bir veri yapısı oluşturulmaz.