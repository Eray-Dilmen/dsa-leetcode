> 💡 **Not:** Bu soru `O(1)` alan karmaşıklığı için **Boyer-Moore Oylama Algoritması** ile, `O(n)` alan karmaşıklığı için ise **Hash Maps** kalıbı ile çözülür. Hash Map kalıbının genel mantığı için [README.md](../README.md) dosyasına bakabilirsiniz.

# [169. Majority Element](https://leetcode.com/problems/majority-element/)


Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

### Example 1:
> **Input:** `nums = [3,2,3]`  
> **Output:** `3`

### Example 2:
> **Input:** `nums = [2,2,1,1,1,2,2]`  
> **Output:** `2`

---

### Türkçe Açıklama
Sana `n` boyutunda bir `nums` dizisi veriliyor ve dizideki **çoğunluk elemanını (majority element)** bulman isteniyor.
Çoğunluk elemanı, dizide `n / 2` kereden daha fazla tekrar eden elemandır. Dizide her zaman bir çoğunluk elemanı bulunduğunu varsayabilirsin.

---

### 1. Boyer-Moore Oylama Algoritması (Optimal)

**Mantığı Nasıl Çalışıyor? (Neden O(1) Bellek Yeterli?)**
Temel mantık "birbirini yok etme" (kelle koltukta eşleşme) prensibine dayanır:

* Problem tanımına göre çoğunluk elemanı dizinin **yarısından fazlasını** kaplar ($> n/2$).
* Eğer çoğunluk elemanı ile onun dışındaki herhangi bir elemanı bir araya getirip ikisini birden diziden "silseydik", çoğunluk elemanı yine de yok edilemezdi; çünkü diğer tüm sayıların toplamından bile daha fazladır.
* Algoritma bunu şöyle simüle eder:
  * `ans` : O anki aday sayı.
  * `count` : Adayın gücü.
  * Karşına adayın kendisi çıkarsa gücü artar (`count += 1`).
  * Karşına adayın dışında farklı bir sayı çıkarsa birer taneleri birbirini yok eder (`count -= 1`).
  * Güç sıfırlandığında (`count == 0`), yeni gördüğün sayı yeni aday olur.
* Sonuçta, diğer tüm sayılar çoğunluk sayısını birer birer eksiltse dahi sayı üstünlüğü çoğunlukta olduğu için sonda kesinlikle gerçek çoğunluk elemanı kalır.

Sadece iki basit değişken (`ans` ve `count`) tuttuğun için hiçbir sözlük veya liste belleğine ihtiyaç duymazsın $\rightarrow$ **$O(1)$ Space**.

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Space Complexity = O(1)
        ans = 0
        count = 0
        
        # Time Complexity = O(N)
        for num in nums:
            if count == 0:
                ans = num
                
            if ans == num:
                count += 1
            else:
                count -= 1
                
        return ans
```

**Time Complexity (Zaman Karmaşıklığı):** `O(N)`
Diziyi sadece bir kez baştan sona tararız.

**Space Complexity (Alan Karmaşıklığı):** `O(1)`
Yukarıda açıklandığı gibi ekstra hafıza (dizi, sözlük vb.) tüketilmez.

--- 

### 2. Hash Map Yaklaşımı (Alternatif)

Diziyi gezerek her bir elemanın kaç kere tekrar ettiğini bir sözlüğe (Hash Map) kaydederiz. Sözlük dolduktan sonra değerleri kontrol ederiz ve tekrar sayısı `len(nums) / 2`'den büyük olan ilk anahtarı (sayıyı) döndürürüz.

```python
class SolutionHashMap:
    def majorityElement(self, nums: list[int]) -> int:
        # Space Complexity = O(N)
        d = {}
        
        # Time Complexity = O(N)
        for i in nums:
            if i not in d:
                d[i] = 1
            elif i in d:
                d[i] += 1
                
        for i in d:
            if d[i] > (len(nums) / 2):
                return i
```

**Time Complexity (Zaman Karmaşıklığı):** `O(N)`
Sözlüğü doldurmak ve sonrasında içinde arama yapmak `O(N)` sürer.

**Space Complexity (Alan Karmaşıklığı):** `O(N)`
En kötü senaryoda dizideki elemanların frekanslarını tutmak için hafızada `O(N)` boyutunda bir sözlük oluşturulur.

---

### 3. Sorting Yaklaşımı (Brute Force)

Çoğunluk elemanı dizinin yarısından fazlasını kapladığı için, diziyi küçükten büyüğe sıraladığımızda, bu eleman her halükarda dizinin tam ortasındaki `n // 2` indeksine yerleşmek zorundadır. Kodlaması çok kısadır ancak sıralama işlemi yüzünden yavaştır.

```python
class SolutionSorting:
    def majorityElement(self, nums: list[int]) -> int:
        # Space Complexity = O(1) veya O(N)
        # Time Complexity = O(N log N)
        nums.sort()
        return nums[len(nums) // 2]
```

**Time Complexity (Zaman Karmaşıklığı):** `O(N log N)`
Sıralama algoritmasının maliyetidir.

**Space Complexity (Alan Karmaşıklığı):** `O(1)` veya `O(N)`
Dile bağlı olarak sıralama işleminin arka planda kullandığı hafızaya göre değişir.