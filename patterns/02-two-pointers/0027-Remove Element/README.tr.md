> 💡 **Not:** Bu soru **Two Pointers** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [27. Remove Element](https://leetcode.com/problems/remove-element/)

Suppose you have an integer array `nums` and a specific integer `val`. Your objective is to eliminate all instances of `val` from the array `nums` modifying it strictly in-place (without allocating another array). The order of the kept elements can be changed. You must return `k`, which represents the count of elements that are not equal to `val`. The judging system will verify that the first `k` positions of your array contain these valid elements.

### Example 1:
> **Input:** `nums = [3,2,2,3], val = 3`  
> **Output:** `2, nums = [2,2,_,_]`  

### Example 2:
> **Input:** `nums = [0,1,2,2,3,0,4,2], val = 2`  
> **Output:** `5, nums = [0,1,4,0,3,_,_,_]`  

---

### Türkçe Açıklama

Sana `nums` adında bir tam sayı dizisi ve `val` adında bir hedef sayı veriliyor. Senden istenen, dizinin içindeki tüm `val` değerlerini ekstra bir hafıza (yeni bir dizi) kullanmadan, doğrudan mevcut dizi üzerinde (in-place) silmendir. Kalan elemanların sırası önemli değildir. İşlem bittiğinde, dizide kalan geçerli (yani `val`'a eşit olmayan) elemanların sayısını (`k`) döndürmen gerekiyor.

---

### 1. In-Place Two Pointers Yaklaşımı (Optimal)

Bu, ekran görüntüsünde yer alan en optimal çözümdür. Hızlı ve yavaş pointer (fast and slow pointers) mantığını kullanır.

`for` döngüsündeki `i` değişkeni hızlı pointer'ımızdır; diziyi baştan sona tarar ve elemanların `val` değerine eşit olup olmadığına bakar. `k` değişkeni ise yavaş pointer'ımızdır; dizide geçerli (silinmemesi gereken) bir sayının yerleştirileceği bir sonraki güvenli indeksi takip eder. Eğer `nums[i]` değeri hedef sayıya eşit değilse, bu sayıyı `nums[k]` pozisyonuna kopyalarız ve `k`'yı bir artırırız. Bu sayede tüm geçerli sayılar dizinin en başına sıkıştırılmış olur.

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

**Time Complexity:** `O(N)`

`for` döngüsü ile diziyi baştan sona sadece bir kez gezdiğimiz için zaman karmaşıklığı lineerdir.

**Space Complexity:** `O(1)`

İşlemi in-place (dizinin kendi üzerinde) yaptığımız ve sadece indeks takibi için `k` değişkenini kullandığımız için ekstra hafıza kullanılmaz.

--- 

### 2. Built-in Remove Yaklaşımı (Alternatif / Brute Force)

Python'un gömülü `in` operatörünü ve `remove()` metodunu kullanarak hedef sayıyı bulup diziden silebiliriz. Bu yöntem in-place kuralına uysa da çok yavaştır. Çünkü hem sayının dizide olup olmadığını aramak hem de onu sildikten sonra sağındaki tüm elemanları birer adım sola kaydırmak dizinin tamamını taramayı gerektirir ve bu durum karesel bir zaman maliyeti yaratır.

```python
class SolutionBruteForce:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
```

**Time Complexity:** `O(N^2)`

`in` araması `O(N)` sürer, `remove()` ile silip elemanları sola kaydırmak da `O(N)` sürer. Bunlar bir döngü içinde tekrarlandığı için toplam karmaşıklık `O(N^2)` olur.

**Space Complexity:** `O(1)`

Yavaş olmasına rağmen bu metot da diziyi kendi üzerinde modifiye ettiği için ekstra alan gerektirmez.