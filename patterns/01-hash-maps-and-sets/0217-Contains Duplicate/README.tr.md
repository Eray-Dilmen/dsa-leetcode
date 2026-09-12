> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)


Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:
> **Input:** `nums = [1,2,3,1]`  
> **Output:** `true`

### Example 2:
> **Input:** `nums = [1,2,3,4]`  
> **Output:** `false`

### Example 3:
> **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
> **Output:** `true`

---

### Türkçe Açıklama
Sana `nums` adında tam sayılardan oluşan bir dizi veriliyor. Eğer dizideki herhangi bir değer en az iki kez geçiyorsa `true`, tüm elemanlar birbirinden farklıysa (hiç tekrar yoksa) `false` döndürmen isteniyor. Amacın dizide kopya/tekrar eden eleman olup olmadığını bulmaktır.

> **Not:** Hash Set kalıbı, bir elemanın varlığını `O(1)` sürede kontrol etmek için kullanılır. Döngü sırasında elemanları bir kümeye (Set) ekleyerek, o elemanı daha önce görüp görmediğimizi anında tespit ederiz ve `O(n^2)` süren iç içe döngülerden kurtuluruz.

---

### 1. Hash Set Yaklaşımı (Optimal)

Dizi üzerinde `O(1)` sürede arama yapabilen bir Hash Set kullanılır. Elemanları tek tek kümeye eklerken, o elemanın zaten kümede olup olmadığına bakarız. Eğer kümede varsa, o elemandan daha önce de görülmüş demektir ve anında `True` döneriz (Erken Çıkış / Early Exit).

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = set()
        
        for number in nums:
            if number in numbers:
                return True
            numbers.add(number)
            
        return False
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n)`
En kötü senaryoda (hiç tekrar yoksa) dizi bir kez tamamen gezilir. Set üzerinde arama yapmak ortalama `O(1)` sürdüğü için genel karmaşıklık `O(n)` olur.

**Space Complexity (Alan Karmaşıklığı):** `O(n)`
En kötü senaryoda tüm benzersiz elemanlar Set içinde saklanır, bu da dizinin boyutuyla doğru orantılı bir alan gerektirir.

---

### 2. Frequency Map Yaklaşımı (Alternatif)

Bir sözlük (Dictionary) kullanılarak her sayının dizide kaç kez geçtiği hesaplanır. Daha sonra sözlükteki elemanlar gezilerek herhangi bir sayının frekansının 1'den büyük olup olmadığına bakılır.

```python
class SolutionFrequencyMap:
    def containsDuplicate(self, nums: list[int]) -> bool:
        number_count = {}
        
        for number in nums:
            if number not in number_count:
                number_count[number] = 1
            else:
                number_count[number] += 1
        
        for number in number_count:
            if number_count[number] > 1:
                return True
        
        return False
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n)`
Sözlüğü doldurmak `O(n)` zaman alır. İkinci aşamada sözlükteki benzersiz elemanları gezmek en kötü durumda yine `O(n)` sürer. Toplam `O(2n)` işlemi katsayı atılarak `O(n)` olarak ifade edilir.

**Space Complexity (Alan Karmaşıklığı):** `O(n)`
En kötü durumda tüm benzersiz sayılar ve sayı frekansları sözlükte tutulur. Asimptotik olarak Hash Set ile aynı olsa da, sözlükler (key-value mantığıyla) bellekte biraz daha fazla yer kaplar.

---

### 3. Brute Force Yaklaşımı

İç içe iki döngü kurularak dizideki her bir eleman, kendisinden sonraki tüm elemanlarla tek tek karşılaştırılır. Eğer eşleşen iki eleman bulunursa `True` döndürülür. Ekstra alan kullanılmaz ancak zaman açısından çok yavaştır ve büyük dizilerde **Time Limit Exceeded (TLE)** hatası alır.

```python
class SolutionBruteForce:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                    
        return False
```

**Time Complexity (Zaman Karmaşıklığı):** `O(n^2)`
İç içe döngüler diziyi ortalama `n(n-1)/2` kez gezer.

**Space Complexity (Alan Karmaşıklığı):** `O(1)`
Ekstra bir veri yapısı oluşturulmaz.