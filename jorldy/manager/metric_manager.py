from collections import defaultdict


class MetricManager:
    def __init__(self):
        self.metrics = defaultdict(list)

    def append(self, result):
        for key, value in result.items():
            self.metrics[key].append(value)

    def get_statistics(self, mode="mean"):
        ret = dict()
        if mode == "mean":
            for key, value in self.metrics.items():
                ret[key] = round(sum(value) / len(value), 4)
        self.metrics.clear()
        return ret
