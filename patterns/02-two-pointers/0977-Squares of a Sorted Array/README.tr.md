> 💡 **Not:** Bu soru **Two Pointers** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Example 1:
> **Input:** `nums = [-4,-1,0,3,10]`  
> **Output:** `[0,1,9,16,100]`  
> **Explanation:** After squaring, the array becomes `[16,1,0,9,100]`. After sorting, it becomes `[0,1,9,16,100]`.

### Example 2:
> **Input:** `nums = [-7,-3,2,3,11]`  
> **Output:** `[4,9,9,49,121]`  

---

### Türkçe Açıklama

Sana küçükten büyüğe sıralanmış bir `nums` dizisi veriliyor. Senden istenen, dizideki her bir sayının karesini alıp yine küçükten büyüğe sıralanmış yeni bir dizi döndürmendir.

---

### 1. Two Pointers & Reverse Yaklaşımı (Optimal)

* Girdi dizisi halihazırda sıralıdır ancak negatif sayılar içerir. Sayıların karesini aldığımızda değerler bir "V" şekli oluşturur: En büyük kareler her zaman en uçlarda (ya baştaki büyük negatif sayılar ya da sondaki büyük pozitif sayılar) bulunurken, en küçük kareler ortalarda (sıfıra yakın noktalarda) yer alır.
* Bu uç noktaları karşılaştırıp en büyüğünü seçerek sonuç dizimizi oluşturmak için **Two Pointers** kalıbını kullanabiliriz.

**Algoritmik Detaylar & "Neden"ler:**
* **Neden Min (`<`) yerine Max (`>`) arıyoruz?:** Mutlak olarak en büyük değerlerin dizinin en sağında veya en solunda olduğunu biliyoruz. Bu yüzden iki ucu kıyaslayıp dıştan içe doğru en büyükleri toplamak çok daha kolaydır. Eğer en küçükleri bulmaya çalışsaydık, dizinin içindeki "sıfır noktasını" (V şeklinin dibini) tespit edip oradan dışa doğru genişlememiz gerekirdi ki bu kodu çok daha karmaşık hale getirirdi.
* **Neden `while left < right` yerine `<=`: ?** Eğer `<` kullansaydık, iki pointer dizinin tam ortasındaki son elemanda buluştuğunda döngü biterdi. Bu durumda o ortadaki son elemanın karesi alınmaz ve sonuca eklenmeden atlanmış olurdu. `<=` (küçük eşittir) kullanmak dizideki her bir elemanın eksiksiz işlenmesini garanti eder.
* **Neden `.reverse()` kullanıyoruz?:** Elemanları en büyükten küçüğe doğru seçip `result` listemize eklediğimiz için, listemiz azalan (büyükten küçüğe) şekilde oluşur. Sorunun bizden istediği artan sıralamayı elde etmek için en sonda listeyi tersine çeviririz. `.reverse()` işlemi `O(N)` zaman alır. Zaten pointer taramamız da `O(N)` sürmüştü. `O(N) + O(N) = O(N)` olduğu için genel zaman karmaşıklığımız bozulmaz.
* **Neden ekstra bir `result[]` listesi açtık? (In-place yapılamaz mıydı?):** Hafızadan tasarruf etmek için orijinal diziyi değiştirmeye (in-place) kalksaydık, yeni bulduğumuz elemanı dizinin en başına eklememiz gerekirdi. Bir diziye en baştan eleman eklemek, içerideki diğer tüm elemanları birer adım sağa kaydırmayı gerektirir (her ekleme için `O(N)` zaman). Bu da algoritmayı `O(N^2)` gibi korkunç bir yavaşlığa sürüklerdi. Zaman karmaşıklığını `O(N)` seviyesinde tutabilmek için `O(N)` boyutunda ekstra bir alan (Space) feda etmek **zorunludur**.

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = []
        
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[right]**2)
                right -= 1
                
        result.reverse()
        return result
```

**Time Complexity:** `O(N)`

Diziyi pointer'larla bir kez tararız (`O(N)`), çıkan listeyi ters çevirmek de (`O(N)`) sürer. Toplam süre `O(N)`'dir.

**Space Complexity:** `O(N)`

Karelenmiş değerleri tutmak için N elemanlı yeni bir `result` dizisi ayırmak zorundayız.

--- 

### 2. Karesini Alıp Sıralama (Alternatif / Brute Force)

* En düz mantık çözüm, diziyi tek tek gezip her elemanın karesini kendi üzerine yazmak ve ardından Python'un gömülü sıralama fonksiyonunu (`.sort()`) çağırmaktır. 
* Kod çok kısadır ancak sıralama algoritmasından dolayı optimalden daha yavaş çalışır.

```python
class SolutionSorting:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            
        nums.sort()
        return nums
```

**Time Complexity:** `O(N log N)`

Zamanı belirleyen temel işlem `.sort()` algoritmasıdır.

**Space Complexity:** `O(1)` veya `O(N)`

Orijinal dizi üzerinde değişiklik yapılır ancak arka planda kullanılan Timsort algoritması en kötü durumda `O(N)` ekstra alan kullanabilir.