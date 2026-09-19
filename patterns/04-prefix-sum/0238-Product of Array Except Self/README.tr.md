> 💡 **Not:** Bu soru **Prefix Sum** (Kümülatif Toplam/Çarpım) kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(N)` time and without using the division operation.

### Example 1:
> **Input:** `nums = [1,2,3,4]`  
> **Output:** `[24,12,8,6]`  

### Example 2:
> **Input:** `nums = [-1,1,0,-3,3]`  
> **Output:** `[0,0,9,0,0]`  

---

### Türkçe Açıklama

Sana `nums` adında bir tam sayı dizisi veriliyor. Senden istenen, dizideki her bir eleman için, **kendisi hariç** dizideki diğer tüm elemanların çarpımını bularak yeni bir `answer` dizisi döndürmendir. Bölme işlemi (`/`) kullanman yasaktır ve algoritman `O(N)` zaman karmaşıklığında çalışmalıdır.

---

### 1. Prefix ve Suffix Çarpımları Yaklaşımı (Optimal)

Bölme işlemi kullanmadan bir eleman hariç diğerlerinin çarpımını bulmak için, o elemanın **solunda kalan tüm sayıların çarpımı** ile **sağında kalan tüm sayıların çarpımını** birbiriyle çarpmamız gerekir. 

**Profesyonel Mantık ve Kodun Okuması:**
* İlk `for` döngüsünde diziyi baştan sona gezerek, her bir elemanın solunda kalan sayıların kümülatif çarpımını hesaplıyoruz ve bunu doğrudan `ans` dizisine kaydediyoruz. (Yani en başta soldan çarpımları aldık ve depoladık).
* Ondan sonraki (tersten çalışan) ikinci `for` döngüsünde ise sağdan çarpımları (`rightProduct`) hesaplayarak ilerliyoruz ve bu değeri, `ans` dizisindeki mevcut değerle (soldaki sonuç ile) çarpıyoruz, değil mi?
* **Neden mi böyle yapıyoruz?** Çünkü `ans` dizisindeki o değer, zaten şimdiye kadar soldakilerin çarpılmış haliydi! Sol çarpım ile anlık olarak hesapladığımız sağ çarpımı birleştirdiğimizde, o eleman hariç dizinin geri kalanının eksiksiz çarpımını ekstra bir hafıza (yeni bir dizi) kullanmadan mükemmel bir şekilde elde etmiş oluyoruz.

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
            
        rightProduct = 1
        
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= rightProduct
            rightProduct *= nums[i]
            
        return ans
```

**Time Complexity:** `O(N)`

Diziyi sadece bir kez baştan sona, bir kez de sondan başa tarıyoruz. Toplam işlem süresi dizinin boyutuyla doğrudan orantılı olduğu için lineerdir.

**Space Complexity:** `O(1)`

Sorunun açıklamasında sonuçları döndürdüğümüz `ans` dizisinin ekstra alan (space complexity) hesabına katılmayacağı özellikle belirtilmiştir. Bunun dışında sadece `rightProduct` adında tek bir değişken kullandığımız için ekstra alan karmaşıklığımız sabittir.

--- 

### 2. İç İçe Döngüler Yaklaşımı (Brute Force 1 - Time Limit Exceeded)

En temel düz mantık çözümdür. Dışarıdaki döngü ile her bir `i` elemanını seçeriz, içerideki döngü ile tüm diziyi baştan sona tekrar tararız. İçerideki döngü sayacı `j`, dışarıdaki `i`'ye eşit olduğunda (`j == i`) sayıyı atlar (`continue`), geri kalan tüm sayıları birbiriyle çarparız.

```python
class SolutionBruteForce1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            summ = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                summ *= nums[j]
                
            ans[i] = summ
            
        return ans
```

**Time Complexity:** `O(N^2)`

Her bir eleman için tüm dizi tekrar tarandığı için karesel bir zaman karmaşıklığı oluşur. Büyük dizilerde Time Limit Exceeded (Zaman Aşımı) hatası verir.

**Space Complexity:** `O(1)`

Sadece çarpımları tutan basit bir değişken kullanılmıştır.

---

### 3. Çift Yönlü While Döngüsü (Brute Force 2 - Time Limit Exceeded)

Bu yaklaşımda, optiomal çözümün mantığına (sol ve sağ çarpımlar) biraz daha yaklaşılır ancak hala verimsizdir. Her bir `i` elemanı için iki ayrı `while` döngüsü kurulur. İlk döngü 0'dan `i`'ye kadar olan sol kısmı çarpar, ikinci döngü ise dizinin sonundan `i`'ye kadar olan sağ kısmı çarpar. 

Sorun şudur ki; kümülatif toplam mantığı (Prefix Sum) kullanılmadığı için, her bir indeks adımında sol ve sağ çarpımlar geçmişten faydalanılmadan sıfırdan tekrar hesaplanır.

```python
class SolutionBruteForce2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            prefix = 0
            summ = 1
            suffix = len(nums) - 1
            
            while prefix < i:
                summ *= nums[prefix]
                prefix += 1
                
            while suffix > i:
                summ *= nums[suffix]
                suffix -= 1
                
            ans[i] = summ
            
        return ans
```

**Time Complexity:** `O(N^2)`

Döngüler ikiye bölünmüş olsa da, her bir `i` için toplamda yine `N-1` adet işlem yapılır. Bu yüzden genel karmaşıklık `O(N^2)` kalır.

**Space Complexity:** `O(1)`

Takip için kullanılan birkaç index değişkeni dışında ekstra hafıza harcanmaz.