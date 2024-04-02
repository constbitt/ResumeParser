class ListCleaner:
    def __init__(self, words):
        self.words = words

    def clean_words(self, words):
        #words = self.remove_subsets(words)
        words = self.filter_unique(words)
        words = self.remove_almost_subsets(words)
        return words


    def leave_almost_subsets(self, words):
        words = self.remove_subsets(words)
        words = self.filter_unique(words)
        return words

    def filter_unique(self, words):
        unique_lists = []
        unique_set = set()
        for word_list in words:
            word_tuple = tuple(sorted(word_list))
            if word_tuple not in unique_set:
                unique_set.add(word_tuple)
                unique_lists.append(word_list)
        return unique_lists


    def remove_subsets(self, words):
        unique_lists = []
        for word_list in words:
            is_unique = True
            for other_list in words:
                if word_list != other_list and set(word_list).issubset(set(other_list)):
                    is_unique = False
                    break
            if is_unique:
                unique_lists.append(word_list)
        return unique_lists


    def check_string_subset(self, str1, str2):
        if str1.lower() in str2.lower():
            return len(str1) / len(str2)
        else:
            return 0


    def calculate_total_percent(self, list1, list2):
        smaller_list = list1 if len(list1) < len(list2) else list2
        larger_list = list2 if len(list1) < len(list2) else list1
        total_percent = 0
        for word1 in smaller_list:
            for word2 in larger_list:
                total_percent += self.check_string_subset(word1, word2)
        match_percent = (total_percent / len(smaller_list))
        return match_percent


    def remove_almost_subsets(self, lists):
        indexes_to_remove = set()
        for i in range(len(lists)):
            for j in range(len(lists)):
                if i != j and self.calculate_total_percent(lists[i], lists[j]) >= 0.8:
                    if len(lists[i]) > len(lists[j]):
                        indexes_to_remove.add(j)
                    if len(lists[i]) < len(lists[j]):
                        indexes_to_remove.add(i)
        result = [lists[i] for i in range(len(lists)) if i not in indexes_to_remove]
        return result


