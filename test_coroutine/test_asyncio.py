import aiohttp
import asyncio
import time


async def downone(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.ensure_future(downone(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'https://www.baidu.com',
        'https://cn.bing.com/',
        'https://www.sina.com.cn/'
    ]
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(download_all(sites))
    finally:
        # loop.close()
        pass
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

# ***************************************************************************************


def test_define_coroutine():
    async def do_some_work(x):
        print('waiting: {}'.format(x))

    now = lambda: time.perf_counter()

    start = now()
    coroutine = do_some_work(4)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    loop.close()
    print('Time lost: %s' % (now() - start))

# ***************************************************************************************


def test_task():
    async def do_some_work(x):
        print('waiting: {}'.format(x))

    now = lambda :time.perf_counter()
    start = now()
    coroutine = do_some_work(4)
    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine)
    task = loop.create_task(coroutine)
    print(task)
    loop.run_until_complete(task)
    print(task)
    print('Time lost: %s' % (now() - start))


# ***************************************************************************************


def test_await():
    async def do_some_work(x):
        print('Waiting: {}'.format(x))
        await asyncio.sleep(x)
        return "Done after {}s".format(x)

    now = lambda: time.perf_counter()
    start = now()
    coroutine = do_some_work(4)
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    loop.run_until_complete(task)
    print('Task ret: ', task.result())
    print('Time lost: %s' % (now() - start))


# ***************************************************************************************


def test_concurrent_using_asyncio():
    async def do_some_work(x):
        print('Waiting: {}'.format(x))
        await asyncio.sleep(x)
        return "Done after {}s".format(x)

    now = lambda: time.perf_counter()
    start = now()
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [asyncio.ensure_future(coroutine1),
             asyncio.ensure_future(coroutine2),
             asyncio.ensure_future(coroutine3)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print("Task ret: ", task.result())
    print('Time lost: %s' % (now() - start))


if __name__ == "__main__":
    # main()

    # test_define_coroutine()

    # test_task()

    # test_await()

    test_concurrent_using_asyncio()
