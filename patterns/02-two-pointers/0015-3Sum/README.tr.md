> 💡 **Not:** Bu soru **Two Pointers** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [15. 3Sum](https://leetcode.com/problems/3sum/)


Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Example 1:
> **Input:** `nums = [-1,0,1,2,-1,-4]`  
> **Output:** `[[-1,-1,2],[-1,0,1]]`  
> **Explanation:**  
> nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.  
> nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.  
> nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.  
> The distinct triplets are [-1,0,1] and [-1,-1,2].  
> Notice that the order of the output and the order of the triplets does not matter.

### Example 2:
> **Input:** `nums = [0,1,1]`  
> **Output:** `[]`  
> **Explanation:** The only possible triplet does not sum up to 0.  

### Example 3:
> **Input:** `nums = [0,0,0]`  
> **Output:** `[[0,0,0]]`  
> **Explanation:** The only possible triplet sums up to 0.


---

### Türkçe Açıklama
Sana tam sayılardan oluşan bir `nums` dizisi veriliyor. Senden istenen, dizinin içinden seçeceğin **farklı indekslerdeki** 3 sayının toplamının `0` olduğu tüm olasılıkları (üçlü gruplar halinde) döndürmen. Bulduğun çözüm kümesinde birbirinin aynısı olan (kopya) üçlüler bulunmamalıdır.

---

### 1. Two Pointers & Hash Set Yaklaşımı (Optimal)

Üç sayının toplamını bulmak için diziyi sabit bir nokta (pivot) etrafında tarayabiliriz. İlk sayıyı (`nums[i]`) sabitleriz ve geriye kalan iki sayıyı bulmak için **Two Pointers** tekniğini kullanırız. 
Bunun düzgün çalışabilmesi için önce diziyi `nums.sort()` ile küçükten büyüğe sıralamalıyız. Çözüm kümesinde tekrar eden üçlülerin olmaması için sonuçları bir **Set** içerisine tuple (demet) olarak atarız.

> ⚠️ **Geçmişten Bir Ders: Liste içinde `not in` ile kopya aramak**
> 
> ```python
> # ❌ HATALI VE YAVAŞ YAKLAŞIM
> l = []
> if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in l:
>     l.append([nums[i], nums[left], nums[right]])
> ```
> Eğer `l` değişkenini bir Liste (`[]`) olarak tanımlayıp, her eşleşme bulduğunda `not in l` diyerek "bu üçlü listede var mı?" diye kontrol edersen, Python o listeyi baştan sona taramak zorunda kalır (`O(k)` zaman). Zaten iç içe döngüde olduğumuz için bu arama işlemi binlerce kez tekrarlanır ve kodun çok yavaşlayıp **Time Limit Exceeded (TLE)** hatası almasına sebep olur.
> 
> **Doğru Yöntem:** `l = set()` kullanarak eşleşmeleri kümeye eklersen (`l.add(...)`), Set veri yapısı Hash Map mimarisi kullandığı için aynı elemandan olup olmadığını `O(1)` sürede anında tespit eder ve fazladan efor harcamadan kopyaları otomatik olarak reddeder.

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Space Complexity = O(n) -> Benzersiz üçlüleri set içinde tutuyoruz
        nums.sort()
        l = set()
        
        # Time Complexity = O(n^2)
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    l.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
                    
        return list(l)
```

**Time Complexity:** `O(n^2)` 

Diziyi sıralamak `O(n log n)` sürer. Sonrasında dıştaki `for` döngüsü `n` kez çalışırken, içindeki `while` döngüsü kalan elemanları taradığı için `O(n)` sürer. `O(n) * O(n) = O(n^2)` asimptotik olarak en baskın değer olduğu için genel karmaşıklık `O(n^2)` olur.

**Space Complexity:** `O(n)` 

Bulduğumuz geçerli üçlüleri benzersiz şekilde tutabilmek için `l` adında bir Hash Set oluşturuyoruz. En kötü durumda çözüm sayısı girdiye bağlı olarak artacağı için hafızada `O(n)` alan kaplar.

--- 

### 2. Brute Force Yaklaşımı

Dizideki her 3'lü kombinasyonu teker teker kontrol etmek için iç içe üç tane döngü yazarız. Toplamı 0 olanları Set içine atarız. Kesin çözüm üretir ancak inanılmaz derecede yavaş çalışır.

```python
class SolutionBruteForce:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Space Complexity = O(n)
        # Time Complexity = O(n^3)
        nums.sort()
        l = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l.add((nums[i], nums[j], nums[k]))
                        
        return list(l)
```

**Time Complexity:** `O(n^3)`

İç içe geçen 3 döngü, girdi boyutu büyüdükçe çalışma süresini kübik olarak artırır.

**Space Complexity:** `O(n)`

Tekrar eden üçlüleri önlemek için kullanılan `set` yapısı ve sonuçları tutmak için dönüştürülen liste, bulunan üçlülerin sayısına bağlı olarak ekstra hafıza kullanır.