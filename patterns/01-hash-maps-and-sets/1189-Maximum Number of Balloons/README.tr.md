> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)


Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.
You can use each character in `text` at most once. Return the maximum number of instances that can be formed.

### Example 1:
> **Input:** `text = "nlaebolko"`  
> **Output:** `1`

### Example 2:
> **Input:** `text = "loonbalxballpoon"`  
> **Output:** `2`

### Example 3:
> **Input:** `text = "leetcode"`  
> **Output:** `0`

---

### Türkçe Açıklama
Sana `text` adında bir metin (string) veriliyor. Amacın, bu metindeki karakterleri kullanarak oluşturabileceğin maksimum **"balloon"** kelimesi sayısını bulmaktır. Metindeki her bir karakteri en fazla bir kez kullanabilirsin. Kaç tane "balloon" kelimesi oluşturulabileceğini döndürmen isteniyor.

> **Not:** Hash table kalıbı, string içindeki harflerin frekansını (kaç kere geçtiklerini) sayıp bir sözlüğe atmak ve sonrasında `O(1)` sürede arama/kontrol yapmak için idealdir.

---

### 1. Hash Map (Frekans Sayımı) - Optimal Çözüm

"balloon" kelimesini oluşturmak için belirli miktarda harflere ihtiyacımız var: Bir 'b', bir 'a', iki 'l', iki 'o' ve bir 'n'. Verilen `text` metnindeki tüm karakterlerin frekanslarını bir Sözlük (Hash Map) kullanarak sayabiliriz.

Oluşturabileceğimiz kelime sayısı, elimizdeki harflerden **en az (yetersiz)** olana göre belirlenir (buna darboğaz diyoruz). "balloon" kelimesinde 'l' ve 'o' harflerinden ikişer tane kullanıldığı için, bu harflerin toplam sayısını 2'ye bölerek potansiyellerini hesaplarız. Son olarak, tüm bu gerekli harflerin eldeki miktarları arasından en küçüğünü alarak sonucu buluruz.

**Kodun Detaylı Açıklaması:**
* **Neden `.get()` kullanıyoruz?** Normalde sözlükte olmayan bir harfi (örneğin 'b') `letters['b']` olarak çağırsaydık, Python o harf sözlükte olmadığı için `KeyError` hatası verip programı çökertecekti. `.get('b', 0)` fonksiyonu şunu söyler: *"Sözlükte 'b' harfini ara, eğer bulamazsan hata verme, onun yerine bana `0` değerini döndür."*
* **Neden `min()` kullanıyoruz?** Bir kelimeyi üretmek bir kek tarifi gibidir. Elinde 100 tane 'b' ve 'a' olsa bile, sadece 1 tane 'n' harfin varsa en fazla 1 tane "balloon" yazabilirsin. `min()` fonksiyonu, elindeki gerekli malzemeler arasından miktarı **en az** olanı bulur ve maksimum üretim kapasiteni belirler.
* **Neden `// 2` yapıyoruz?** "balloon" kelimesinde 2 adet 'l' ve 2 adet 'o' vardır. Yani elinde 5 tane 'l' varsa bundan ancak $5 // 2 = 2$ tane balon çıkar. Tam sayı bölmesi (`//`) kullanarak küsuratları atıp gerçek kapasiteyi buluyoruz.

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        
        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
                
        return min(
            letters.get('b', 0),
            letters.get('a', 0),
            letters.get('l', 0) // 2, 
            letters.get('o', 0) // 2, 
            letters.get('n', 0)
        )
```

**Zaman Karmaşıklığı:** `O(n)`

`n` uzunluğundaki `text` metnini sadece bir kez gezeriz. Sözlüğe yazma, sözlükten okuma ve `min()` işlemi `O(1)` sürer.

**Alan Karmaşıklığı:** `O(1)`

Hash map içerisinde sadece İngilizce küçük harfler tutulur (maksimum 26 karakter). Girdi olan metnin uzunluğu ne kadar artarsa artsın, hafızada kaplanan alan 26 karakteri geçemeyeceği için sabit kalır.