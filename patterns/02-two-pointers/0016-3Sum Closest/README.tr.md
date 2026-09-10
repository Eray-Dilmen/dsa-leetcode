> 💡 **Not:** Bu soru **Two Pointers (İki İşaretçi)** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

**Problem Statement**
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

### Example 1:
> **Input:** `nums = [-1,2,1,-4], target = 1`  
  **Output:** `2`  
  **Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

### Example 2:
> **Input:** `nums = [0,0,0], target = 1`  
  **Output:** `0`  

---

**Türkçe Açıklama**
Sana `n` uzunluğunda bir `nums` tam sayı dizisi ve bir `target` (hedef) değeri veriliyor. Senden istenen, diziden seçeceğin 3 sayının toplamının hedefe en yakın olduğu durumu bulman ve bu toplamı döndürmendir. Her girdinin tam olarak tek bir çözümü olduğunu varsayabilirsin.

---

### 1. Sorting & Two Pointers Yaklaşımı (Optimal)

Bu yaklaşım, standart 3Sum problemiyle büyük ölçüde aynıdır. Diziyi baştan sıralayarak dıştaki döngü ile ilk sayıyı (`nums[i]`) sabitleriz. Dizinin geri kalan kısmında ise diğer iki sayıyı bulmak için Two Pointers (`lo` ve `hi`) tekniğini kullanırız.

Tam bir eşleşme aramak yerine, o anki toplam ile hedef arasındaki mutlak farkı (`abs(cur_sum - target)`) ölçerek `closest_sum` (en yakın toplam) değişkenini güncelleriz. Eğer hedef değere tam ulaşılırsa işlemi anında sonlandırıp sonucu döndürürüz. Aksi halde, toplamın küçük veya büyük olmasına göre işaretçileri daraltırız.

```python
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]
                
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                    
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1
                    
        return closest_sum
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N^2)$
Sıralama işlemi $O(N \log N)$ sürer. Dıştaki döngü $O(N)$, içteki Two Pointers taraması da $O(N)$ zaman alır. Genel karmaşıklık $O(N^2)$ olarak kabul edilir.
**Space Complexity (Alan Karmaşıklığı):** $O(1)$
Algoritma sadece birkaç temel değişken kullanır, ekstra bir dizi veya veri yapısı tahsis edilmez.

--- 

### 2. Brute Force Yaklaşımı (Alternatif)

Kaba kuvvet yöntemi, üç tane iç içe geçmiş döngü kullanarak olası tüm üçlü kombinasyonları tek tek kontrol eder. Her bir üçlünün toplamı hesaplanır ve hedefe daha yakın bir sonuç bulunursa `closest_sum` güncellenir.

```python
class SolutionBruteForce:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Time Complexity: O(N^3)
        # Space Complexity: O(1)
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if abs(cur_sum - target) < abs(closest_sum - target):
                        closest_sum = cur_sum
                        
        return closest_sum
```

**Time Complexity (Zaman Karmaşıklığı):** $O(N^3)$
Olası tüm üçlüleri denemek kübik zaman alır.
**Space Complexity (Alan Karmaşıklığı):** $O(1)$
Ekstra bellek kullanılmaz.