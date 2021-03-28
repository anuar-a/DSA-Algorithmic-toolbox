# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          #print(self.assigned_workers[i][1], self.start_times[i])
          print(self.start_times[i][0],self.start_times[i][1])

    def LeftChild(self,i):
        return 2*(i+1) -1

    def RightChild(self,i):
        return 2*(i+1)

    def Parent(self,i):
        return math.floor(i/2)

    def Compare(self, thread1, thread2):
        if thread1[1] != thread2[1]:
            return thread1[1] < thread2[1]
        else:
            return thread1[0] < thread2[0]

    def ChangePriority(self, i, priority):
        old_p = self.assigned_workers[i][1]
        self.assigned_workers[i] = (self.assigned_workers[i][0], priority)
        if priority < old_p:
            self.SiftUp(i)
        else:
            self.SiftDown(i)

    def SiftUp(self, i):
        while i > 1 and self.Compare(self.assigned_workers[i], self.assigned_workers[self.Parent(i)]):
            self.assigned_workers[self.Parent(i)], self.assigned_workers[i] = self.assigned_workers[i], self.assigned_workers[self.Parent(i)]
            i = self.Parent(i)

    def SiftDown(self, i):
        minIndex = i
        l = self.LeftChild(i)
        if l <= (len(self.assigned_workers)-1) and self.Compare(self.assigned_workers[l], self.assigned_workers[minIndex]):
            minIndex = l
        r = self.RightChild(i)
        if r <= (len(self.assigned_workers)-1) and self.Compare(self.assigned_workers[r], self.assigned_workers[minIndex]):
            minIndex = r

        if i != minIndex:
            self.assigned_workers[i], self.assigned_workers[minIndex] = self.assigned_workers[minIndex], self.assigned_workers[i]
            self.SiftDown(minIndex)

    def ExtractMin(self,i):
        result = self.assigned_workers[0]
        return result

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [(i,0) for i in range(self.num_workers)]
        self.start_times = [] * len(self.jobs)

        for i in self.jobs:
            self.start_times.append(self.ExtractMin(i))
            self.ChangePriority(0, self.assigned_workers[0][1] + i)




    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
