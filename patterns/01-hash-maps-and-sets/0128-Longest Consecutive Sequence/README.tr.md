> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)


Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in `O(n)` time.

### Example 1:
> **Input:** `nums = [100,4,200,1,3,2]`  
  **Output:** `4`  
  **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

### Example 2:
> **Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`  
  **Output:** `9`  

---

### Türkçe Açıklama
Sana karışık sırada tam sayılardan oluşan bir `nums` dizisi veriliyor. Ardışık olarak (peş peşe) devam eden en uzun sayı dizisinin uzunluğunu bulman isteniyor.
*(Önemli Şart: Algoritman kesinlikle `O(n)` zaman karmaşıklığında çalışmalıdır).*

---

### 1. Hash Set Yaklaşımı (Optimal)

Sorunun bizden kesin olarak istediği $O(N)$ zaman karmaşıklığına ulaşmak için diziyi sıralayamayız (çünkü sıralama işlemi $O(N \log N)$ sürer). Bunun yerine diziyi bir Hash Set'e (Kümeye) çeviririz. Bu bize $O(1)$ sürede eleman arama imkanı sunar.

Buradaki en kritik ve zekice mantık **dizinin başlangıç noktasını** bulmaktır. Bir sayı, sadece ve sadece kendisinden bir önceki sayı (`num - 1`) kümede **yoksa** bir ardışık dizinin başlangıcı olabilir. 
Bir başlangıç noktası yakaladığımızda, `num + 1`, `num + 2` kümede var mı diye saymaya başlarız. Sadece dizilerin en başındaki sayılar için `while` döngüsünü tetiklediğimizden, gereksiz tekrarlardan kurtulmuş oluruz.

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Space Complexity = O(N) -> Benzersiz elemanları kümede tutuyoruz
        s = set(nums)
        longest = 0
        
        # Time Complexity = O(N) -> Her sayı maksimum 2 kez ziyaret ediliyor
        for num in s:
            # Sayının bir dizinin başlangıcı olup olmadığını kontrol et
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                
                # Ardışık seriyi say
                while next_num in s:
                    length += 1
                    next_num += 1
                    
                longest = max(longest, length)
                
        return longest
```

**Time Complexity:** $O(N)$

`for` döngüsünün içinde bir `while` döngüsü olmasına rağmen, `while` döngüsü yalnızca bir serinin başlangıç sayısını bulduğumuzda çalışır. Bu sayede her eleman `while` tarafından en fazla 1 kere işlenir. Toplam süre kesinlikle $O(N)$'dir.

**Space Complexity:** $O(N)$

Dizideki elemanları saklamak için oluşturduğumuz Hash Set, eleman sayısıyla orantılı olarak hafızada yer kaplar.

--- 

### 2. Sorting Yaklaşımı (Alternatif / Daha Yavaş)

Diziyi önce küçükten büyüğe sıralayıp, ardından yan yana duran ardışık sayıları sayabiliriz. Mantıksal olarak doğru çalışsa da, sıralama (`sort`) işlemi zaman karmaşıklığını $O(N \log N)$ seviyesine çıkarır. Bu durum sorunun $O(N)$ kuralını ihlal eder, ancak mülakatlarda asıl optimizasyona geçmeden önce sunulabilecek güzel bir temel mantıktır.

```python
class SolutionSorting:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Space Complexity = O(1) veya O(N) (Kullanılan dilin sort algoritmasına bağlı)
        if not nums:
            return 0
            
        # Time Complexity = O(N log N) -> Diziyi sıralama maliyeti
        nums.sort()
        
        longest = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    longest = max(longest, current_streak)
                    current_streak = 1
                    
        return max(longest, current_streak)
```

**Time Complexity:** $O(N \log N)$

En baskın işlem olan diziyi sıralama işlemi $O(N \log N)$ sürer.

**Space Complexity:** $O(1)$ veya $O(N)$

Python'un Timsort algoritması sıralama yaparken arka planda $O(N)$ ekstra alan kullanır.