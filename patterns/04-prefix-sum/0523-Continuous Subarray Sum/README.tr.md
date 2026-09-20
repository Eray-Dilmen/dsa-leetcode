> 💡 **Not:** Bu problem **Prefix Sum** (Kümülatif Toplam) kalıbı ve Modüler Aritmetik kullanılarak çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is a subarray where:
* its length is at least two, and
* the sum of the elements of the subarray is a multiple of `k`.

**Note that:**
* A subarray is a contiguous part of the array.
* An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is always a multiple of `k`.

### Example 1:
> **Input:** `nums = [23,2,4,6,7]`, `k = 6`  
> **Output:** `true`  
> **Explanation:** `[2, 4]` is a continuous subarray of size 2 whose elements sum up to 6.  

### Example 2:
> **Input:** `nums = [23,2,6,4,7]`, `k = 6`  
> **Output:** `true`  
> **Explanation:** `[23, 2, 6, 4, 7]` is an continuous subarray of size 5 whose elements sum up to 42. 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.  

### Example 3:
> **Input:** `nums = [23,2,6,4,7]`, `k = 13`  
> **Output:** `false`  

---

### Türkçe Açıklama

Sana `nums` adında bir tam sayı dizisi ve `k` adında bir hedef sayı veriliyor. Senden istenen, dizinin içerisinde aşağıdaki iki şartı da sağlayan "iyi bir alt dizi (good subarray)" olup olmadığını bulmandır:
1. Alt dizinin uzunluğu **en az 2** olmalıdır.
2. Alt dizideki elemanların toplamı **`k` sayısının bir katı** olmalıdır (Yani toplamanın `k`'ya bölümünden kalan 0 olmalıdır).

Eğer böyle bir alt dizi varsa `True`, yoksa `False` döndürmelisin.

---

### 1. Hash Map ve Modüler Aritmetik ile Prefix Sum Yaklaşımı (Optimal)

Bir alt dizinin toplamının `k`'nın katı olup olmadığını bulmak için modüler aritmetik kuralını kullanırız. 
Kural şudur: Eğer `(A - B) % k == 0` ise, o zaman `A % k == B % k`'dır. 
Yani dizide ilerlerken kümülatif toplamların `k`'ya göre kalanını (modülünü) alırız. Eğer aynı kalanı daha önce de gördüysek, o iki nokta arasındaki alt dizinin toplamı tam olarak `k`'nın katı demektir.

**`{0: -1}` Başlangıç Ayarının Mantığı Nedir?**
Hash map'i (sözlüğü) baştan `remainder_map = {0: -1}` şeklinde başlatmamız çok kritik bir detaydır. 
Neden `0: -1` olarak ayarladık? Çünkü geçerli bir alt dizinin dizinin tam olarak 0. indeksinden başlaması durumunu doğru hesaplamamız gerekir.
Örneğin, dizinin ilk iki elemanının (index 0 ve index 1) toplamı `k`'ya tam bölünüyor diyelim. Bu durumda kalan `0` olacaktır. Şu anki bulunduğumuz index ise `1`'dir. Bizden istenen alt dizi uzunluğunun "en az 2" olmasıdır. Koddaki uzunluk kontrolü `şuanki_index - eski_index >= 2` şeklindedir. Eğer biz `0` kalanının en baştaki varsayılan indexini `-1` olarak kabul edersek; formül `1 - (-1) = 2` olur ve şart kusursuz bir şekilde sağlanır. Eğer bunu `-1` vermeseydik, sıfırıncı indexten başlayan geçerli alt dizilerin uzunluklarını eksik ölçeceğimiz için hatalı sonuç alırdık.

```python
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        summ = 0
        
        for index, val in enumerate(nums):
            summ += val
            rem = summ % k
            
            if rem in remainder_map:
                if index - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = index
                
        return False
```

**Time Complexity:** `O(N)`
Diziyi sadece bir kez baştan sona tararız. Hash map'te arama ve ekleme işlemleri ortalamada `O(1)` sürede gerçekleşir.

**Space Complexity:** `O(min(N, k))`
Sözlük, kalan değerlerini tutar. Bir sayının `k`'ya bölümünden en fazla `k` farklı kalan çıkabileceği için sözlük en fazla `k` eleman tutar.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force - Time Limit Exceeded)

Tüm alt dizilerin toplamını tek tek kontrol eden en temel yaklaşımdır. Dış döngü `i` başlangıç noktasını, iç döngü `j` ise bitiş noktasını belirler. İç döngü her zaman `i+1`'den başladığı için, alt dizinin uzunluğu doğal olarak en az 2 olur. `summ` değişkenine ekleme yaparken toplam `k`'ya tam bölünürse anında `True` döndürürüz.

```python
class SolutionBruteForce:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        for i in range(0, len(nums)-1):
            summ = nums[i]
            for j in range(i+1, len(nums)):
                summ += nums[j]
                if summ % k == 0:
                    return True
                    
        return False
```

**Time Complexity:** `O(N^2)`
Her bir `i` elemanı için dizinin geri kalanı tekrar taranır. Bu durum büyük veri setlerinde (LeetCode test case'lerinde) Zaman Aşımına (Time Limit Exceeded) sebep olur.

**Space Complexity:** `O(1)`
Sadece toplamı takip ettiğimiz `summ` değişkeni kullanılır.