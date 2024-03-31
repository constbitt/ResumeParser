class CustomMatcher:
    def __init__(self, patterns):
        self.patterns = patterns

    def match(self, text):
        matches = []
        for i in range(len(text)):
            matches.extend(self._match_pattern(text[i:], i))
        return matches

    def _match_pattern(self, text, start_index):
        matched_indices = []
        for pattern in self.patterns:
            match, end_index = self._match_sequence(text, pattern)
            if match:
                matched_indices.append((start_index, start_index + end_index))
        return matched_indices

    def _match_sequence(self, text, pattern):
        next_index = 0
        for i, token_pattern in enumerate(pattern):
            if i >= len(text):
                return False, next_index
            if not self._match_token(text[i], token_pattern):
                if token_pattern.get("OP") == "?":
                    continue
                else:
                    return False, next_index
            next_index += 1
        return True, next_index

    def _match_token(self, token, token_pattern):
        for key, value in token_pattern.items():
            if key == "TEXT":
                if token != value:
                    return False
            elif key == "OP":
                if value == "?" and token not in token_pattern.get("IN", []):
                    return True
            elif key == "IN":
                if token not in value:
                    return False
            elif key == "ANY":
                return True
        return True
