> 💡 **Not:** Bu soru **Sliding Window** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Example 1:
> **Input:** `s = "ABAB", k = 2`
> **Output:** `4`
> **Explanation:** Replace the two 'A's with two 'B's or vice versa.

### Example 2:
> **Input:** `s = "AABABBA", k = 1`
> **Output:** `4`
> **Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
> The substring "BBBB" has the longest repeating letters, which is 4.
> There may exists other ways to achieve this answer too.

---

### Türkçe Açıklama

Sana sadece büyük İngilizce harflerden oluşan bir `s` metni ve `k` tam sayısı veriliyor. En fazla `k` adet harfi başka bir harfe değiştirme hakkın var. Senden istenen, bu değiştirme işlemini yaparak elde edebileceğin, tamamen aynı harflerden oluşan en uzun alt dizgenin (substring) uzunluğunu bulmandır.

---

### 1. Frekans Haritası ile Sliding Window Yaklaşımı (Optimal)

* Bu soruyu çözerken `l` (sol) ve `r` (sağ) pointer'larıyla bir Sliding Window oluşturuyoruz. 
* Pencerenin içindeki karakterlerin frekansını (hangi harften kaç tane olduğunu) bir Sözlük (`count`) yardımıyla tutuyoruz. Ayrıca penceredeki en çok tekrar eden harfin sayısını da `max_freq` değişkeninde saklıyoruz.
* Sağ pointer `r` ile metni tararken şu mantığı kuruyoruz: Mevcut pencerenin uzunluğundan, penceredeki en sık geçen harfin sayısını çıkarırsak, "değiştirmemiz gereken harf sayısını" buluruz `(r - l + 1) - max_freq`. 
* Eğer bu değiştirmemiz gereken harf sayısı bize verilen `k` hakkını aşarsa, mevcut penceremiz geçersiz demektir. 
* Bu durumda pencereyi geçerli hale getirmek için sol pointer'ı (`l`) bir adım sağa kaydırarak pencereyi sol taraftan daraltırız. Her geçerli pencere adımında ise en uzun boyutu (`longest`) güncelleriz.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = {}
        max_freq = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            longest = max(longest, (r - l + 1))
            
        return longest
```

**Time Complexity:** `O(N)`

Sağ ve sol pointer'lar diziyi en fazla birer kez tarar. Bu yüzden zaman karmaşıklığı lineerdir.

**Space Complexity:** `O(1)`

Sözlük (Hash Map) en fazla 26 büyük İngilizce harfi tutacağı için kullanılan alan `O(26)` yani `O(1)` (sabit) kabul edilir.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force)

* Metindeki her bir indexten başlayan tüm alt dizgeleri iç içe iki döngü ile tek tek kontrol edebiliriz. 
* Her alt dizge için karakterlerin frekansını hesaplar, en sık geçen karakteri buluruz. 
* Eğer "alt dizgenin boyutu - en sık geçen karakterin sayısı" değeri `k`'ya eşit veya ondan küçükse, bu alt dizge bizim için geçerlidir. 
* `k` sınırını aşan bir duruma geldiğimizde ise o alt dizgeyi daha fazla uzatmadan durdurup (`break`), bir sonraki başlangıç elemanına geçeriz.

```python
class SolutionBruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)
        
        for i in range(n):
            count = {}
            max_freq = 0
            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                
                if (j - i + 1) - max_freq <= k:
                    longest = max(longest, j - i + 1)
                else:
                    break
                    
        return longest
```

**Time Complexity:** `O(N^2)`

İç içe döngülerle tüm olası alt dizgeleri taramak, karesel zaman karmaşıklığı yaratır.

**Space Complexity:** `O(1)`

Her alt dizge için oluşturulan Sözlük boyutu 26 karakterle sınırlı olduğu için ekstra alan sabit kalır.