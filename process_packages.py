# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived", "time"])
Response = namedtuple("Response", ["drop", "start"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here

        while len(self.finish_time) > 0 and self.finish_time[0] <= request.arrived :
            self.finish_time.pop(0)

        if len(self.finish_time) < self.size:
            if len(self.finish_time) == 0:
                self.finish_time.append(request.arrived + request.time)
                return Response(True, request.arrived)
            else:
                start_time = request.arrived
                if self.finish_time[-1] > start_time:
                    start_time = self.finish_time[-1]
                elif self.finish_time[-1] == start_time:
                    start_time = self.finish_time[-1] 
                self.finish_time.append(start_time + request.time)
                return Response(True, start_time)
        else:
            return Response(False, -1)

def process_requests(requests, buffer):
    if len(requests) == 0:
        return
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    if n_requests == 0:
        return
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.start if response.drop else -1)


if __name__ == "__main__":
    main()
