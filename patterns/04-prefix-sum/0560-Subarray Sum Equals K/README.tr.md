> 💡 **Not:** Bu soru **Prefix Sum (Kümülatif Toplam)** ve **Hash Map (Sözlük)** veri yapısı birleştirilerek çözülmüştür. Kalıbın genel mantığı ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

### Example 1:
> **Input:** `nums = [1,1,1]`, `k = 2`  
> **Output:** `2`  

### Example 2:
> **Input:** `nums = [1,2,3]`, `k = 3`  
> **Output:** `2`  

---

### Türkçe Açıklama

Sana `nums` adında bir tam sayı dizisi ve `k` adında bir hedef toplam veriliyor. Senden istenen, dizinin içinde elemanlarının toplamı tam olarak `k`'ya eşit olan alt dizgelerin (subarrays) toplam sayısını bulmandır.

---

### 1. Prefix Sum + Hash Map Yaklaşımı (Optimal)

Tüm alt dizileri iç içe döngülerle baştan hesaplamak yerine, dizide ilerledikçe kümülatif bir toplam (`prefix_sum`) tutarız. Bu esnada karşılaştığımız her bir kümülatif toplamın geçmişte **kaç kez** oluştuğunu bir Sözlük (`freq`) içinde kaydederiz. 

**Olayın Mantığı ve Kodun Okuması:**

* **1. Matematiksel Mantık:**
Diyelim ki bir noktaya kadar geldin ve elindeki kümülatif toplam `prefix_sum`. Senin aradığın şey ise toplamı `k` olan bir alt dizi. Denklem şu:
`Şu anki Toplam - Geçmişteki Bir Toplam = k`
Buradan geçmişi çekersek: `Geçmişteki Toplam = prefix_sum - k`.
Yani Hash Map'te `prefix_sum - k` değerini aramak, *"Aradaki farkı tam olarak k yapan bir başlangıç noktası var mı?"* sorusunun doğrudan kontrolüdür. Parçayı baştan toplayıp kontrol etmene gerek kalmaz.

* **2. Neden `freq = {0: 1}` ile Başlıyor? (En Çok Karışan Kısım):**
Diyelim ki `k = 3` ve dizinin ilk elemanı tek başına `3`. Kümülatif toplam `3` olur. Formülü uygularsın: `3 - 3 = 0`. Kod geçmişe döner ve bakar: *"Daha önce toplamın 0 olduğu bir durum var mıydı?"* Eğer sözlüğe en başta `{0: 1}` koymazsan, en baştan (0. indeksten) başlayan geçerli alt dizileri çöpe atmış olursun. Kısacası bu, *"Henüz hiçbir eleman seçilmemişken toplam 0'dır ve bu durum 1 kez gerçekleşmiştir"* taban durumudur (base case).

* **3. Neden 1 Değil de Map'teki Frekans Kadar (`freq[...]`) Ekliyoruz? (Kesip Atma Mantığı):**
`prefix_sum - k` değeri bizim bulduğumuz alt dizi **değildir**; o kısım bıçakla **kesip çöpe attığımız** (çıkardığımız) kısımdır. Başlangıçtan aradaki bir yere kadar olan bu kısmı çöpe atarsan, geriye tam olarak `k` kalır. Dizide `0` veya negatif sayılar olabileceği için, kümülatif toplam dalgalanabilir ve çöpe atacağımız o "Geçmişteki Toplam" değeri geçmişte 2 veya 3 kere oluşmuş olabilir. Geçmişte o kesim noktasından kaç tane varsa, bıçağı vurup baştan atabileceğin o kadar farklı nokta vardır ve her biri sana şu an bulunduğun yerde biten ayrı bir alt dizi verir. Bu yüzden `count += 1` demek yerine o geçmiş toplamın frekansını ekleriz.

```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]
                
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
            
        return count
```

**Time Complexity:** `O(N)`

Diziyi yalnızca bir kez tarıyoruz. Sözlük (Hash Map) içi arama ve ekleme işlemleri ortalama olarak sabit zamanlı `O(1)` olduğu için, genel karmaşıklık lineerdir.

**Space Complexity:** `O(N)`

Kötü senaryoda (örneğin dizideki tüm sayılar pozitifse) her bir kümülatif toplam birbirinden farklı olur. Bu durumda sözlükte `N` adet farklı anahtar-değer çifti depolanır.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force - Time Limit Exceeded)

Tüm olası alt dizileri başlangıç noktasına göre iç içe iki döngü ile tarayabiliriz. Dış döngü `l` alt dizinin başlangıcını belirler, iç döngü `r` ise bu diziyi sağa doğru genişleterek anlık toplamı (`summ`) tutar. Toplam `k`'ya eşit olduğunda sayacı artırırız.

Mantıken kusursuz çalışsa da, tüm olası kombinasyonları denediği için büyük boyutlu dizilerde LeetCode üzerinde **Time Limit Exceeded (TLE)** (Zaman Aşımı) hatası verir.

```python
class SolutionBruteForce:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for l in range(len(nums)):
            summ = 0
            for r in range(l, len(nums)):
                summ += nums[r]
                if summ == k:
                    count += 1
        return count
```

**Time Complexity:** `O(N^2)`

İç içe döngüler dizinin boyutuna bağlı olarak karesel bir büyüme yaratır.

**Space Complexity:** `O(1)`

Sadece anlık değerleri tutan değişkenler kullanılır, ekstra bir veri yapısına ihtiyaç duyulmaz.