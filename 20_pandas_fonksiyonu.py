# -*- coding: utf-8 -*-
"""20-Pandas-Fonksiyonu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sbnLLCsegI9E0sVAjvRXiR38qbm3el3j

# **Veri Bilimi Projenizin %80 nine Yeticek 20 Pandas Fonksiyonu**

Pandas, veri bilimi topluluğunda en yaygın kullanılan kitaplıklardan biridir ve veri işleme, temizleme ve analiz konularında size yardımcı olabilecek güçlü bir araçtır. İster yeni başlayan ister deneyimli bir veri bilimcisi olun, bu makale en sık kullanılan Pandas işlevleri ve bunların pratik olarak nasıl kullanılacağı hakkında değerli bilgiler sağlayacaktır.

Temel veri manipülasyonundan gelişmiş veri analizi tekniklerine kadar her şeyi ele alacağız ve bu makalenin sonunda, veri bilimi iş akışınızı daha verimli hale getirmek için Pandaları nasıl kullanacağınız konusunda sağlam bir anlayışa sahip olacaksınız.

# **1.pd.read_csv()**

pd.read_csv(), bir CSV (Virgülle Ayrılmış Değerler) dosyasını okumak ve onu bir pandas DataFrame'e dönüştürmek için kullanılan, Python'daki Pandas kitaplığında bulunan bir işlevdir.
"""

import pandas as pd
df = pd.read_csv('CarPrice_Assignment.csv')

"""Bu örnekte, pd.read_csv işlevi "data.csv" dosyasını okur ve onu daha sonra "data" değişkenine atanan bir DataFrame'e dönüştürür. DataFrame içeriği daha sonra yazdırma işlevi kullanılarak yazdırılabilir.

sep, header, index_col, skirows, na_values ​​gibi birçok seçeneğe sahiptir.
"""

df_no_columns = pd.read_csv('CarPrice_Assignment.csv', sep=';', header=0, index_col=0, skiprows=5, na_values='N/A')

"""Bu örnek, data.csv CSV dosyasını ; ile okur. ayırıcı olarak, ilk satırı başlık olarak, ilk sütunu dizin olarak, ilk 5 satırı atlayarak ve N/A yerine NaN koyarak.

# **2. df.describe()**

Pandas kütüphanelerindeki df.describe() yöntemi, bir DataFrame'in çeşitli özelliklerinin özet istatistiklerini oluşturmak için kullanılır. Orijinal DataFrame'deki her sayısal sütunun sayısını, ortalamasını, standart sapmasını, minimumunu, yüzde 25'ini, ortancasını, yüzde 75'ini ve maksimumunu içeren yeni bir DataFrame döndürür.
"""

print(df.describe())

"""Ayrıca, yönteme uygun bağımsız değişkenleri geçirerek belirli sütunları dahil edebilir veya hariç tutabilir ve sayısal olmayan sütunları da dahil edebilirsiniz."""

df.describe(include='all') #tüm sütunları dahil eder

"""Ayrıca, hariç tut yöntemini kullanarak bazı sütunları hariç tutabilirsiniz:"""

df.describe(exclude='number') #sayısal sütunları hariç tutma

"""# **3. df.info()**

df.info() Pandas'ta, her sütundaki boş olmayan değerlerin sayısı, her sütunun veri türleri ve DataFrame'in bellek kullanımı dahil olmak üzere DataFrame'in kısa bir özetini almak için kullanılan bir yöntemdir.
"""

print(df.info())

"""# **4. df.plot()**

df.plot() Pandas'ta bir DataFrame'den çeşitli türlerde grafikler oluşturmak için kullanılan bir yöntemdir. Varsayılan olarak, DataFrame'deki tüm sayısal sütunların bir çizgi grafiğini oluşturur. Ancak oluşturmak istediğiniz çizim türünü belirtmek için kind argümanını da iletebilirsiniz. Mevcut seçenekler çizgi, çubuk, barh, hist, kutu, kde, yoğunluk, alan, pasta, dağılım ve hexbin'dir.

Aşağıdaki örneklerde sayısal ve kategorik değişkenleri çizmek için .plot() yöntemini kullanacağım. Kategorik değişken için çubuk ve pasta grafikleri çizeceğim ve sayısal değişken için kutu grafikleri çizeceğim. Siz de farklı grafik türlerini deneyebilirsiniz.
"""

df['symboling'].value_counts().plot(kind='bar')

df['symboling'].value_counts().plot(kind='pie')

