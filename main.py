from double_linked_list import LinkedList, Node

class HomeWork(LinkedList):
    def insert_at_index(self, data, index):
        """ Вставляет элемент по индексу. Start_index=1 """
        new_node = Node(data)
        if index == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {index}"
        """Опционально"""
        current_node = self.head
        if index > len(LinkedList.List):
            self.insert_at_tail(data)
            return
        current_index = 1
        while current_node is not None and current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        """Если есть опционально (код выше то следующие 2 строки не нужны)"""
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        HomeWork.List.insert(index - 1, new_node.data)
        return f"Узел с данными {new_node.data} добавлен на позицию {index}"

    def remove_by_index(self, index):
        """Удаляет данные списка по индексу. Start_index=1"""
        if index == 1:
            removed_node = self.head
            self.head = self.head.next_node
            LinkedList.List.pop(0)
            return f"Удален узел с данными {removed_node.data} позиции {index}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < index - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node  # removed_node.next_node
        LinkedList.List.pop(index)
        return f"Удален узел с данными {removed_node.data} позиции {index}"

    def remove_by_data(self, data):
        if self.contains_from_head(data):
            LinkedList.List.remove(data)
            return True
        return False

    def contains_from(self, data, end=None):
        if end:
            return True if self.contains_from_tail(data) else False
        return True if self.contains_from_head(data) else False

    @staticmethod
    def len_ll():
        return len(LinkedList.List)

    @staticmethod
    def contains_from_head(data):
        return True if data in LinkedList.List else False

    @staticmethod
    def contains_from_tail(data):
        return True if data in LinkedList.List[::-1] else False

    @staticmethod
    def print_ll_form_tail():
        """ Печатает список с конца """
        return LinkedList.List[::-1]
            



if __name__ == '__main__':
    homework = HomeWork()
    # Добавляем элементы в список и выводим список в обратном порядке на печать
    homework.insert_at_index(111, 1)
    homework.insert_at_index(112, 2)
    homework.insert_at_index(113, 3)
    homework.insert_at_index('very big index=30', 30)
    homework.insert_at_index('new index=2', 2)
    print(f'Вывод списка в обратном порядке = {homework.print_ll_form_tail()}')
    print()
    # Удаление данных по индексу и вывод результата на печать
    homework.remove_by_index(2)
    print(f'Удаление из списка по индексу (2, номер 112) = {homework.print_ll_form_tail()}')
    print()
    # Удаление данных по данным и вывод результата на печать
    homework.remove_by_data('new index=2')
    print(f'Удаление из списка "new index=2" = {homework.print_ll_form_tail()}')
    print()
    # Длина списка
    print(f'Длина списка = {homework.len_ll()}')
    print()
    # Проверка на содержание элемента с головы списка
    print(f'Ищем элемент "113" в списке. Результат поиска с головы списка = {homework.contains_from_head(113)}')
    print(f'Ищем элемент "114" в списке. Результат поиска с головы списка = {homework.contains_from_head(114)}')
    print()
    # Проверка на содержание элемента с конца списка
    print(f'Ищем элемент "113" в списке. Результат поиска с конца списка = {homework.contains_from_tail(113)}')
    print(f'Ищем элемент "114" в списке. Результат поиска с конца списка = {homework.contains_from_tail(114)}')
    print()
    # Предоставляем выбор
    choice = int(input('Как вы хотите проверить свои данные?\n1. С начала\n2. С конца\n-> '))
    if choice == 1:
        print(f'Ищем элемент "111" с начала в списке = {homework.contains_from(111)}')
        print(f'Ищем элемент "50" с начала в списке = {homework.contains_from(50)}')
    else:
        print(f'Ищем элемент "111" с конца в списке = {homework.contains_from(111)}')
        print(f'Ищем элемент "50" с конца в списке = {homework.contains_from(50)}')

