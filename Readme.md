Задание 1
Подключите СУБД PostgreSQL для работы в проекте, для этого:

Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения.
Мы уже работали с этой СУБД на курсе «Работа с базами данных». В уроке 17.1 «Введение в работу с базами данных» подробно описан процесс создания базы данных.

Задание 2
В приложении каталога создайте модели:

Product,
Category.
Опишите для них начальные настройки.

К начальным настройкам модели относятся метод 
__str__
 и 
class Meta
 с описанием свойств модели.

Задание 3
Для каждой модели опишите следующие поля:

Product
Наименование
Описание
Изображение (превью)
Категория
Цена за покупку
Дата создания (записи в БД)
Дата последнего изменения (записи в БД)
Category
Наименование
Описание
Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».

У одной категории может быть много продуктов, но у одного продукта может быть только одна категория.

Воспользуйтесь специальным полем модели — ForeignKey().
При необходимости подробнее про то, как работает такое поле, можно почитать тут.

Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. Их общепринятые названия — created_at и updated_at соответственно.

 
Примечание

Для поля с изображением необходимо добавить соответствующие настройки (MEDIA URL, MEDIA ROOT, настроить URL для отображения медиаданных) в проект, а также установить библиотеку для работы с изображениями 
Pillow
. Не забудьте обновить файл с зависимостями для проекта после установки новой библиотеки.

Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций, для этого:

создайте миграции для новых моделей;
примените миграции;
внесите изменения в модель продукта, добавьте поле «Дата производства продукта» (
manufactured_at
), примените обновление структуры с помощью миграций;
откатите миграцию до состояния, когда поле «Дата производства продукта» (
manufactured_at
) для модели продукта еще не существовало, и удалите лишнюю миграцию.
Важно сохранять всю историю миграций проекта для сохранения целостности базы данных проекта.

Не забудьте добавить все выполненные миграции в коммит, а затем отправить в удаленный репозиторий на GitHub.

Подсказка
 

Задание 5
Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.

При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

 

Подсказка
 

Задание 6
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
Установите библиотеку 
ipython
 для комфортной работы с инструментом 
shell
. Не забудьте зафиксировать изменения в файле зависимостей проекта.

 

Подсказка
 

Сформируйте фикстуры для заполнения базы данных.
Фикстуры создайте командой. Для управления кодировкой используйте опцию 
-Xutf8
 для команды. Такой параметр уместно будет использовать на операционной системе Windows.

В общем случае команда для создания фикстур будет выглядеть следующим образом:

python -Xutf8 manage.py dumpdata имя_приложения > имя_папки_с_фикстурами/имя_приложения_data.json
Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от старых данных.