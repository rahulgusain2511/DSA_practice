def shipWithinDays(self,weights, days):
    
        lo = max(weights)  
        hi = sum(weights)
        while lo<=hi:
            mid = (lo+hi)//2  # fixing a capacity as mid for checking       
            cur_sum = 0
            d=1               
            cur_sum = 0
            for i in weights:
                if cur_sum + i <= mid: 
                     cur_sum += i   # if capacity increased increase the day by one and set/store the capacity
                    
                else:
                    cur_sum = i
                    d+=1
            
            if d>days:
                lo = mid +1     # if days exceed than given increase the capacity
            else:
                hi = mid -1     # if work got completed in less days than given decrease the assumed capacity
        return lo