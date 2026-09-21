> 💡 **Not:** Bu soru **Prefix Sum** (Kümülatif Toplam) kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [0724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the **leftmost pivot index**. If no such index exists, return `-1`.

### Example 1:
> **Input:** `nums = [1,7,3,6,5,6]`  
> **Output:** `3`  
> **Explanation:**  
> The pivot index is 3.  
> Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11  
> Right sum = nums[4] + nums[5] = 5 + 6 = 11  

### Example 2:
> **Input:** `nums = [1,2,3]`  
> **Output:** `-1`  
> **Explanation:**  
> There is no index that satisfies the conditions in the problem statement.  

---

### Türkçe Açıklama

Sana `nums` adında bir tam sayı dizisi veriliyor. Senden istenen, dizinin **pivot indeksini** bulmandır.
Pivot indeks, o indeksin **tam solunda** kalan tüm sayıların toplamının, **tam sağında** kalan tüm sayıların toplamına eşit olduğu noktadır. 

Eğer pivot indeks dizinin en başındaysa sol tarafın toplamı 0 kabul edilir. Aynı şey en sağdaki eleman için de geçerlidir. Varsa en soldaki (ilk karşılaşılan) pivot indeksi döndür, yoksa `-1` döndür.

---

### 1. Prefix Sum Matematiksel Yaklaşımı (Optimal)

Her indeks için sol ve sağ toplamları `while` veya `for` döngüleriyle sıfırdan hesaplamak yerine çok basit bir denklem kurarız. İlk iş olarak dizideki tüm sayıların toplamını (`total_sum`) buluruz.

**Matematiksel Mantık ve `val` (O Anki Sayı) Trick'i:**
Dizideki herhangi bir indeks noktasında durduğumuzda, o anki tablo tam olarak 3 parçadan oluşur:
1. Solumuzda kalanların toplamı (`left_sum`)
2. Tam üstünde durduğumuz sayının kendisi (`val`)
3. Sağımızda kalanların toplamı (`right_sum`)

Denklem olarak yazarsak: `Genel Toplam = Sol Toplam + O Anki Sayı + Sağ Toplam`
Bizim amacımız sağ tarafı bulmak olduğuna göre, denklemi tersine çeviririz:
`Sağ Toplam = Genel Toplam - Sol Toplam - O Anki Sayı`

İşte bu kadar! Yeni bir döngü kurmaya gerek kalmadan sağ tarafın toplamını anında buluruz. Ardından `left_sum == right_sum` diyerek solun sağa eşit olup olmadığını kontrol ederiz. Değilse, üzerinde durduğumuz sayıyı sol toplama ekler ve bir sonraki adıma geçeriz.

```python
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for index, val in enumerate(nums):
            right_sum = total_sum - left_sum - val
            
            if left_sum == right_sum:
                return index
                
            left_sum += val
            
        return -1
```

**Time Complexity:** `O(N)`  
Diziyi iki kere tararız. Birincisi `sum()` fonksiyonu ile genel toplamı bulurken, ikincisi pivot ararken. Döngü içinde döngü olmadığı için $O(N)$ zaman alır.

**Space Complexity:** `O(1)`  
Sadece toplam değerleri tutan değişkenler kullandığımız için ekstra hafıza maliyeti yoktur.

--- 

### 2. Çift While Döngüsü Yaklaşımı (Brute Force)

Mantığı en basit ama en verimsiz yöntemdir. Dışarıdaki bir döngü ile dizinin her bir elemanını tek tek seçeriz. Seçtiğimiz her eleman için iki ayrı `while` döngüsü başlatırız. İlk döngü sıfırdan o indekse kadar olan sayıları, ikinci döngü ise dizinin sonundan o indekse kadar olan sayıları toplar. 

```python
class SolutionBruteForce:
    def pivotIndex(self, nums: list[int]) -> int:
        for index, val in enumerate(nums):
            left = 0
            right = len(nums) - 1
            left_sum = 0
            right_sum = 0
            
            while left < index:
                left_sum += nums[left]
                left += 1
                
            while index < right:
                right_sum += nums[right]
                right -= 1
                
            if right_sum == left_sum:
                return index
                
        return -1
```

**Time Complexity:** `O(N^2)`  
Her bir indeks noktası için sol ve sağ taraf en baştan tekrar hesaplandığı için iç içe döngü mantığıyla karesel bir zaman karmaşıklığı oluşur.

**Space Complexity:** `O(1)`  
Ekstra bellek kullanılmaz.