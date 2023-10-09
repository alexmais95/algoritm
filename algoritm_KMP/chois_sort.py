import random


class Sort:

    def find_min_element(self, lis_t):
        min_elem = lis_t[0]
        index_min_element = 0
        for i in range(1, len(lis_t)):
            if lis_t[i] < min_elem:
                min_elem = lis_t[i]
                index_min_element = i
        return index_min_element

    def sort_list(self, lis_t):
        sorted = []
        for i in range(len(lis_t)):
            min = self.find_min_element(lis_t)
            sorted.append(lis_t.pop(min))
        return sorted



sort = Sort()
print(sort.sort_list([l for l in range(random.randint(1, 1000))]))