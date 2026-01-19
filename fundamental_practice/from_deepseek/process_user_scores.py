def process_scores(scores):
    if scores == []:
        return (0, [], 0)        
    total = 0
    high_score = []
    fail_count = 0
    for nums in scores:        
        if nums > 90:
            high_score.append(nums)
        elif nums < 60:
            fail_count += 1       
        total += nums
    average = sum(scores) / len(scores)
    return (average, high_score, fail_count)
    
   
       
print(process_scores([85, 92, 78, 90, 55, 96, 42, 88, 73]))