df['enginesize'].plot(kind='box')

"""Ayrıca grafiği özelleştirmek için başlık, xlabel, ylabel, gösterge, ızgara, xlim, ylim, xticks, yticks vb. gibi diğer birçok seçeneği de destekler. Ayrıca özelleştirmek için çizimden sonra plt.xlabel(), plt.ylabel(), plt.title() vb. kullanabilirsiniz.

Lütfen df.plot() işlevinin matplotlib.pyplot kütüphanesi etrafında kullanışlı bir sarmalayıcı olduğunu unutmayın, bu nedenle matplotlib'de bulunan aynı özelleştirme seçenekleri df.plot() için de kullanılabilir.

# **5. df.iloc()**

Pandas'ın .iloc() fonksiyonu, bir DataFrame'de satırları ve sütunları tamsayı tabanlı indekslerine göre seçmek için kullanılır. Satır ve sütunları tamsayı tabanlı konumlarına göre seçmek için kullanılır.

İşte nasıl kullanabileceğinize dair bazı örnekler:
"""

#İlk satırı seçin
print(df.iloc[0])

#İlk iki satırı seçin
print(df.iloc[:2])

#İlk sütunu seçin
print(df.iloc[:, 0])

#İlk iki sütunu seçin
print(df.iloc[:, :2])

#(1,1) öğesini seçin
print(df.iloc[1, 1])

"""Yukarıdaki örneklerde, df.iloc[0] veri çerçevesinin ilk satırını seçer, df.iloc[:2] ilk iki satırı seçer, df.iloc[:, 0] ilk sütunu seçer, df.iloc[:, :2] ilk iki sütunu seçer ve df.iloc[1, 1] veri çerçevesinin (ikinci satır, ikinci sütun) (1, 1) konumundaki öğeyi seçer.

.iloc() yönteminin satırları ve sütunları yalnızca tamsayı tabanlı dizinlerine göre seçtiğini unutmayın, bu nedenle satırları ve sütunları etiketlerine göre seçmek istiyorsanız bunun yerine daha sonra gösterileceği gibi .loc() yöntemini kullanmalısınız.

# **6. df.loc()**

Pandas'ın .loc() fonksiyonu, bir DataFrame'de satırları ve sütunları etiket tabanlı indekslerine göre seçmek için kullanılır. Satır ve sütunları etiket tabanlı konumlarına göre seçmek için kullanılır.

İşte nasıl kullanabileceğinize dair bazı örnekler:
"""

#'CarName' sütununu seçin
print(df.loc[:, 'CarName'])

#'CarName' ve 'car_ID' isimli sütunları seçin
print(df.loc[:, ['car_ID', 'CarName']])

"""Yukarıdaki örnekte, 'CarName' adlı sütunu seçmek için df.loc[:, 'CarName'] kullandık ve df.loc[:, ['car_ID', 'CarName']] 'CarName' ve 'car_ID' adlı sütunları seçer.

# **7. df.assign()**

Pandas'ın .assign() işlevi, mevcut sütunların hesaplanmasına dayalı olarak bir DataFrame'e yeni sütunlar eklemek için kullanılır. Orijinal veri çerçevesini değiştirmeden bir DataFrame'e yeni sütunlar eklemenizi sağlar. Fonksiyon, eklenen sütunlarla birlikte yeni bir DataFrame döndürür.

İşte nasıl kullanabileceğinize dair bir örnek:
"""

df_new = df.assign(count_plus_5=df['enginesize'] + 5)
df_new.head()

