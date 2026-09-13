class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:   
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        counts.sort(reverse=True)
        max_freq = counts[0]
        # Number of gaps between the most frequent tasks
        gaps = max_freq - 1
        # Each gap needs n slots
        empty_slots = gaps * n
        # Fill those slots using the other tasks
        for count in counts[1:]:
            empty_slots -= min(count, gaps)
        # Whatever slots remain have to be idle
        if empty_slots > 0:
            return len(tasks) + empty_slots
        return len(tasks)
                


            





       
             

