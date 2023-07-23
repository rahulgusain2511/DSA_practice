def minDays (self, bloomDay, m, k ):
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        result = max(bloomDay)
        while low <= high:
            mid = (low+high)// 2
            flowers = 0
            bouquets = 0
            for val in bloomDay:
                if mid >= val:
                    flowers += 1
                else:
                    flowers = 0
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            if bouquets >= m:
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        return result