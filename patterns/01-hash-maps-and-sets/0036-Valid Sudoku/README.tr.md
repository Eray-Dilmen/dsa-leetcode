> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [README.md](../README.md) dosyasına bakabilirsiniz.

# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)


Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated according to the mentioned rules.

### Example 1:
> **Input:** board = 
> [["5","3",".",".","7",".",".",".","."]
> ,["6",".",".","1","9","5",".",".","."]
> ,[".","9","8",".",".",".",".","6","."]
> ,["8",".",".",".","6",".",".",".","3"]
> ,["4",".",".","8",".","3",".",".","1"]
> ,["7",".",".",".","2",".",".",".","6"]
> ,[".","6",".",".",".",".","2","8","."]
> ,[".",".",".","4","1","9",".",".","5"]
> ,[".",".",".",".","8",".",".","7","9"]]
>  
> **Output:** `true`  

### Example 2:
> **Input:** board = 
> [["8","3",".",".","7",".",".",".","."]
> ,["6",".",".","1","9","5",".",".","."]
> ,[".","9","8",".",".",".",".","6","."]
> ,["8",".",".",".","6",".",".",".","3"]
> ,["4",".",".","8",".","3",".",".","1"]
> ,["7",".",".",".","2",".",".",".","6"]
> ,[".","6",".",".",".",".","2","8","."]
> ,[".",".",".","4","1","9",".",".","5"]
> ,[".",".",".",".","8",".",".","7","9"]]
>  
> **Output:** `false`  

---

### Türkçe Açıklama
Sana `9x9` boyutlarında bir Sudoku tahtası veriliyor. Tahtanın şu anki halinin geçerli (kurallara uygun) olup olmadığını bulman isteniyor.
Geçerlilik kuralları:
1. Her satırda `1-9` arası rakamlar tekrar etmeden bulunmalıdır.
2. Her sütunda `1-9` arası rakamlar tekrar etmeden bulunmalıdır.
3. Tahtayı oluşturan 9 adet `3x3`'lük alt kutunun her birinde `1-9` arası rakamlar tekrar etmeden bulunmalıdır.
*Sadece dolu hücreleri kontrol etmen yeterlidir, tahtanın çözülebilir olup olmadığı önemli değildir.*

> ⚠️ **Kritik Performans Notu: `list` vs `set` Kullanımı**
> 
> * `x in list` $\rightarrow O(n)$: Liste sıralı bir dizi yapısındadır. Python, elemanı bulana kadar baştan sona tek tek bakar (linear search). Eleman sonda veya listede yoksa tüm elemanları gezer.
> * `x in set` $\rightarrow O(1)$: `set`, arkasında **hash tablosu (hash table)** kullanır. Aranan elemanın hash değeri doğrudan hesaplanır ve tablodaki konuma tek adımda (ortalama durumda) bakılır.

---

### 1. Hash Set Yaklaşımı (Optimal)

Tahtayı doğrulamak için üç ayrı tarama yapıyoruz: Satırlar, sütunlar ve 3x3 kutular için. Tekrarlanan bir sayı olup olmadığını hızlıca anlamak için Hash Set kullanıyoruz. Bir elemanın küme içinde olup olmadığını sorgulamak `O(1)` sürdüğü için bu yöntem çok verimlidir.

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row validation (Satır Doğrulaması)
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # column validation (Sütun Doğrulaması)
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
                    
        # box validation (3x3 Kutu Doğrulaması)
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]

        for i,j in starts:
            s = set()
            for row in range(i,i+3):
                for column in range(j,j+3):
                    item = board[row][column]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
```

**Time Complexity (Zaman Karmaşıklığı):** `O(1)`
Sudoku tahtasının boyutu `9x9` olarak sabit olduğu için, tahtayı gezmek her döngüde maksimum `81` adım sürer. Set üzerinde arama yapmak da `O(1)` olduğu için çalışma süresi sabittir (Constant Time).

**Space Complexity (Alan Karmaşıklığı):** `O(1)`
Her bir Set içerisine maksimum 9 eleman alabilir. Girdi boyutu değişmediği için kullanılan ekstra hafıza da sabittir.

--- 

### 2. List Lookup Yaklaşımı (Verimsiz / Brute Force)

Görülen elemanları takip etmek için `set` yerine bir liste (`list`) kullanırsak, `if item in l` kodunu çalıştırdığımızda algoritma `O(n)` süren yavaş bir doğrusal arama (linear search) yapar. Tahta 9x9 gibi küçük bir boyutta olduğu için burada gözle görülür bir fark yaratmasa da, büyük veri setlerinde liste kullanmak ciddi performans sorunlarına yol açar.

```python
class SolutionBruteForce:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            l = []
            for j in range(9):
                item = board[i][j]
                # Liste içinde arama yapmak O(n) sürer
                if item in l:
                    return False
                elif item != '.':
                    l.append(item)
                    
        # (Aynı liste mantığının sütun ve kutular için de uygulandığını varsayıyoruz)
        return True
```

**Time Complexity (Zaman Karmaşıklığı):** `O(1)`
Matematiksel olarak tahta boyutu sabit olduğu için zaman karmaşıklığı sabittir, ancak `O(n)` arama mantığı sebebiyle Set yaklaşımına kıyasla daha yavaş çalışır.

**Space Complexity (Alan Karmaşıklığı):** `O(1)`
Listeler de 9'dan fazla eleman tutmayacağı için harcanan alan sabittir.