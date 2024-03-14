# goit-algo-hw-09

## Висновки щодо алгоритмів видачі решти

### Жадібний алгоритм (`find_coins_greedy`)
- **Швидкість**: Висока на всіх тестованих сумах.
- **Оптимальність**: Забезпечує оптимальне рішення зі стандартним набором монет, але може бути неоптимальним для певних спеціалізованих наборів.

### Алгоритм динамічного програмування (`find_min_coins`)
- **Швидкість**: Повільніший за жадібний на великих сумах через більшу кількість обчислень.
- **Оптимальність**: Гарантує мінімальну кількість монет для будь-якої суми та набору монет.

### Рекомендації
- Використовуйте **жадібний алгоритм** для швидкого вирішення задачі зі стандартним набором монет.
- Оберіть **алгоритм динамічного програмування**, якщо потрібна гарантована оптимальність з будь-яким набором монет або для великих сум.
