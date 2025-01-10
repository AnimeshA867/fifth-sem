class Job: 
    def __init__(self,job_id,deadline,profit) -> None:
        self.job_id= job_id;
        self.deadline= deadline;
        self.profit= profit;
        

def job_sequencing(jobs,max_deadline):
    jobs.sort(reverse=True,key=lambda x:x.profit)

    slots = [-1]*max_deadline;
    
    totalProfit=0;
    for job in jobs:
        
        for i in range (min(max_deadline,job.deadline)-1,-1,-1):
            if(slots[i]==-1):
                slots[i]=job.job_id;
                totalProfit+= job.profit;
                break;
            
    return totalProfit,slots;

jobs = [
    Job('Job1', 2, 60),
    Job('Job2', 1, 100),
    Job('Job3', 3, 20),
    Job('Job4', 2, 40),
    Job('Job5', 1, 20)
]

# Maximum deadline across jobs
max_deadline = 3

profit, job_sequence = job_sequencing(jobs, max_deadline)
print("Total Profit:", profit)
print("Job Sequence:", job_sequence)
