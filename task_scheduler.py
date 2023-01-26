class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fre = {}
        for task in tasks:
            if task not in fre: fre[task]= 1
            else: fre[task]+=1
        freq = [value for key, value in fre.items()]
        max_freq = max(freq)
        max_freq_task = freq.count(max_freq)
        return max(len(tasks), (max_freq - 1) *(n + 1) + max_freq_task)
