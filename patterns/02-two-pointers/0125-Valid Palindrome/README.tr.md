> 💡 **Not:** Bu soru **Two Pointers** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example 1:
**Input:** `s = "A man, a plan, a canal: Panama"`  
**Output:** `true`  
**Explanation:** "amanaplanacanalpanama" is a palindrome.  

### Example 2:
**Input:** `s = "race a car"`  
**Output:** `false`  
**Explanation:** "raceacar" is not a palindrome.  

---

### Türkçe Açıklama

Sana bir `s` metni veriliyor. Metindeki tüm harfleri küçük harfe çevirip, harf ve rakam olmayan (boşluk, noktalama işareti vb.) tüm karakterleri sildiğinde, metin tersten de aynı okunuyorsa (palindrom ise) `true`, aksi halde `false` döndürmen isteniyor.

---

### 1. In-Place Two Pointers Yaklaşımı (Optimal)

* En yüksek performansı elde etmek için yeni bir dizi veya metin oluşturmadan, **Two Pointers** tekniğini doğrudan orijinal metin üzerinde uygulayabiliriz.
* `left` pointer'ını en başa, `right` pointer'ını en sona yerleştiririz.
* Sadece harfler ve rakamlarla (alphanumeric) ilgileniyoruz. Eğer `s[left]` boşluk veya noktalama işaretiyse (`not s[left].isalnum()`), pointer'ı bir adım kaydırır (`left += 1`) ve **`continue`** komutunu kullanırız.
* **`continue` ne işe yarar?:** Döngünün o anki adımını anında kesip `while` döngüsünün en başına dönmesini sağlar. Bu sayede, pointer geçerli bir karakter bulana kadar döngü aşağıdaki karşılaştırma koduna inmeden kendini tekrar eder. Aynı mantık `right` pointer'ı için de geçerlidir.
* **Neden Optimal?:** Geçersiz karakterleri anlık olarak atladığımız için, geçerli harfleri doğrudan birbirleriyle kıyaslarız. Harfleri ayıklayıp bir yerde depolamaya (yeni bir liste oluşturmaya) gerek kalmaz. Bu sayede alternatif çözümdeki `O(N)` alan karmaşıklığı yerine, harika bir `O(1)` alan karmaşıklığı elde ederiz.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
                
            if not s[right].isalnum():
                right -= 1
                continue
                
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
```

**Time Complexity:** `O(N)`

Her bir karakter maksimum bir kez kontrol edilir.

**Space Complexity:** `O(1)`

Sadece iki adet tam sayı pointer'ı kullanıldığı için ekstra belleğe ihtiyaç duyulmaz.

--- 

### 2. Diziyi Filtreleme & Two Pointers Yaklaşımı (Alternatif)

* Karakterleri anlık olarak atlamak yerine, önce tüm metni gezip sadece harf ve rakamları (küçük harfe çevirerek) `nonalpha` adında yeni bir listeye ekleyebiliriz. 
* Ardından temizlenmiş bu liste üzerinde standart Two Pointers mantığını uygularız. 
* Anlaması ve kurgulaması daha kolay olsa da, geçerli karakterleri depoladığımız için `O(N)` oranında ekstra hafıza feda etmiş oluruz.

```python
class SolutionAlternative:
    def isPalindrome(self, s: str) -> bool:
        nonalpha = []
        
        for i in range(len(s)):
            if s[i].isalnum():
                nonalpha.append(s[i].lower())
                
        left = 0
        right = len(nonalpha) - 1
        
        while left < right:
            if nonalpha[left] != nonalpha[right]:
                return False
            left += 1
            right -= 1
            
        return True
```

**Time Complexity:** `O(N)`

Filtreleme işlemi ve palindrom kontrolü toplamda `O(N)` sürer.

**Space Complexity:** `O(N)`

`nonalpha` listesi orijinal metin kadar yer kaplayabilir.

---

### 3. Built-in Reverse Yaklaşımı (Brute Force)

* Metni temizleyip yeni bir listeye alırız ve bu listeyi Python'un dilimleme (slicing `[::-1]`) özelliğiyle ters çevrilmiş haliyle direkt kıyaslarız.

```python
class SolutionBruteForce:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]
```

**Time Complexity:** `O(N)`

Liste oluşturma ve ters çevirme işlemleri lineer zaman alır.

**Space Complexity:** `O(N)`

Temizlenmiş liste ve ters çevrilmiş kopyası için fazladan yer ayrılır.