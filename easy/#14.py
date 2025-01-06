from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    common_chars = set(strs[0])
    for str_ in strs[1:]:
        common_chars = common_chars & set(str_)

    if len(common_chars) == 0:
        return ""
    if len(common_chars) == strs[0]:
        return strs[0]

    max_idx = 0
    for idx, char in enumerate(strs[0]):
        for str_ in strs[1:]:
            if len(str_) - 1 < idx or str_[idx] not in common_chars or str_[idx] != char:
                result = str_[:max_idx]
                return result
        max_idx += 1

    return strs[0][:max_idx]



