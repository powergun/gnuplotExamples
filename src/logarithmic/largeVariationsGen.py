
import random
import sys


class Point(object):
    
    def __init__(self, base_value, deviation):
        self._base_value = base_value
        self._deviation = deviation
    
    def y(self):
        return self._base_value * (1 - random.random() * self._deviation)


def iter_segments(from_p, to_p, num_segments):
    segment_size = (to_p - from_p + 1) / float(num_segments)
    half_size = segment_size / 2
    for x in xrange(from_p, to_p):
        distance = float(x - from_p + 1) % segment_size
        ratio = 1.0
        if distance >= 0:
            if distance < half_size:
                yield x, False, ratio
        yield x, True, ratio
    
    
def gen(from_p, to_p, num_peaks=3, deviation=0.75, min_=40, max_=4000):
    for x, is_peak, ratio in iter_segments(from_p, to_p, num_peaks):
        if is_peak:
            base_value = max_ * ratio
        else:
            base_value = min_ * ratio
        print x, Point(base_value, deviation).y()
        
        
def test():
    print list(iter_segments(1, 18, 3))


if __name__ == '__main__':
    if not sys.argv[1:]:
        test()
    else:
        from_ = int(sys.argv[1])
        to_ = int(sys.argv[2])
        gen(from_, to_)
