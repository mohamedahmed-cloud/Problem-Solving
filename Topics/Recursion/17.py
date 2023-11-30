#!/bin/bash

import string
from typing import Optional, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
            lowerCase = string.ascii_lowercase
            ans = []
            def prepare(digits):
                for i in digits:
                    if int(i) in range(2,7):
                        ans.append(list(lowerCase[(int(i) - 2 ) * 3 : (int(i) - 1) * 3 ]))
                
                    else:
                        if int(i) == 7:
                            ans.append(list("pqrs"))
                        elif int(i) == 8:
                            ans.append(list("tuv"))
                        else:
                            ans.append(list("wxyz"))
            prepare(digits)

            res = []
            def find(idx, compine ):
                if idx >= len(digits):
                    if compine:res.append(compine)
                    return
                for i in ans[idx]:
                    find(idx + 1, compine + i)

            find(0, "")
            return res
    
slv = Solution()
print(slv.letterCombinations("22"))