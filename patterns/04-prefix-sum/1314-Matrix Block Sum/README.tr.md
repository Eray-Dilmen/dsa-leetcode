> 💡 **Not:** Bu soru **2D Prefix Sum** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [1314. Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/)

`m x n` boyutlarında bir `mat` matrisi ve bir `k` tam sayısı veriliyor. Her bir `answer[i][j]` hücresinin, aşağıdaki koşulları sağlayan tüm `mat[r][c]` elemanlarının toplamına eşit olduğu bir `answer` matrisi döndürmeniz isteniyor:
* $i - k \le r \le i + k$
* $j - k \le c \le j + k$
* $(r, c)$ matris içinde geçerli bir konumdur.

### Example 1:
> **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
> **Output:** `[[12,21,16],[27,45,33],[24,39,28]]`

### Example 2:
> **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2`
> **Output:** `[[45,45,45],[45,45,45],[45,45,45]]`

---

### Türkçe Açıklama ve Detaylı Mantık

"Matrix Block Sum" probleminde, toplanacak alt matrisin sınırları, seçilen merkez elemandan `k` birim mesafeye kadar uzanır[cite: 38]. 

**Boyut Neden $2k + 1$'dir?**
Sorunun kuralı gereği toplanacak elemanların indisleri ($r, c$) $i - k \le r \le i + k$ ve $j - k \le c \le j + k$ formülü ile tanımlanır[cite: 39]. Bu durum, merkezin $k$ birim yukarısı ile $k$ birim aşağısını kapsar[cite: 39]. Yani satır sayısı; merkez elemanın üstünde $k$ satır, altında $k$ satır ve merkez satırın kendisi (1) olmak üzere toplam $k + k + 1 = 2k + 1$ formülüyle hesaplanır[cite: 38]. Sütun sayısı da benzer şekilde sağda $k$, solda $k$ ve merkez sütunun kendisi (1) olmak üzere $2k + 1$ adettir[cite: 38]. Örneğin $k = 1$ seçildiği için hesaplanacak maksimum blok boyutu her yöne 1 birim genişleyerek $3 \times 3$ olarak hesaplanır[cite: 39]. Eğer $k = 2$ verilseydi, kural gereği sağa-sola ve yukarı-aşağı 2'şer birim uzanacaktı[cite: 39].

**Neden `m + 1` ve `n + 1` Boyutunda Prefix Sum Matrisi Kullanıyoruz? (Out of Bounds Sorunu)**
Prefix sum dizisi oluştururken, formülde bulunduğun hücrenin üstüne ($i - 1$) ve soluna ($j - 1$) bakman gerekiyor[cite: 40]. İndekslerin 0'dan başlaması asıl sorundur[cite: 40]. İlk satır veya ilk sütundaki (0. indeks) değerler için $0 - 1 = -1$ işlemi yapıldığında indeks dışına (out of bounds) düşülür[cite: 40]. Matrisi başından 1 birim 0'larla doldurmak (padding), bu indeks hatasını temiz ve hatasız bir şekilde önler.

---

### 1. 2D Prefix Sum Yaklaşımı (Optimal)

* Her hücre için `(2k+1) x (2k+1)` boyutundaki bloğu baştan toplamak yerine **2D Prefix Sum** (İki Boyutlu Kümülatif Toplam) matrisi oluştururuz.
* `prefix` matrisini hazırladıktan sonra, herhangi bir sol üst `(r1, c1)` ve sağ alt `(r2, c2)` noktaları arasında kalan dikdörtgenin toplamını kümeler teorisine (Inclusion-Exclusion Principle) dayanarak `O(1)` sürede şu formülle çekeriz:
  `Alan = Prefix[r2][c2] - Prefix[r1-1][c2] - Prefix[r2][c1-1] + Prefix[r1-1][c1-1]`

```python
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
                
        answer = [[0] * n for _ in range(m)]
          
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)
                
                r1 += 1
                c1 += 1
                r2 += 1
                c2 += 1
                
                answer[i][j] = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
                
        return answer
```

**Time Complexity:** `O(m * n)`

Prefix sum matrisini oluşturmak `O(m * n)` zaman alır. Daha sonra cevap matrisindeki her bir hücreyi hesaplamak için prefix matrisinden $O(1)$ sürede veri çekeriz. Bu nedenle toplam süre matrisin boyutuyla doğru orantılıdır (lineer).

**Space Complexity:** `O(m * n)`

Ara hesaplamaları saklamak için `(m+1) x (n+1)` boyutunda bir `prefix` matrisi ve sonuçları döndürmek için `m x n` boyutunda bir `answer` matrisi ayrılır.

--- 

### 2. İç İçe Döngülerle Kutu Tarama (Brute Force)

* Matristeki her bir `(i, j)` hücresi için, sınır değerleri (`r1, r2, c1, c2`) hesaplarız.
* İç içe iki döngü daha açarak bu sınırlar içinde kalan her bir hücreyi tek tek toplarız. Kesişen alanlar tekrar tekrar hesaplandığı için oldukça yavaş bir yöntemdir[cite: 37].

```python
class SolutionBruteForce:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        answer = []

        for i in range(m):
            row = []
            for j in range(n):
                r1, r2 = max(0, i - k), min(m - 1, i + k)
                c1, c2 = max(0, j - k), min(n - 1, j + k)
                
                total = 0
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        total += mat[r][c]
                
                row.append(total)
            answer.append(row)
            
        return answer
```

**Time Complexity:** `O(m * n * k^2)`

`m * n` adet hücrenin her biri için, maksimum `(2k+1) x (2k+1)` boyutunda bir alanı tek tek taradığımız için `k` değerine bağlı olarak performans dramatik şekilde düşer.

**Space Complexity:** `O(m * n)`

Sonuçları tutmak için ayırdığımız `answer` matrisi bellekte yer kaplar.