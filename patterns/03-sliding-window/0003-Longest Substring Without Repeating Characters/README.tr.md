💡 **Not:** Bu soru **Sliding Window** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string `s`, find the length of the longest substring without duplicate characters.

### Example 1:
> **Input:** `s = "abcabcbb"`  
> **Output:** `3`  
> **Explanation:** The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

### Example 2:
> **Input:** `s = "bbbbb"`  
> **Output:** `1`  
> **Explanation:** The answer is "b", with the length of 1.

### Example 3:
> **Input:** `s = "pwwkew"`  
> **Output:** `3`  
> **Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

### Türkçe Açıklama

Sana bir `s` stringi (metin dizgesi) veriliyor. Senden istenen, içinde hiçbir karakterin tekrar etmediği **en uzun alt dizgenin (substring)** uzunluğunu bulmandır. (Alt dizge, metnin içinde kesintisiz olarak devam eden bir parçadır.)

---

### 1. Sliding Window ve Set Yaklaşımı (Optimal)

* Soruyu çözmek için, içinde tekrar eden harf bulunmayan bir Sliding Window oluşturuyoruz. Bu pencereyi `l` ve `r` pointer'larıyla kontrol ederken, pencerenin içindeki harfleri bir `Set` veri yapısında tutuyoruz.
* `r` pointer'ı ile metni harf harf tarayarak penceremizi genişletiyoruz. Eğer karşılaştığımız harf zaten `Set` içinde varsa (yani tekrar ediyorsa), pencere geçerliliğini yitirir. 
* Bu durumu düzeltmek için, tekrar eden harfi pencereden çıkarana kadar `l` pointer'ını sağa doğru kaydırırız ve çıkardığımız harfleri `Set` üzerinden de sileriz. 
* Pencere tekrar benzersiz (unique) karakterlerden oluştuğunda, yeni harfi `Set`'e ekleriz ve o ana kadarki en uzun pencere boyutunu güncelleriz.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = r - l + 1
            longest = max(longest, w)
            sett.add(s[r])
            
        return longest
```

**Time Complexity:** `O(N)`

Sağ pointer (`r`) ve sol pointer (`l`) metni en fazla birer kez tarar. Bu yüzden zaman karmaşıklığı lineerdir.

**Space Complexity:** `O(min(M, N))`

`Set` veri yapısı, mevcut penceredeki benzersiz karakterleri tutar. Kullanılan alan, stringin uzunluğu (`N`) ve karakter setinin boyutu (`M`) ile sınırlıdır.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force)

* Metindeki tüm olası başlangıç noktalarından yola çıkarak iç içe döngülerle her bir alt dizgeyi kontrol edebiliriz. 
* Bir alt dizgeyi oluştururken karakterleri bir `Set` içinde biriktiririz. 
* Eğer o alt dizge içinde daha önce eklediğimiz bir harfe denk gelirsek, o noktadan sonrasını kontrol etmeyi bırakırız (çünkü artık tekrar eden bir harf vardır) ve bir sonraki başlangıç indeksine geçeriz. Bu yöntem `O(N^2)` zaman alır ve büyük girdilerde çok yavaştır.

```python
class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)
                
        return max_len
```

**Time Complexity:** `O(N^2)`

İç içe döngülerle tüm olası alt dizgeleri taramak, karesel zaman karmaşıklığı yaratır.

**Space Complexity:** `O(min(M, N))`

Her bir alt dizgeyi oluştururken kullanılan `Set` nedeniyle ayrılan ekstra hafızadır.