"""Yukarıdaki örnekte, df.assign() ilk kez count + 5 değerine sahip 'count_plus_5' adlı yeni bir sütun oluşturmak için kullanılır.

Orijinal DataFrame df'nin değişmeden kaldığına ve eklenen yeni sütunlarla birlikte yeni DataFrame df_new'in döndürüldüğüne dikkat etmek önemlidir.

.assign() yöntemi, bir DataFrame'e tek bir kod satırında birden çok yeni sütun eklemenize olanak tanıyan bir zincir içinde birden çok kez kullanılabilir.

# **8. df.query()**

Pandas'ın .query() işlevi, bir Boolean ifadesine dayalı olarak bir DataFrame'i filtrelemenize olanak tanır. SQL'e benzer bir sorgu dizesi kullanarak bir DataFrame'den satır seçmenize olanak tanır. Fonksiyon, yalnızca Boolean ifadesini karşılayan satırları içeren yeni bir DataFrame döndürür.

# **9. df.sort_values()**

Pandas'ın .sort_values() işlevi, bir DataFrame'i bir veya birden çok sütuna göre sıralamanıza olanak tanır. DataFrame'i bir veya daha fazla sütunun değerlerine göre artan veya azalan sırada sıralar. Fonksiyon, belirtilen sütun(lar)a göre sıralanmış yeni bir DataFrame döndürür.

# **10. df.sample()**

Pandas'ın .sample() fonksiyonu bir DataFrame'den rastgele satırlar seçmenizi sağlar. Rastgele seçilen satırları içeren yeni bir DataFrame döndürür. Fonksiyon, döndürülecek satır sayısı ve tekrarlanabilirlik için değiştirme ve tohumlama ile örnekleme yapılıp yapılmayacağı gibi örnekleme sürecini kontrol etmenizi sağlayan çeşitli parametreler alır.

İşte nasıl kullanabileceğinize dair bir örnek:
"""

df_sample = df.sample(n=3, replace=True, random_state=1)
df_sample

#Seçilecek belirli sütunla değiştirmeden 2 satırı örnekleyin
df_sample = df.sample(n=2, replace=False, random_state=1, axis=1)
df_sample

"""Yukarıdaki örnekte, df.sample() ilk kez 2 satırı değiştirmeden rastgele seçmek için kullanılır, ikinci kez 3 satırı değiştirerek rastgele seçmek için kullanılır ve son kez 2 sütunu değiştirmeden rastgele seçmek için kullanılır.

Orijinal DataFrame df'nin değişmeden kaldığını ve rastgele seçilen satırlarla birlikte yeni DataFrame df_sample'ın döndürüldüğünü unutmamak önemlidir.

.sample() yöntemi, test veya doğrulama için verilerin bir alt kümesini rastgele seçmek istediğinizde veya daha fazla analiz için rastgele bir satır örneği seçmek istediğinizde yararlı olabilir. random_state parametresi tekrarlanabilirlik için kullanışlıdır ve axis=1 parametresi sütunları seçmenize olanak tanır.

# **11. df.isnull()**

Pandas'taki isnull() yöntemi, orijinal DataFrame ile aynı şekle sahip bir DataFrame döndürür, ancak orijinal DataFrame'deki her bir değerin eksik olup olmadığını gösteren True veya False değerlerine sahiptir. NaN veya None gibi eksik değerler, elde edilen DataFrame'de True olurken, eksik olmayan değerler False olur.
"""

df.isnull()

"""# **12. df.fillna()**

Pandas'taki fillna() yöntemi, bir DataFrame'deki eksik değerleri belirtilen bir değer veya yöntemle doldurmak için kullanılır. Varsayılan olarak, eksik değerleri NaN ile değiştirir, ancak bunun yerine aşağıda gösterildiği gibi kullanmak için farklı bir değer belirtebilirsiniz:

**değer**: Eksik değerleri doldurmak için kullanılacak değeri belirtir. Skaler bir değer veya farklı sütunlar için değerlerin bir dict'i olabilir.
**yöntem**: Eksik değerleri doldurmak için kullanılacak yöntemi belirtir. 'ffill' (ileri doldurma) veya 'bfill' (geri doldurma) veya 'interpolate' (değerler arası doldurma) veya 'pad' veya 'backfill' olabilir
**Eksen**: Eksik değerlerin hangi eksen boyunca doldurulacağını belirtir. 0 (satırlar) veya 1 (sütunlar) olabilir.
**inplace**: Eksik değerlerin yerinde doldurulup doldurulmayacağı (orijinal DataFrame'in değiştirilmesi) veya eksik değerlerin doldurulduğu yeni bir DataFrame döndürülüp döndürülmeyeceği.
**limit**: Doldurulacak ardışık eksik değerlerin maksimum sayısını belirtir.
**downcast**: Sütunların veri türlerini düşürmek için kullanılacak bir değerler sözlüğü belirtir.

"""

#eksik değerleri 0 ile doldur
df.fillna(0)

#eksik değerleri ileriye doğru doldurma (son geçerli gözlemi bir sonrakine ilerletir)
df.fillna(method='ffill')

#geriye doğru eksik değerleri doldurma (bir sonraki geçerli gözlemi son gözlemden geriye doğru yayar)
df.fillna(method='bfill')

#enterpolasyon kullanarak eksik değerleri doldurma
df.interpolate()

