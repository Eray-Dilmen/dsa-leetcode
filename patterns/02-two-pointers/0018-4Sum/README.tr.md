> 💡 **Not:** Bu soru **Two Pointers (İki İşaretçi)** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [18. 4Sum](https://leetcode.com/problems/4sum/)

**Problem Statement**
Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
* `0 <= a, b, c, d < n`
* `a`, `b`, `c`, and `d` are distinct.
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

### Example 1:
> **Input:** `nums = [1,0,-1,0,-2,2], target = 0`  
> **Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`  

### Example 2:
> **Input:** `nums = [2,2,2,2,2], target = 8`  
> **Output:** `[[2,2,2,2]]`  

---

**Türkçe Açıklama**
Sana `n` tane tam sayıdan oluşan bir `nums` dizisi veriliyor. Senden istenen, toplamları `target` (hedef) değerine eşit olan tüm benzersiz dörtlüleri (quadruplets) bulmandır. Bulduğun dörtlülerin içinde aynı sayılar farklı indekslerden seçilmiş olsa bile, genel sonuç kümesinde birbirinin kopyası olan (aynı sayılardan oluşan) dörtlüler bulunmamalıdır.

---

### 1. Sorting & Two Pointers Yaklaşımı (Optimal)

Bu, 4Sum problemi için en optimal çözümdür ve 3Sum probleminin mantığı üzerine inşa edilmiştir. Diziyi en başta küçükten büyüğe sıralayarak, ilk iki sayıyı iç içe geçmiş iki döngüyle (`i` ve `j`) sabitleriz. Kalan iki sayıyı ise dizinin geri kalan kısmında **Two Pointers** (`lo` ve `hi`) tekniği ile ararız.

Sıralama işlemi kritik bir role sahiptir; çünkü aynı değere sahip sayıları atlamamıza (skip duplicates) olanak tanır. Böylece ekstra bir Hash Set kullanmadan doğrudan benzersiz dörtlülere ulaşırız.

```python
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Space Complexity = O(1) veya O(N) -> Sonuç dizisi hariç, sort işleminin hafızasına bağlıdır
        n = len(nums)
        answer = []
        
        # Time Complexity = O(N log N) -> Diziyi baştan sıralıyoruz
        nums.sort()
        
        # Time Complexity = O(N^3) -> İç içe iki döngü O(N^2) * Two Pointers Taraması O(N)
        for i in range(n - 3):
            # İlk sayı için tekrarları atla
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # İkinci sayı için tekrarları atla
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                lo, hi = j + 1, n - 1
                while lo < hi:
                    summ = nums[i] + nums[j] + nums[lo] + nums[hi]
                    
                    if summ == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        
                        # Üçüncü ve dördüncü sayılar için tekrarları atla
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                            
                    elif summ < target:
                        lo += 1
                    else:
                        hi -= 1
                        
        return answer
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N^3)$
Sıralama işlemi $O(N \log N)$ sürer. En dıştaki iki döngü $O(N^2)$, en içteki Two Pointers döngüsü ise $O(N)$ zaman alır. Bu da genel zaman karmaşıklığını 4Sum için optimal olan $O(N^3)$ seviyesine getirir.
**Space Complexity (Alan Karmaşıklığı):** $O(1)$ veya $O(N)$
Ekstra bir dizi oluşturulmaz (sonuç dizisi hariç), ancak Python'daki Timsort algoritması sıralama yaparken arka planda $O(N)$ hafıza kullanabilir.

--- 

### 2. Brute Force Yaklaşımı (Time Limit Exceeded)

En basit yöntem, dört tane iç içe döngü kurarak olası tüm dörtlü kombinasyonları tek tek kontrol etmektir. "Benzersiz dörtlüler" kuralını sağlamak için ise bulunan sonuçları sıralayıp bir Hash Set içerisine atabiliriz.

```python
class SolutionBruteForce:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Space Complexity = O(N) -> Benzersiz kombinasyonları tutan Set yüzünden
        n = len(nums)
        unique_quads = set()
        
        # Time Complexity = O(N^4) -> İç içe 4 döngü kullanılıyor
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            # Set'e eklerken sıralamak tekrarları önler
                            quad = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                            unique_quads.add(quad)
                            
        return [list(q) for q in unique_quads]
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N^4)$
Tüm ihtimalleri denemek $O(N^4)$ sürer. Sorudaki kısıtlamalara göre bu çözüm kesinlikle Time Limit Exceeded (TLE) hatası alır.
**Space Complexity (Alan Karmaşıklığı):** $O(N)$
Hash Set, bulunan tüm benzersiz dörtlülere yetecek kadar ekstra hafıza kaplar.