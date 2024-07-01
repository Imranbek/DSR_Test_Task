Чеклист

1. Все поля пустые + проверить порядок элементов и ошибок на странице
    test_submit_no_fields_are_filled
2. Все поля заполнены валидными данными (перебрать варианты должности, пола. использовать максимальную длину для имен)
    test_all_fields_are_filled_with_diff_gender
    test_all_fields_are_filled_with_diff_vacancy
3. Валидный телефон (корнер кейсы)
    test_valid_phone
3. Невалидные телефон
    test_invalid_phone
4. Невалидный имейл
    test_invalid_email
5. Невалидные имя и фамилия
    test_invalid_length_names
6. Проверить список вакансий на полноту
    test_submit_no_fields_are_filled
7. Подставить разные варианты форматов CV (pdf, txt, html, docx)
   test_all_fields_are_filled_with_diff_cv_format

Проблемы в текущей реализации:
Длина email не ограничена разумным количеством знаков
В итоговой форме не отображается информация о файле с CV