"""fillna() yönteminin eksik değerleri doldurulmuş yeni bir DataFrame döndürdüğünü ve orijinal DataFrame'i yerinde değiştirmediğini unutmamak önemlidir. Orijinal DataFrame'i değiştirmek istiyorsanız, inplace parametresini kullanabilir ve True olarak ayarlayabilirsiniz."""

#eksik değerleri yerine doldurun
df.fillna(0, inplace=True)

"""# **13. df.dropna()**

df.dropna(), Pandas kütüphanesinde bir DataFrame'den eksik veya null değerleri kaldırmak için kullanılan bir yöntemdir. DataFrame'den en az bir elemanın eksik olduğu satırları veya sütunları kaldırır.

En az bir eksik değer içeren tüm satırları df.dropna() yöntemini çağırarak kaldırabilirsiniz.
"""

df_drop_na = df.dropna()

"""Yalnızca en az bir eksik değer içeren sütunları kaldırmak istiyorsanız df.dropna(axis=1) kullanabilirsiniz"""

df_drop_na = df.dropna(axis=1)

"""thresh parametresini yalnızca en az thresh non-NA/null değerlerine sahip satırları/sütunları tutmak için de ayarlayabilirsiniz."""

df_drop_na = df.dropna(thresh=2)

"""# **14. df.drop()**

df.drop() Pandas kütüphanesinde, ilgili etiketleri belirterek bir DataFrame'den satırları veya sütunları kaldırmak için kullanılan bir yöntemdir. Etiketlerini temel alarak bir veya birden fazla satırı veya sütunu bırakmak için kullanılabilir.

Belirli bir satırı, df.drop() metodunu çağırıp kaldırmak istediğiniz satırın indeks etiketini ve 0 olarak ayarlanmış eksen parametresini (varsayılan değer 0'dır) ileterek kaldırabilirsiniz


"""

df_drop = df.drop(0)

"""Bu, DataFrame'in ilk satırını kaldıracaktır.

İndeks etiketlerinin bir listesini ileterek birden fazla satırı da düşürebilirsiniz:
"""

df_drop = df.drop([0,1])

"""Bu, DataFrame'in birinci ve ikinci satırlarını kaldıracaktır.

Benzer şekilde, kaldırmak istediğiniz sütunların etiketlerini ileterek ve axis parametresini 1 olarak ayarlayarak sütunları düşürebilirsiniz:
"""

df_drop = df.drop(['enginesize'], axis=1)

"""# **15. pd.pivot_table()**

pd.pivot_table(), Pandas kütüphanesinde bir DataFrame'den pivot tablo oluşturmak için kullanılan bir yöntemdir. Pivot tablo, indeks olarak bir veya daha fazla sütun, değer olarak bir veya daha fazla sütun ve öznitelik olarak bir veya daha fazla sütun içeren yeni bir tablo oluşturarak verileri daha anlamlı ve düzenli bir şekilde özetleyen ve toplayan bir tablodur.

Aşağıdaki örnekte, indeks olarak Ethnicity ile bir pivot tablo oluşturacağız ve sayım toplamını toplayacağız. Bu, veri kümesindeki her bir Etnik Köken'in sayısını bilmek için kullanılır.

"""

pivot_table = pd.pivot_table(df, index='fueltype', values='symboling', aggfunc='sum')
pivot_table.head()

"""# **16. df.groupby()**

df.groupby(), Pandas kütüphanesinde bir DataFrame'in satırlarını bir veya birden fazla sütuna göre gruplamak için kullanılan bir yöntemdir. Bu, gruplar üzerinde her gruptaki değerlerin ortalamasını, toplamını veya sayısını hesaplamak gibi toplu işlemler gerçekleştirmenize olanak tanır.

df.groupby() bir GroupBy nesnesi döndürür; bu nesneyi daha sonra gruplar üzerinde, her gruptaki değerlerin toplamını, ortalamasını veya sayısını hesaplamak gibi çeşitli işlemler gerçekleştirmek için kullanabilirsiniz.

Doğum adları veri kümesini kullanarak bir örnek görelim:

"""

grouped = df.groupby('symboling')
#Her grubun ortalamasını yazdır
print(grouped.mean())

grouped = df.groupby(['symboling', 'fuelsystem'])

#Her grubun toplamını yazdır
print(grouped.sum())

