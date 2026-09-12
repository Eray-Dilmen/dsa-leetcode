> 💡 **Not:** Bu soru **Two Pointers** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

### Example 1:
> **Input:** `numbers = [2,7,11,15]`, `target = 9`  
> **Output:** `[1,2]`  
> **Explanation:** The sum of 2 and 7 is 9. Therefore, `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

### Example 2:
> **Input:** `numbers = [2,3,4]`, `target = 6`  
> **Output:** `[1,3]`  
> **Explanation:** The sum of 2 and 4 is 6. Therefore `index1 = 1`, `index2 = 3`. We return `[1, 3]`.

---

### Türkçe Açıklama

Sana önceden **küçükten büyüğe sıralanmış** ve indeksleri 1'den başlayan (`1-indexed`) bir `numbers` dizisi veriliyor. Toplamları verilen `target` (hedef) sayısına eşit olan iki sayıyı bulman ve bu sayıların dizideki indekslerini döndürmen isteniyor. Çözümünün hafızada ekstra yer kaplamaması (`O(1)` space) şartı koşulmuş.

---

### 1. Two Pointers Yaklaşımı (Optimal)

* Dizi halihazırda sıralı olduğu için ekstra bir Hash Map kullanıp hafızayı `O(N)` seviyesine çıkarmamıza gerek yoktur. Uçlardan merkeze doğru ilerleyen **Two Pointers** kalıbıyla `O(N)` sürede optimum sonuca ulaşabiliriz.
* Dizi küçükten büyüğe sıralı olduğu için en başa (`left`) ve en sona (`right`) birer pointer yerleştiririz. Bu iki pointer'ın gösterdiği sayıların toplamına bakarız.
* Toplam hedefe eşitse, aradığımızı bulduk demektir (dizi 1'den başladığı için indekslere 1 ekleyerek döndürürüz).
* Toplam hedeften **büyükse**, sayıyı küçültmemiz gerekir. Bunun için sağdaki pointer'ı (`right`) bir adım sola kaydırarak daha küçük bir sayıya geçeriz.
* Toplam hedeften **küçükse**, sayıyı büyütmemiz gerekir. Bunun için soldaki pointer'ı (`left`) bir adım sağa kaydırarak daha büyük bir sayıya geçeriz.

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
```

**Time Complexity:** `O(N)`

İki pointer uçlardan başlayıp birbirlerine doğru ilerler ve en kötü senaryoda ortada buluşurlar. Dizi sadece bir kez taranmış olur.

**Space Complexity:** `O(1)`

Sadece `left` ve `right` adında iki değişken kullandığımız için ekstra hafıza tüketilmez. Sorunun bizden istediği "constant extra space" kuralı sağlanmış olur.

--- 

### 2. Brute Force Yaklaşımı (Time Limit Exceeded)

* Tüm olası sayı çiftlerini denemek için iç içe iki döngü kurarız. 
* Mantıksal olarak doğru çalışsa da, dizinin "sıralı" olma avantajını tamamen çöpe atar. 
* Görseldeki test analizinde de görüldüğü üzere büyük dizilerde **Time Limit Exceeded (TLE)** (Zaman Aşımı) hatası alarak başarısız olur.

```python
class SolutionBruteForce:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
```

**Time Complexity:** `O(N^2)`

Dizideki her bir eleman için geri kalan tüm elemanlar tekrar tekrar taranır.

**Space Complexity:** `O(1)`

Ekstra bir veri yapısı oluşturulmaz.