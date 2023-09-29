## Актуальные гипотезы

1. **Какова эффективность работы службы привлечения клиентов?**
    1. Коэффициент становление клиентом из посетителя за весь период равен: **0.28** (11)
    2. Число посетителей за весь период равно: **49239.00** (12)
2. **Какова эффективность работы службы отгрузки товаров?**
    1. Средний объем продуктовой корзины покупателя за весь период равен: **2.06** (13)
    2. Товарооборот за весь период равен: **3667.00** (14)
3. **Какова удовлетворенность клиентов от взаимодействия с сайтом?**
    1. Среднее количество элементов в корзине клиента за весь период равно: **1.24** (16)
    2. Среднее время браузинга пользователем товаров на сайте за весь период равно: **19.31** (17)
    3. **При формировании своей продуктовой корзины, покупатель с большей степенью воспользуется КАТАЛОГОМ, нежели
       ПОИСКОМ** (19)
    4. Среднее количество переходов от одного пользователя за весь период равно: **4.72** (21)
4. **Какие есть возможности по повышению эффективности интернет-магазина?**
    1. **Общее число запросов КАТАЛОГ, не меньше чем ПОИСК** (6)
    2. Последний запрос пользователя за сессию является ORDER, а не любой другой с вероятностью: 0.04 (10)
    3. Задача об ассоциативных правилах (смотри сгенерированный граф) (20)
   
## Ассоциативные правила (raw):
[('2', '4', 1102), ('3', '7', 1120), ('7', '3', 1120), ('1', '6', 207), ('24', '6', 56), ('9', '0', 1058), ('0', '9', 1058), ('55', '6', 182), ('4', '2', 1102), ('90', '3', 46), ('8', '2', 227), ('6', '2', 267), ('5', '6', 263), ('83', '0', 208), ('60', '2', 181), ('79', '2', 185), ('14', '3', 169), ('73', '4', 59)]


---

## Архив гипотез:

1. При покупке предмета **(ID предмета)**, также покупают **(ID предмета)** (4)
    * переписана, стала основой задаче о кластеризации
2. Среднее количество покупок с использованием **КАТАЛОГА** больше, чем с использованием **ПОИСКА** (7)
    * переписана, стала основой гипотезы (19)
3. При использовании **КАТАЛОГА** пользователь добавляет предмет в корзину чаще, чем после **ПОИСКА** (1)
    * не используется
4. При добавлении предмета с использованием **КАТАЛОГА** пользователь добавляет следующий предмет в корзину чаще, чем
   при использовании **ПОИСКА** (2)
    * не используется
5. При добавлении предмета с использованием **ПОИСКА**, пользователь чаще не добавляет других предметов в корзину (3)
    * не используется
6. Среднее количество покупок у пользователя больше чем **$VAL** _(к примеру 1)_ (5)
    * Переписана, стала основой гипотезы (15)
7. Пользователь при использовании **КАТАЛОГА**, после этого чаще переходит в **ПОИСК** (8)
    * не используется, было отдано предпочтение гипотезе (6)
8. Среднее количество покупок с использованием **КАТАЛОГА** больше, чем с использованием **ПОИСКА** (9)
    * не используется

---

### ~~Пояснение~~ (устарело из-за неактуальности гипотез)

1. Проверяется эффективность работы способов привлечения клиентов к покупке книги: через поиск и через каталог. Эта
   гипотеза проверяет, какой из методов является более эффективным.
2. Проверяется эффективность работы метода "каталог". Если пользователь использует каталог, рассматривается,
   способствует ли это добавлению нескольких предметов в корзину.
3. Проверяется эффективность работы поиска. Если пользователь заинтересован в поиске конкретной книги, вероятность того,
   что он добавит другие предметы в корзину, ниже.
4. Проверяется, с какой частотой пользователь при покупке одного предмета переходит к покупке соответствующего по
   гипотезе другого предмета.
5. Проверяется количество покупок у пользователя. Если пользователя удовлетворяют предложенные ему варианты, среднее
   количество покупок будет больше.
6. Если число запросов в каталог меньше, чем в поиск, то возможным улучшением будет изменение алгоритма предложения
   книг, так как каталог не справляется с удержанием пользователей.
7. Проверяется удержание клиента на сайте. Чем больше времени пользователь проводит при осмотре интересующих его
   товаров, тем более удовлетворен он будет.
8. Пользователям, неудовлетворенным фильтрами каталога, может быть проще найти конкретные предметы с помощью поиска.
   Возможным улучшением будет изменение фильтров каталога.
9. Проверяются все покупки. Если покупок, совершенных с помощью каталога, было больше, это указывает на эффективность
   метода "каталог".
10. Если последний запрос пользователя - "ADDBASKET", это означает, что сайт не предоставляет способов удержания
    пользователя на сайте. Возможным улучшением будет предложение перехода в каталог с похожими книгами.