"""# **17. df.transpose()**

df.transpose(), Pandas kütüphanesinde bir DataFrame'in satır ve sütunlarının yerlerini değiştirmek için kullanılan bir yöntemdir? Bu, satırların sütunlara ve sütunların satırlara dönüşmesi anlamına gelir.


"""

#DataFrame'i Transpoze Etme
df_transposed = df.transpose()

#Dönüştürülmüş DataFrame'i yazdır
df_transposed.head()

"""Veri çerçevesi üzerinde T nitelikleri kullanılarak da yapılabilir. df.T, df.transpose() ile aynı işlemi yapacaktır."""

df_transposed = df.T
df_transposed.head()

"""# **18. df.merge()**

df.merge(), bir veya daha fazla ortak sütuna dayalı olarak iki DataFrame'i birleştirmenize olanak tanıyan bir pandas işlevidir. SQL JOIN'lerine benzer. Fonksiyon, yalnızca belirtilen sütunlardaki değerlerin iki DataFrame arasında eşleştiği satırları içeren yeni bir DataFrame döndürür.

Ortak bir sütuna dayalı olarak iki DataFrame'i birleştirmek için df.merge() fonksiyonunun nasıl kullanılacağına ilişkin bir örnek aşağıda verilmiştir:
"""

#İlk DataFrame'i oluşturun
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 4]})
#İkinci DataFrame'i oluşturun
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value': [5, 6, 7, 8]})
#İki DataFrame'i 'anahtar' sütununda birleştirin
merged_df = df1.merge(df2, on='key')
#Birleştirilmiş DataFrame'i yazdır
print(merged_df)

"""# **19. df.rename()**

df.rename(), bir DataFrame'deki bir veya daha fazla sütunun veya satırın adını değiştirmenize olanak tanıyan bir pandas fonksiyonudur. Sütun adlarını değiştirmek için columns parametresini, satır adlarını değiştirmek için ise index parametresini kullanabilirsiniz.
"""

#'Count' sütununu 'count' olarak yeniden adlandırın
df_rename = df.rename(columns={'symboling': 'Symboling'})
df_rename.head()

"""Dizini de benzer şekilde yeniden adlandırabilirsiniz:"""

df_rename = df.rename(index={0: 'first', 1:'second', 2:'third'})
df_rename.head()

"""# **20. df.to_csv()**

df.to_csv(), Pandas kütüphanesinde bir DataFrame'i CSV dosyasına aktarmak için kullanılan bir yöntemdir. CSV, "Virgülle Ayrılmış Değerler" anlamına gelir ve verileri tablo biçiminde saklamak için kullanılan popüler bir dosya biçimidir.

Örneğin, bir CSV dosyasına aktarmak istediğiniz df'yi kaydetmek istediğimizi varsayalım. DataFrame'i df.to_csv() çağrısı yaparak ve dosya adını bir string olarak geçirerek bir CSV dosyasına aktarabilirsiniz:
"""

df.to_csv('data.csv')

"""CSV dosyasında kullanılan ayırıcıyı sep parametresini geçerek de belirtebilirsiniz. Varsayılan olarak "," olarak ayarlanmıştır.

"""

df.to_csv('path/to/data.csv', sep='\t')

"""Sütun adları listesini columns parametresine geçirerek DataFrame'in yalnızca belirli sütunlarını kaydetmek ve ayrıca index parametresine bir boolean maskesi geçirerek yalnızca belirli satırları kaydetmek de mümkündür.

"""

df.to_csv('path/to/data.csv', columns=['enginesize'])

"""Veri çerçevesinin dizininin dışa aktarılan CSV dosyasına dahil edilip edilmeyeceğini belirtmek için dizin parametresini de kullanabilirsiniz.

Bu, dışa aktarılan CSV dosyasındaki veri çerçevesinin indeksini hariç tutacaktır.

Dışa aktarılan CSV dosyasındaki eksik değerleri belirli bir değerle değiştirmek için na_rep parametresini de kullanabilirsiniz.
"""

df.to_csv('path/to/data.csv', na_rep='NULL')

"""**Özet olarak, veri görevlerinizin çoğunu gerçekleştirmek için kullanılabilecek 20 pandas işlevi aşağıda verilmiştir:**

pd.read_csv()

df.describe()

df.info()

df.plot()

df.iloc()

df.loc()

df.assign()

df.query()

df.sort_values()

df.sample()

df.isnull()

df.fillna()

df.dropna()

df.drop()

pd.pivot_table()

df.groupby()

df.transpose()

df.merge()

df.rename()

df.to_csv()
"""