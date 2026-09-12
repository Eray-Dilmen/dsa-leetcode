> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [1. Two Sum](https://leetcode.com/problems/two-sum/)


You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

### Example 1:
> **Input:** `nums = [2,7,11,15]`, `target = 9`
> 
> **Output:** `[0,1]`
> 
> **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
> **Input:** `nums = [3,2,4]`, `target = 6`
> 
> **Output:** `[1,2]`

### Example 3:
> **Input:** `nums = [3,3]`, `target = 6`
> 
> **Output:** `[0,1]`

---

### Türkçe Açıklama

Bizden bir sayı dizisi (`nums`) ve bir hedef sayı (`target`) veriliyor. Dizideki hangi iki sayının toplamının bu hedef sayıya eşit olduğunu bulmamız ve bu iki sayının **indekslerini** (yerlerini) döndürmemiz isteniyor. Her test case için kesinlikle bir çözüm olduğu ve aynı indeksteki elemanı iki kere kullanamayacağımız belirtilmiş.

> **Not:** Hash table kalıbı (pattern), bir elemanı ararken diziyi baştan sona tekrar taramak yerine (ki bu `O(n)` sürer), elemanları ve indekslerini bir sözlüğe (Hash Map) kaydederek daha sonra bu elemanları `O(1)` sürede bulmak için kullanılır.

---

### 1. Hash Map Yaklaşımı (Optimal)

* Diziyi tek bir döngüyle gezeriz. Her adımda şu anki sayıyı hedeften çıkararak aradığımız "diğer sayıyı" (`target - num`) buluruz.
* Eğer bu aradığımız "diğer sayı" Hash Map'te varsa, eşleşmeyi bulduk demektir; ikisinin indeksini döndürürüz.
* Eğer yoksa, şu anki sayıyı ve indeksini Hash Map'e (`mapping[num] = index`) kaydeder, bir sonraki sayıya geçeriz.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} # Space Complexity = O(n)

        # Time Complexity = O(n) -> Dizi içindeki elemanları bir kere gezer
        for index, num in enumerate(nums):
            # Aranan sayının map içinde olup olmadığı kontrol edilir (O(1) zaman alır)
            if (target - num) in mapping:
                return [mapping[target - num], index]
            else:
                # Sayı map'te yoksa değeri anahtar, indeksi value olarak kaydedilir
                mapping[num] = index
```

**Time Complexity:** `O(n)`


Dizideki tüm elemanlar `enumerate` ile tek bir `for` döngüsü kullanılarak sadece bir kez gezilir, bu `O(n)` zaman alır. Sözlük (Hash Map) içinde arama yapma (`in` anahtar kelimesi) işlemi ortalama `O(1)` sürede gerçekleştiği için toplam karmaşıklık `O(n)` olur.

**Space Complexity:** `O(n)`


Dizideki sayıları ve indekslerini tutabilmek için `mapping` adında ekstra bir sözlük yapısı oluşturduk. En kötü senaryoda (örneğin aradığımız ikili dizinin en sonundaysa), dizideki tüm elemanlar bu sözlüğe eklenebilir. Bu yüzden kullanılan ekstra alan dizinin uzunluğu (`n`) ile doğru orantılı olarak `O(n)` olur.

--- 

### 2. Brute Force Yaklaşımı

* Tüm olasılıkları denemek için iç içe iki döngü (nested loop) kurarız.
* İlk döngü dizideki ilk sayıyı seçer, ikinci döngü ise geri kalan sayıları tek tek gezerek toplamlarının `target` olup olmadığına bakar.
* Bu yöntem her bir eleman için dizinin geri kalanını tekrar taradığı için maliyetlidir.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Space Complexity = O(1)
        
        # Time Complexity = O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**Time Complexity:** `O(n^2)`

Dizi içindeki her bir eleman için (`n`), geri kalan diğer tüm elemanlar (`n-1`) tekrar kontrol edilir. Bu iç içe döngü durumu karmaşıklığı `O(n^2)` seviyesine çıkarır.

**Space Complexity:** `O(1)`

Ekstra hiçbir veri yapısı (liste, sözlük vb.) kullanılmadığı için hafızada kaplanan alan sabittir.