> 💡 **Not:** Bu soru **Sliding Window (Kayan Pencere)** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Problem Statement**
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### Example 1:
> **Input:** `target = 7, nums = [2,3,1,2,4,3]`
> **Output:** `2`
> **Explanation:** The subarray `[4,3]` has the minimal length under the problem constraint.

### Example 2:
> **Input:** `target = 4, nums = [1,4,4]`
> **Output:** `1`

### Example 3:
> **Input:** `target = 11, nums = [1,1,1,1,1,1,1,1]`
> **Output:** `0`

---

**Türkçe Açıklama**
Sana sadece pozitif tam sayılardan oluşan bir `nums` dizisi ve pozitif bir `target` (hedef) sayısı veriliyor. Senden istenen, dizinin içindeki elemanların toplamı `target` sayısına eşit veya ondan büyük olan **en kısa** alt dizgenin (subarray) uzunluğunu bulmandır. Eğer böyle bir alt dizge yoksa geriye `0` döndürmelisin.

---

### 1. Sliding Window Yaklaşımı (Optimal)

Çözümde `l` (sol) ve `r` (sağ) işaretçilerini kullanarak bir kayan pencere (sliding window) oluşturuyoruz. Sağ işaretçimizle (`r`) diziyi baştan sona tararken, karşılaştığımız her sayıyı `summ` (toplam) değişkenine ekleyerek penceremizi genişletiyoruz.

Dizideki tüm sayılar pozitif olduğu için penceremizi sağa doğru genişlettikçe toplamın daima artacağını biliyoruz. Eğer penceremizin toplamı (`summ`), bizden istenen `target` hedefine ulaşır veya onu geçerse, geçerli bir alt dizge bulmuşuz demektir. Artık amacımız bu geçerli alt dizgeyi **mümkün olan en kısa** hale getirmektir. Bunun için sol işaretçimizi (`l`) sağa doğru kaydırarak penceremizi daraltmaya başlarız. Daraltma işlemi sırasında her seferinde minimum uzunluğu (`minn`) günceller ve pencereden çıkardığımız sol elemanı (`nums[l]`) toplamdan düşeriz. Toplam değerimiz `target`'ın altına düşene kadar pencereyi soldan daraltmaya devam ederiz.

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        minn = float('inf')
        summ = 0
        l = 0
        
        for r in range(len(nums)):
            summ += nums[r]
            
            while summ >= target:
                minn = min(minn, r - l + 1)
                summ -= nums[l]
                l += 1
                
        return minn if minn != float('inf') else 0
```

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force)

Tüm olası başlangıç noktalarından (indekslerden) yola çıkarak iç içe iki döngü ile alt dizgeleri kontrol edebiliriz. Her başlangıç noktası için sağa doğru sayıları toplarız. Toplam değerimiz `target` sayısına eşit veya ondan büyük olduğu anda alt dizgenin uzunluğunu kaydederiz. Dizideki sayılar pozitif olduğu için hedefi bulduktan sonra alt dizgeyi daha fazla uzatmanın bir mantığı yoktur, bu yüzden içteki döngüyü kırıp (`break`) bir sonraki başlangıç elemanına geçeriz. Bu yöntem O(N^2) zaman alır.

```python
class SolutionBruteForce:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        minn = float('inf')
        n = len(nums)
        
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                if summ >= target:
                    minn = min(minn, j - i + 1)
                    break
                    
        return minn if minn != float('inf') else 0
```