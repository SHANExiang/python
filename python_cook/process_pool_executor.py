from concurrent.futures import ProcessPoolExecutor
import glob
import gzip
import io


def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots_map(dir):
    files = glob.glob(dir + '/*.log.gz')
    all_robots = set()
    print(map(find_robots, files))
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


def find_all_robots_pool(dir):
    files = glob.glob(dir + '*.log.gz')
    all_robots = set()
    with ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots



