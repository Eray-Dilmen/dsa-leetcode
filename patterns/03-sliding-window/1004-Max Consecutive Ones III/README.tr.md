> 💡 **Not:** Bu soru **Sliding Window** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

### Example 1:
> **Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2`  
> **Output:** `6`  
> **Explanation:** `[1,1,1,0,0,1,1,1,1,1,1]` 
> Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

### Example 2:
> **Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3`  
> **Output:** `10`  
> **Explanation:** `[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]` 
> Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

---

### Türkçe Açıklama

Sana sadece 0 ve 1'lerden oluşan `nums` adında bir dizi ve bir `k` tam sayısı veriliyor. Senden istenen, en fazla `k` adet 0'ı 1'e çevirme hakkını kullanarak, dizide arka arkaya gelen 1'lerin sayısını maksimum yapman ve bu maksimum uzunluğu döndürmendir.

---

### 1. Sliding Window Yaklaşımı (Optimal)

* Çözümde, `l` (sol) ve `r` (sağ) pointer'larıyla belirlenen bir Sliding Window kullanıyoruz. 
* Sağ pointer'ı (`r`) dizinin sonuna kadar ilerleterek penceremizi genişletiyoruz. Eğer karşılaştığımız eleman `0` ise, sıfır sayacımızı (`num_zeros`) artırıyoruz. 
* Eğer pencere içindeki sıfır sayısı bize verilen `k` hakkını aşarsa, pencerenin sol tarafını (`l`), pencereden bir `0` çıkarana kadar sağa doğru daraltıyoruz. 
* Her adımda pencerenin mevcut uzunluğunu hesaplayıp en büyük uzunluğu (`max_w`) güncelliyoruz.

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_w = 0
        num_zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            w = r - l + 1
            max_w = max(max_w, w)

        return max_w
```

**Time Complexity:** `O(N)`

Pointer'lar diziyi uçtan uca sadece bir kez taradığı için zaman karmaşıklığı lineerdir.

**Space Complexity:** `O(1)`

Ekstra bellek (dizi, sözlük vb.) kullanılmaz, yalnızca sayısal değişkenler tutulur.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force)

* Dizideki her bir elemandan başlayan tüm alt dizileri (subarrays) tek tek kontrol ederiz. 
* Her alt dizi için 0'ları sayarız ve eğer 0 sayısı `k` sınırını aşarsa o alt diziyi kontrol etmeyi bırakıp bir sonraki başlangıç elemanına geçeriz. 

```python
class SolutionBruteForce:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_w = 0
        n = len(nums)

        for i in range(n):
            num_zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    num_zeros += 1
                if num_zeros > k:
                    break
                max_w = max(max_w, j - i + 1)
                
        return max_w
```

**Time Complexity:** `O(N^2)`

İç içe iki döngü kullanıldığı için zaman karmaşıklığı karesel olur.

**Space Complexity:** `O(1)`

İlave bir veri yapısı tahsis edilmediğinden alan karmaşıklığı sabittir